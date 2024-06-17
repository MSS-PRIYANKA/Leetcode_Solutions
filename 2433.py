def findArray(self, pref: List[int]) -> List[int]:
    res = [pref[0]]
    length = len(pref)
    for i in range(0, length-1):
        res.append(pref[i] ^ pref[i+1])
    return res
