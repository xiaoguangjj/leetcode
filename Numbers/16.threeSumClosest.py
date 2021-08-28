"""
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 思路：双指针法
class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        res = 3000
        # 1.排除特殊情况，当nums为空或者长度小于3时
        if  nums is None or len(nums) < 3:
            return res
        # 2.对nums进行从小到大排序
        nums.sort()
        # 3.当全为0时，0即是最为接近的 无论等不等于target
        if (len(set(nums)) == 1 and nums[0]==0):
            return nums[0]
        # 4.当不为0，可全部都为同一个数字时，判断此数字三个相加是否等于target
        # 若不等于，则return 三个同一数字的和
        if (len(set(nums)) == 1 and nums[0] != 0):
            if sum(nums[:3]) == target:
                return target
            else:
                return sum(nums[:3])
        if len(nums) == 3:
            return sum(nums)
        #去除重复的数字项，设置左右两个双指针
        for i in range(n):
            if nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = n - 1
        # 循环进行三个数相加，找出其中绝对值最小的值，赋给res进行返回
        # 注：此处的res在前面设置过，要选择一个较大的数才行，此处我设置的res = 3000
            while L < R:
                t = nums[i]+nums[L]+nums[R]
                if t == target:
                    return target
                if (abs(t-target)<(abs(res-target))):
                    res = t
        # 小于0 偏小指针右移，偏大指针左移
                if (t-target<0):
                    L = L + 1
                else:
                    R = R - 1
        return  res


if __name__=="__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    s = Solution()
    print(s.threeSumClosest(nums,target))
