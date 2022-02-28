package main

import "fmt"

func potenciacion(a int, b int) int {

	var resultado int

	if b == 0 {
		resultado = 1
	} else if b > 0 {
		resultado = a * potenciacion(a, b-1)
	}

	return resultado
}

func main() {
	var a int
	var b int

	fmt.Print("a : ")
	fmt.Scanln(&a)
	fmt.Print("b : ")
	fmt.Scanln(&b)

	if b >= 0 {
		resultado := potenciacion(a, b)
		fmt.Printf("%d^%d = %d", a, b, resultado)
		fmt.Println("")
	} else {
		fmt.Println("Por favor introduzca un valor de b mayor o igual a 0")
		main()
	}

}
