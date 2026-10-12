class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # my solution:
        # first condition is that the lenght must be equal
        """
        if (len(s) != len(t)):
            return  False

        s_ordered = "".join(sorted(s))
        t_ordered = "".join(sorted(t))

        if s_ordered == t_ordered:
            return True
        else:
            return False
        """
        # better solution...
        if (len(s) != len(t)):
            return  False

        counter = {}

        for c_s, c_t in zip(s, t):
            counter[c_s] = counter.get(c_s, 0) + 1
            counter[c_t] = counter.get(c_t, 0) - 1
        
        return all(val == 0 for val in counter.values())
