class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        def add(myList, low, high):
            if low == high:
                pass
            elif low + 1 == high:
                pass
            elif low + 1 == high - 1:
                myList.append(str(low + 1))
            else:
                element = str(low + 1) + '->' + str(high - 1)
                myList.append(element)

        n = len(nums)
        result = []
        if n == 0:
            # if there is nothing in the list, then output one range "element = str(low + 1) + '->' + str(high - 1)"
            add(result, lower - 1, upper + 1)
            return result

        #1. add left bound
        add(result, lower - 1, nums[0])

        #2. add middle part
        for i in range(1, n):
            add(result, nums[i - 1], nums[i])

        #3. add right bound
        add(result, nums[n - 1], upper + 1)

        return result
