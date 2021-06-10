import time
from bisect import bisect_right

'''
#########插入算法
算法思想：
    在要排序的一组数中，假定前n-1个数已经排好序，现在将第n个数插到前面的有序数列中，
    使得这n个数也是排好顺序的。
    如此反复循环，直到全部排好顺序
'''

def insertion_sort(nums):
    # 从低二个元素循环到最后一个元素
    for i in range(1,len(nums)):
        # 记住要插入进行比较的元素的值
        t = nums[i]
        # 循环，从上次最后一次循环的元素开始进行比较
        for j in range(i-1,-1,-1):
            # 记住下标
            k = j
            # 当待插入值大于或等于当前值，那么待插入值就在该值的后面位置插入
            if nums[j] <= t:
                # 记住下标，插入这个元素的后面，并结束循环
                k = k+1
                break
            # 当比较的元素小于循环的元素时，将大的元素逐个向后移
            nums[j+1] = nums[j]
        # 将元素标记为元素插入到比它小的那个元素后，此时的k是循环体内的k+1
        nums[k] = t
    return nums

if __name__ == '__main__':
    inpurt_data = [8, 7, 12, 3, 2, 11, 10, 6]
    now = time.time()
    output_data = insertion_sort(inpurt_data)
    print(time.time() - now)
    print(output_data)