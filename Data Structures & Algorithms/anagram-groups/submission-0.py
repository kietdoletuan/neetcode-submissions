class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = {}

        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            key = tuple(counts)
            if key in output_dict:
                output_dict[key].append(s)
            else:
                output_dict[key] = [s]
        
        output = [v for _, v in output_dict.items()]
        return output