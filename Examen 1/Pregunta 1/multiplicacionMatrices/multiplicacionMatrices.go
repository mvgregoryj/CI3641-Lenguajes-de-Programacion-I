package main

import "fmt"

func main() {
	var A [10][10]int
	var B [10][10]int
	var C [10][10]int

	var N, M, P, i, j, k, temp int

	temp = 0

	fmt.Print("N : ")
	fmt.Scanln(&N)
	fmt.Print("M : ")
	fmt.Scanln(&M)
	fmt.Print("P : ")
	fmt.Scanln(&P)

	fmt.Println("Introduzca los elementos de la matriz A: ")
	for i = 0; i < N; i++ {
		for k = 0; k < M; k++ {
			fmt.Scan(&A[i][k])
		}
	}

	fmt.Println("Introduzca los elementos de la matriz B: ")
	for k = 0; k < M; k++ {
		for j = 0; j < P; j++ {
			fmt.Scan(&B[k][j])
		}
	}

	for i = 0; i < N; i++ {
		for j = 0; j < P; j++ {
			for k = 0; k < M; k++ {
				temp = temp + A[i][k]*B[k][j]
			}
			C[i][j] = temp
			temp = 0
		}
	}

	fmt.Println("Matriz C: ")
	for i = 0; i < N; i++ {
		for j = 0; j < P; j++ {
			fmt.Print(C[i][j], "\t")
		}
		fmt.Print("\n")
	}
}
