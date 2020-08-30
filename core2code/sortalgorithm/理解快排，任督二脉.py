"""
经典top k 问题 ： 找到无序数组进行排序，找出 其中排名第k的元素
 通常解法：选择排序算法  时间复杂度o(n^2)
 更快的解法： 快速排序法
 优化 快速选择算法

 快排核心： 找到基准值
    step1:选择一个值作为基准值
    step2:将小于基准值的元素放在基准值元素的左边， 将大于基准值的元素放在基准值的右边  —— partition 分割操作
            ——空出一个位置！反复的前后调换元素： 当我们选择了基准值有以后， 原先基准值的位置就相当于被空出来了！！
    step3：对基准值的两侧，递归的进行step1,step2

"""

from eliot import start_action, to_file

to_file(open("quick_sort.log", "w"))


class QuickSort:

    def quick_sort(self, l: list, left: int, right: int):
        if left <= right:
            position = self.partition(l, left, right)
            # 左边
            self.quick_sort(l, left, position - 1)
            # 右边
            self.quick_sort(l, position + 1, right)

    def partition(self, l: list, left: int, right: int) -> int:
        # 选择基准元素
        target = l[right]
        index = left
        for i in range(left, right):
            if l[i] <= target:
                l[index], l[i] = l[i], l[index]
                index += 1
        l[index], l[right] = l[right], l[index]
        return index

    def topK(self, l: list, k: int):
        pass


if __name__ == '__main__':
    l = [8, 3, 10, 2, 7, 6, 9, 12]
    s = QuickSort()
    with start_action(action_type="quickSort", l=l):
        s.quick_sort(l=l, left=0, right=len(l) - 1)
    print(l)
