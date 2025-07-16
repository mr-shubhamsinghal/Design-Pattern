class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # from ipdb import set_trace; set_trace()
        i = 0
        j = 0
        first_occurence = False
        first_occurence_index = -1
        while i < len(needle) and j < len(haystack):
            if needle[i] == haystack[j]:
                i += 1
                if not first_occurence:
                    first_occurence = True
                    first_occurence_index = j
            else:
                first_occurence = False
                i = 0
            j += 1
        
        if first_occurence and needle[i-1] == haystack[j-1]:
            print(first_occurence)
            return first_occurence_index
        return -1
    
s = Solution()
haystack = "leetcode"
needle = "leeto"

print(s.strStr(haystack, needle))