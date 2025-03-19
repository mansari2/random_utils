package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("My favorite number is", rand.Intn(10))
	fmt.Println("My second favorite number is", rand.Intn(10))
}

// to run this program, use the command `go run playground.go`
// to build the program, use the command `go build playground.go`