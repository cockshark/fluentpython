package quick_sort

import (
	"math/rand"
	"testing"
)

func createRandomArr(length int) arr []int {
    arr := make([]int, length, length)
    for i := 0; i<length; i++ {
        arr := rand.Intn(100)
    }
    return arr
}

func TestQuickSort(t *testing.T){
    arr :=[]int{5, 4}
    Quick_sort(arr)
    t.Log(arr)

    arr = createRandomArr(100)
    Quick_sort(arr)
    t.Log(arr)
}