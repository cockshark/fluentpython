package  quick_sort

// 给外部引用的方式需要大写
func Quick_sort(arr []int){
    quick_sort(arr, 0, len(arr)-1)
}

func quick_sort(arr []int, start, end int){
    if start >= end {
    return
    }
    index := partition(arr, start, end)
    quick_sort(arr, start, index-1)
    quick_sort(arr, index+1 ,end)
}

func partition(arr int[], start, end int) int {
    pivot = arr[end]
    var i = start
    for j:=start;j<end;j++{
        if arr[j] < pivot {
            if !(i==j){
            //交换位置
               arr[i], arr[j] = arr[j], arr[i]
            }
            i++
        }
    }
    arr[i], arr[end] = arr[end], arr[i]
    return i
}