package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

func plusMinus(arr []int32) {
    var positive []int32
    var negative []int32
    var zero []int32
    
    for _, num := range arr {
        if num < 0 {
            negative = append(negative, num)
        } else if num > 0 {
            positive = append(positive, num)
        } else {
            zero = append(zero, num)
    }}
    
    positive_ratio := float64(float64(len(positive)) / float64(len(arr)))    
    negative_ratio := float64(float64(len(negative)) / float64(len(arr)))
    zero_ratio := float64(float64(len(zero)) / float64(len(arr)))
    
    fmt.Printf("%.6f\n", positive_ratio)
    fmt.Printf("%.6f\n", negative_ratio)
    fmt.Printf("%.6f\n", zero_ratio)
    
    }

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    n := int32(nTemp)

    arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var arr []int32

    for i := 0; i < int(n); i++ {
        arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
        checkError(err)
        arrItem := int32(arrItemTemp)
        arr = append(arr, arrItem)
    }

    plusMinus(arr)
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
