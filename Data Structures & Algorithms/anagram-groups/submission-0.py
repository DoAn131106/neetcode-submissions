class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            hash_map[key].append(i)
        return list(hash_map.values())