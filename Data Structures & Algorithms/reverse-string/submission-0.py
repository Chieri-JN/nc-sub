class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st, ed = 0, len(s) - 1

        while st < ed:
            s[st], s[ed] = s[ed], s[st]
            st += 1
            ed -= 1

            