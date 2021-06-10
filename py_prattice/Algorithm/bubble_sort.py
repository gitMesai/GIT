import time

'''
############冒泡算法实现###########
算法思想：
    它的基本思想是对所有相邻记录的关键字值进行比效，如果是逆顺（a[j]>a[j+1]），则将其交换，最终达到有
    序化;
 
    对于需要从小到大（从大到小的数组）进行排序：从第一个位置开始，两两比较相邻的元素大小，如果前者比后者大（从大到小排序前者比后者小），那么两者交换位置，以此类推
时间复杂度：
    bubble_sort : (n-1)+(n-2)+...+1=o(n^2)
    bubble_sort2 优化后：当传入的序列本身是有序的，则在第一次循环后发现，此时时间复杂度是o(n)
空间复杂度：
    冒泡算法空间复杂度取决于序列规模，o(n)
'''

def bubble_sort(nums):
    '''
    冒泡算法核心函数
    输入：nums,无序列表
    输出，从小到大的有序列表
    '''
    # range(8)  : 0 -7 (因为最后一次可以不用比较，所以需要 减1)
    for i in range(len(nums)-1):
        # 每次循环比较后，最大的值放到最后，所以每次都可以比上次少比较一次
        for j in range(len(nums) -1 - i ):
            if nums[j] > nums[j+1]:
                nums[j+1],nums[j] = nums[j],nums[j+1]
    return nums

def bubble_sort2(nums):
    '''
    冒泡算法核心函数
    输入：nums,无序列表
    输出，从小到大的有序列表
    优化后：当传入的序列本身是有序的，则在第一次循环后发现，此时时间复杂度是o(n)
    '''
    # 优化部分 ： 添加标记位
    swapped = False
    # range(8)  : 0 -7 (因为最后一次可以不用比较，所以需要 减1)
    for i in range(len(nums)-1):
        # 每次循环比较后，最大的值放到最后，所以每次都可以比上次少比较一次
        for j in range(len(nums) -1 - i ):
            if nums[j] > nums[j+1]:
                nums[j+1],nums[j] = nums[j],nums[j+1]

                # 优化部分 ：如果第一次循环后有进行过交换位置操作，则改变标记位状态
                swapped =True
        # 优化部分 ：当标记位状态改变后，则代表是无序列表
        if not swapped:
            break
    return nums

if __name__ == '__main__':
    inpurt_data = [8, 7, 12, 3, 2, 11, 10, 6]
    now = time.time()
    output_data = bubble_sort(inpurt_data)
    print(time.time() - now)
    print(output_data)