// go_cheatsheet_iterating_string_manipulations.go
package main

import (
	"fmt"
	"regexp"
	"strings"
)

// -----------------------------
// Iteration Patterns
// -----------------------------

// 1. Iterating over a slice using range
func iterateSlice(slice []int) {
	for index, value := range slice {
		fmt.Printf("Index: %d, Value: %d\n", index, value)
	}
}

// 2. Transforming a slice (e.g., squaring numbers)
func squareNumbers(numbers []int) []int {
	squares := make([]int, len(numbers))
	for i, n := range numbers {
		squares[i] = n * n
	}
	return squares
}

// 3. Iterating over a map's key-value pairs
func iterateMap(m map[string]int) {
	for key, value := range m {
		fmt.Printf("Key: %s, Value: %d\n", key, value)
	}
}

// 4. Iterating over two slices in parallel
func iterateZip(slice1, slice2 []string) {
	minLen := len(slice1)
	if len(slice2) < minLen {
		minLen = len(slice2)
	}
	for i := 0; i < minLen; i++ {
		fmt.Printf("Slice1: %s, Slice2: %s\n", slice1[i], slice2[i])
	}
}

// 5. Iterating with a while-like loop (using for with a condition)
func iterateWhile(limit int) {
	count := 0
	for count < limit {
		fmt.Printf("Count: %d\n", count)
		count++
	}
}

// -----------------------------
// String Manipulation Patterns
// -----------------------------

// 6. Reversing a string (handling multi-byte characters)
func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

// 7. Splitting a string into parts and joining with a different delimiter
func splitAndJoin(s, delimiter string) ([]string, string) {
	parts := strings.Split(s, delimiter)
	joined := strings.Join(parts, "-")
	return parts, joined
}

// 8. Changing the case of a string
func changeCase(s string) map[string]string {
	return map[string]string{
		"upper": strings.ToUpper(s),
		"lower": strings.ToLower(s),
	}
}

// 9. Replacing substrings within a string
func replaceSubstring(s, old, new string) string {
	return strings.ReplaceAll(s, old, new)
}

// 10. Trimming leading and trailing whitespace
func stripWhitespace(s string) string {
	return strings.TrimSpace(s)
}

// 11. Finding a substring within a string
func findSubstring(s, substr string) int {
	return strings.Index(s, substr)
}

// 12. Using regular expressions to find all matches of a pattern in a string
func regexFind(pattern, s string) []string {
	re := regexp.MustCompile(pattern)
	return re.FindAllString(s, -1)
}

// 13. Iterating over each line in a multi-line string
func iterateLines(multiline string) {
	lines := strings.Split(multiline, "\n")
	for _, line := range lines {
		fmt.Println(line)
	}
}

// 14. Iterating over words in a sentence
func iterateWords(sentence string) {
	words := strings.Fields(sentence)
	for _, word := range words {
		fmt.Println(word)
	}
}

// -----------------------------
// Main Function with Example Usage
// -----------------------------

func main() {
	// Iteration examples
	fmt.Println("Iterating over slice:")
	iterateSlice([]int{10, 20, 30, 40, 50})

	fmt.Println("\nSquaring numbers:")
	squares := squareNumbers([]int{1, 2, 3, 4, 5})
	fmt.Println(squares)

	fmt.Println("\nIterating over map:")
	iterateMap(map[string]int{"apple": 3, "banana": 5, "cherry": 2})

	fmt.Println("\nIterating over two slices in parallel:")
	iterateZip([]string{"one", "two", "three"}, []string{"uno", "dos", "tres"})

	fmt.Println("\nIterating with a while-like loop:")
	iterateWhile(5)

	// String manipulation examples
	s := "Hello, World!"
	fmt.Println("\nOriginal string:", s)

	fmt.Println("\nReversed string:")
	fmt.Println(reverseString(s))

	fmt.Println("\nSplitting and joining string:")
	parts, joined := splitAndJoin("Go is awesome", " ")
	fmt.Println("Parts:", parts)
	fmt.Println("Joined:", joined)

	fmt.Println("\nChanging case:")
	cases := changeCase(s)
	fmt.Println("Upper:", cases["upper"])
	fmt.Println("Lower:", cases["lower"])

	fmt.Println("\nReplacing substring:")
	fmt.Println(replaceSubstring(s, "World", "Gopher"))

	fmt.Println("\nStripping whitespace:")
	fmt.Printf("'%s'\n", stripWhitespace("   Lots of space   "))

	fmt.Println("\nFinding substring:")
	fmt.Printf("Position of 'World' in '%s': %d\n", s, findSubstring(s, "World"))

	fmt.Println("\nRegex find (all 5-letter words):")
	regexResult := regexFind(`\b\w{5}\b`, "Hello there, these words: apple, world, and peace.")
	fmt.Println(regexResult)

	fmt.Println("\nIterating over lines in a multi-line string:")
	multiline := "Line one\nLine two\nLine three"
	iterateLines(multiline)

	fmt.Println("\nIterating over words in a sentence:")
	iterateWords("Iterate through each word in this sentence.")
}

