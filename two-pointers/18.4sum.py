# @leet start
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        results = []
        for a in range(len(nums) - 3):
            if a > 0 and nums[a - 1] == nums[a]:
                continue
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b - 1] == nums[b]:
                    continue
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total == target:
                        results.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c + 1] == nums[c]:
                            c += 1
                        while c < d and nums[d - 1] == nums[d]:
                            d -= 1
                        c += 1
                        d -= 1
                    elif total > target:
                        d -= 1
                    else:
                        c += 1
        return results


# @leet end
