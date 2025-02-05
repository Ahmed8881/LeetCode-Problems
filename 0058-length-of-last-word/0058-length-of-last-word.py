class Solution(object):
    def lengthOfLastWord(self, s):
        last_word = s.split()[-1]
        return len(last_word)



        