package main

import "fmt"

var a = 1

func P() {
	a = 3
}

func Q() {
	var a = 2
	fmt.Println("valor de a en la funcion Q, antes de llamar P: \na =", a)
	P()
	fmt.Println("valor de a en la funcion Q, luego de llamar P: \na =", a)
}

func main() {
	Q()

	fmt.Println("valor de a en el main\na =", a)
}
