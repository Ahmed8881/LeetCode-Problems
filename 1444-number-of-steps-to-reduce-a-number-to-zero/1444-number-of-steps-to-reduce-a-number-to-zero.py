class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        while num:
            num = num // 2 if num % 2 == 0 else num - 1
            steps += 1
        return steps
