package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
)

type Point struct {
	x int
	y int
}

type Humanoid struct {
	lifePoints int
	pos        Point
}

func main() {
	theMapRead, err := ioutil.ReadFile("baby.txt")

	if err != nil {
		fmt.Print(err)
	}

	theMap := make([][]byte, len(theMapRead)/bytes.IndexByte(theMapRead, byte('\n')))
	for i := range theMap {
		theMap[i] = make([]byte, len(theMapRead)/len(theMap))
	}
	var counter int = 0
	for l := range theMap {
		for c := range theMap[l] {
			theMap[l][c] = theMapRead[counter]
			counter = counter + 1
		}
	}
	fmt.Println(theMap)

	// theElves := make([]Humanoid, 0)
	// theGoblins := make([]Humanoid, 0)

	str := string(theMapRead) // convert content to a 'string'

	fmt.Println(str) // print the content as a 'string'
}
