abstract class Coleccion<T>() {

    // Se crea una lista para almacenar los elementos
    val lista: MutableList<T> = mutableListOf<T>()

    abstract fun agregar(elem: T)

    // Funcion eliminar para eliminar elementos de la coleccion:
    fun eliminar(elem: T) {
        if (this.buscar(elem)) {
            lista.remove(elem)
        } else {
            println("El elemento $elem no existe en la coleccion")
        }
    }

    // Funcion buscar para buscar elementos en la coleccion:
    fun buscar(elem: T): Boolean {
        return lista.contains(elem)
    }

    // Funcion imprimir para imprimir los elementos de la coleccion:
    fun imprimir(){
        println(lista.toString())
    }    
    
    // Funcion vacio para indicar si el conjunto esta vacio o no
    fun vacio(){
        if (lista.isEmpty()) {
            println("El conjunto está vacío (no tiene elementos).")
        } else {
            println("El conjunto no está vacio.")
        }
    }
}

class Conjunto<T>() : Coleccion<T>() {
    // Funcion agregar para agregar elementos al conjunto, los elementos no se pueden repetir:
    override fun agregar(elem: T) {
        if (!this.buscar(elem)) {
            lista.add(elem)
        }
    }
}

class Bolsa<T>() : Coleccion<T>() {

    // Funcion agregar para agregar elementos a la bolsa, los elementos se pueden repetir:
    override fun agregar(elem: T) {
        lista.add(elem)
    }
}

fun main() {

    // Conjunto:
    println("\nConjunto1:")
    val miConjunto = Conjunto<String>()
    miConjunto.vacio()
    miConjunto.imprimir()
    miConjunto.agregar("elemento1") 
    miConjunto.imprimir()
    miConjunto.agregar("elemento2") 
    miConjunto.imprimir()
    miConjunto.agregar("elemento3")
    miConjunto.imprimir()
    miConjunto.agregar("elemento3")
    miConjunto.imprimir()
    miConjunto.agregar("elemento3")
    miConjunto.imprimir()
    miConjunto.eliminar("elemento1")
    miConjunto.imprimir()
    miConjunto.eliminar("elemento1")
    miConjunto.imprimir()
    miConjunto.eliminar("elemento3")
    miConjunto.imprimir()
    miConjunto.vacio()

    println("\nConjunto2:")
    val miConjunto2 = Conjunto<Int>()
    miConjunto2.vacio()
    miConjunto2.imprimir()
    miConjunto2.agregar(1) 
    miConjunto2.imprimir()
    miConjunto2.agregar(2)
    miConjunto2.imprimir()
    miConjunto2.agregar(2)
    miConjunto2.imprimir()
    miConjunto2.eliminar(2)
    miConjunto2.imprimir()
    miConjunto2.eliminar(2)
    miConjunto2.imprimir()
    miConjunto2.vacio()

    // Bolsa:
    println("\nBolsa1:")
    val miBolsa = Bolsa<String>()
    miBolsa.vacio()
    miBolsa.imprimir()
    miBolsa.agregar("elemento1") 
    miBolsa.imprimir()
    miBolsa.agregar("elemento2") 
    miBolsa.imprimir()
    miBolsa.agregar("elemento3")
    miBolsa.imprimir()
    miBolsa.agregar("elemento3")
    miBolsa.imprimir()
    miBolsa.agregar("elemento3")
    miBolsa.imprimir()
    miBolsa.eliminar("elemento1")
    miBolsa.imprimir()
    miBolsa.eliminar("elemento1")
    miBolsa.imprimir()
    miBolsa.eliminar("elemento3")
    miBolsa.imprimir()
    miBolsa.vacio()

    println("\nBolsa2:")
    val miBolsa2 = Bolsa<Int>()
    miBolsa2.vacio()
    miBolsa2.imprimir()
    miBolsa2.agregar(1) 
    miBolsa2.imprimir()
    miBolsa2.agregar(2)
    miBolsa2.imprimir()
    miBolsa2.agregar(2)
    miBolsa2.imprimir()
    miBolsa2.eliminar(2)
    miBolsa2.imprimir()
    miBolsa2.eliminar(2)
    miBolsa2.imprimir()
    miBolsa2.vacio()
}
