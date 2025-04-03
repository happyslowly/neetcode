# @leet start
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        count = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            count += 1
        return count


# @leet end
