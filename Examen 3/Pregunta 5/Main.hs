-- 5. Considere las funciones foldr y const, escritas en un lenguaje muy similar a Haskell:


foldr :: (a -> b -> b) -> b -> [a] -> b
foldr _ e []        = e
foldr f e (x:xs)    = f x $ foldr f e xs

const :: a -> b -> a
const x _ = x

-- Considere también la siguiente función que aplica una función solamente sobre la cola de una lista y agrupa la cabeza con otro valor dado:


what :: a -> ([b] -> [(a, b)]) -> [b] -> [(a, b)]
what _ _ []     = []
what x f (y:ys) = (x, y) : f ys


-- 5.a) Considere la siguiente implementación de una función misteriosa, usando foldr:
misteriosa :: ???
misteriosa = foldr what (const [])

--Considere también la siguiente función, que genera una lista de números enteros a partir de un cierto valor inicial:
gen :: Int -> [Int]
gen n = n : gen (n + 1)

{-
Muestre la evaluación, paso a paso, de la expresión misteriosa "abc" (gen 1), con-
siderando que:
i. El lenguaje tiene orden de evaluación normal.
ii. El lenguaje tiene orden de evaluación aplicativo.
-}

------------------ RESPUESTA 5.a ------------------

--- i) Orden de evaluación Normal:

misteriosa "abc" (gen 1)
=
foldr what (const []) "abc" (gen 1)
=
what "a" $ foldr what (const []) "bc" (gen 1)
=
what "a" $ foldr what (const []) "bc" (1 : gen 2)
=
("a", 1) : $ foldr what (const []) "bc" (gen 2)
=
("a", 1) : what "b" $ foldr what (const []) "c" (gen 2)
=
("a", 1) : what "b" $ foldr what (const []) "c" (2 : gen 3)
=
("a", 1) : ("b", 2) : $ foldr what (const []) "c" (gen 3)
=
("a", 1) : ("b", 2) : what "c" $ foldr what (const []) "" (gen 3)
=
("a", 1) : ("b", 2) : what "c" $ foldr what (const []) "" (3 : gen 4)
=
("a", 1) : ("b", 2) : ("c", 3) $ foldr what (const []) "" (gen 4)
=
("a", 1) : ("b", 2) : ("c", 3) : (const []) (gen 4)
=
("a", 1) : ("b", 2) : ("c", 3) : []
=
("a", 1) : ("b", 2) : ("c", 3) : []
=
("a", 1) : ("b", 2) : [("c", 3)]
=
("a", 1) : [("b", 2), ("c", 3)]
=
[("a", 1), ("b", 2), ("c", 3)]


--- ii) Orden de evaluación Aplicativo:

misteriosa "abc" (gen 1)
=
misteriosa "abc" (1 : gen 2)
=
misteriosa "abc" (1 : 2 : gen 3)
=
misteriosa "abc" (1 : 2 : 3 : gen 4)
=
misteriosa "abc" (1 : 2 : 3 : 4 : gen 5)
=
.
.
.
Evaluacion recursiva infinita de gen. 
------------------------------------------------------

-- 5.b) Considere el siguiente tipo de datos que representa árboles binarios con información en las ramas:

data Arbol a = Hoja | Rama a (Arbol a) (Arbol a)

{-
Construya una función foldA (junto con su firma) que permita reducir un valor de
tipo (Arbol a) a algún tipo b (de forma análoga a foldr). Su implementación debe
poder tratar con estructuras potencialmente infinitas.
-}


--Su función debe cumplir con la siguiente firma:
foldA :: (a -> b -> b -> b) -> b -> Arbol a -> b

------------------ RESPUESTA 5.b ------------------

foldA :: (a -> b -> b -> b) -> b -> Arbol a -> b
foldA _ i Hoja = i 
foldA f i (Rama value left right) = f value (foldA f i left) (foldA f i right)

------------------------------------------------------

-- 5.c) Considere una versión de la función what que funciona sobre árboles (aplica la función proporcionada a ambos sub–árboles) y llamésmola what tree function:

whatTF :: a
    -> (Arbol b -> Arbol (a, b))
    -> (Arbol b -> Arbol (a, b))
    -> Arbol b
    -> Arbol (a, b)
whatTF _ _ _  Hoja          = Hoja
whatTF x f g (Rama y i d)   = Rama (x, y) (f i) (g d)

--Usando su función foldA definimos la función sospechosa:

sospechosa :: ???
sospechosa = foldA whatTF (const Hoja)

--Definimos también la siguiente función, que genera un árbol de números enteros a partir de un cierto valor inicial:

genA :: Int -> Arbol Int
genA n = Rama n (genA (n + 1)) (genA (n * 2))

--Finalmente, definimos el valor arbolito como una instancia de Arbol Char:

arbolito :: Arbol Char
arbolito = Rama 'a' (Rama 'b' Hoja (Rama 'c' Hoja Hoja)) Hoja

--Muestre la evaluación, paso a paso, de la expresión sospechosa arbolito (genA 1), considerando que:
--i. El lenguaje tiene orden de evaluación normal.
--ii. El lenguaje tiene orden de evaluación aplicativo.

------------------ RESPUESTA 5.c ------------------

--- i) Orden de evaluación Normal:

sospechosa arbolito (genA 1)
=
foldA whatTF (const Hoja) arbolito (genA 1)
=
foldA whatTF (const Hoja) (Rama 'a' 
                                (Rama 'b' 
                                       Hoja 
                                       (Rama 'c' Hoja Hoja)
                                ) 
                                Hoja
                          ) (genA 1)
=
whatTF 'a' (foldA whatTF (const Hoja) (Rama 'b'
                                             Hoja
                                             (Rama 'c' 
                                                    Hoja 
                                                    Hoja
                                             )
                                       )
            ) 
            (foldA whatTF (const Hoja) Hoja) 
            (genA 1)
= -- Evaluamos (genA 1)
--      x  
whatTF 'a' (foldA whatTF (const Hoja) (Rama 'b'                     --  \
                                            Hoja                    --   \
                                            (Rama 'c' Hoja Hoja)    --    f
                                      )                             --   /
           )                                                        --  /
           (foldA whatTF (const Hoja) Hoja)                         ------ g
           (Rama 1                                                  ------ Rama y
                (genA (1 + 1))                                      ------ i
                (genA (1 * 2))                                      ------ d
           )
= -- Evaluamos whatTF 'a' f g (Rama y i d) ----- quedando:
{--
Rama ( x , y)
--}
Rama ('a', 1) 
     ((foldA whatTF (const Hoja) (Rama 'b'                          --  \
                                        Hoja                        --   \
                                        (Rama 'c' Hoja Hoja)        --    f
                                 )                                  --   /
      )                                                             --  /
      (genA (1 + 1))                                                ----- i
     ) 
     ((foldA whatTF (const Hoja) Hoja)                              ----- g
      (genA (1 * 2))                                                ----- d
     )
= -- Evaluamos foldA de más arriba
Rama ('a', 1) 
     (whatTF 'b' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (genA (1 + 1))) 
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
= -- Evaluamos (genA (1+1))

--            x  |--------- f ------------------| |--------------------- g ----------------------| (Rama y 
Rama ('a', 1) 
     (whatTF 'b' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (Rama 2 
                                                                                                         (genA (2 + 1))     ----i
                                                                                                         (genA (2 * 2))     ----d
                                                                                                   )
     )                                                                                           
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
-- Evaluamos whatTF 'b' ---:
Rama ('a', 1) 
     (Rama ('b', 2)
           ((foldA whatTF (const Hoja) Hoja)                (genA (2 + 1)))
           (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)  (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos foldA de más arriba

Rama ('a', 1) 
     (Rama ('b', 2)
           ((const Hoja) (genA (2 + 1)))
           (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)  (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos (const Hoja) (genA (2 + 1))

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja
           (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)  (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos foldA de más arriba

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja
           (whatTF 'c' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) Hoja) (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos (genA (2 * 2))

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja --  x  |--------- f ------------------| |------------ g ---------------| (Rama y 
           (whatTF 'c' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) Hoja) (Rama 4
                                                                                               (genA(4+1))      ----i
                                                                                               (genA(4*2))      ----d
                                                                                          ) 
           )
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos whatTF 'c' ....

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                ((foldA whatTF (const Hoja) Hoja) (genA(4+1)))
                ((foldA whatTF (const Hoja) Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos foldA de más arriba

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                ((const Hoja) (genA(4+1)))
                ((foldA whatTF (const Hoja) Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= --- Evaluamos (const Hoja) (genA(4+1))

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                ((foldA whatTF (const Hoja) Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos foldA de más arriba

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                ((const Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= --- Evaluamos (const Hoja) (genA(4*2))

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                Hoja
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos foldA de más arriba

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                Hoja
     )
     ((const Hoja) (genA (1 * 2)))

= -- Evaluamos (const Hoja) (genA (1 * 2))

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                Hoja
     )
     Hoja

--- ii) Orden de evaluación Aplicativo:


sospechosa arbolito (genA 1)
=
sospechosa arbolito Rama 1 
                         (genA (2)) 
                         (genA (2))
=
sospechosa arbolito Rama 1 
                         (Rama 2 (genA (3)) (genA (4))) 
                         (genA (2))
=
sospechosa arbolito Rama 1 
                         (Rama 2 (genA (3)) (genA (4))) 
                         (Rama 2 (genA (3)) (genA (4))) 
=
sospechosa arbolito Rama 1 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
=
sospechosa arbolito Rama 1 
                         (Rama 2 
                               (Rama 3 (genA (4)) (genA (6))) 
                               (genA (4))
                         ) 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
=
sospechosa arbolito Rama 1 
                         (Rama 2 
                               (Rama 3 (genA (4)) (genA (6))) 
                               (Rama 3 (genA (4)) (genA (6))) 
                         ) 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
.
.
.
Evaluacion recursiva infinita de genA. 
