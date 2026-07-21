class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict={}
        for s in strs:
            sort_s = tuple(sorted(s))
            if sort_s in anagram_dict:
                anagram_dict[sort_s].append(s)
            else:
                anagram_dict[sort_s] = [s]

        out = []
        for key in anagram_dict:
            out.append(anagram_dict[key])
        return out    