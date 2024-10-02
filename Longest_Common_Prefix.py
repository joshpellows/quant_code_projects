from os.path import commonprefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix_len = len(strs[0])
        for i in strs[1: ]:
            prefix_len = min(prefix_len, len(i))
            while not i.startswith(strs[0][ : prefix_len]):
                prefix_len -= 1
        prefix = strs[0][ :prefix_len]
        return prefix

