package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func miniMaxSum(arr []int32) {
	minValue := arr[0]

	for _, num := range arr {
		if num < minValue {
			minValue = num
		}
	}

	maxValue := arr[0]

	for _, num := range arr {
		if num > maxValue {
			maxValue = num
		}
	}

	var sum int64 = 0

	for _, num := range arr {
		sum += int64(num)
	}

	minResult := sum - int64(maxValue)
	maxResult := sum - int64(minValue)

	fmt.Println(minResult, maxResult)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var arr []int32

	for i := 0; i < 5; i++ {
		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
		checkError(err)
		arrItem := int32(arrItemTemp)
		arr = append(arr, arrItem)
	}

	miniMaxSum(arr)
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
