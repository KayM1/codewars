// go  un test.go

package main

import "fmt"

func main() {
	// main automatically runs everything in it
	messagesFromDoris := []string{
		"You doing anything later??",
		"Did you get my last message?",
		"Don't leave me hanging...",
		"Please respond I'm lonely!",
	}
	numMessages := float64(len(messagesFromDoris))
	costPerMessage := .02

	// don't touch above this line

	totalCost := costPerMessage * numMessages

	// don't touch below this line

	fmt.Printf("Doris spent %.2f on text messages today\n", totalCost)
	fmt.Println("the compiled textio server is starting")
	hello_wlrd()
}

func hello_wlrd() {
	fmt.Println("hello world")
}
