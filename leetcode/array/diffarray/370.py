class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # convert arr to diff arr. it is the same as diff of 0 and 0 is 0
        diff = [0] * length
        # update record
        for change in updates:
            start = change[0]
            end = change[1]
            val = change[2]
            diff[start] += val
            if end + 1 < length:
                diff[end+1] -= val
        # convert diff arr back to res
        res = [0] * length
        res[0] = diff[0]
        for i in range(1, length):
            res[i] = res[i-1] + diff[i]
        return res