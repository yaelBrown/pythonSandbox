class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start = intervals[0][0]
        end = intervals[0][1]

        out = []
        cur = 0

        while cur < len(intervals):
            if len(out) == 0 and cur == (len(intervals) - 1):
                out.append([start, intervals[cur][1]])
                continue
            if intervals[cur] == [start, end] and cur is (len(intervals) - 1):
                out.append([start, end])
                cur += 1
                continue
            if intervals[cur] == [start, end]:
                cur += 1
                continue
            if intervals[cur][0] is end or intervals[cur][0] is start:
                end = intervals[cur][1]
                out.append([start, end])
                cur += 1
                continue
            if intervals[cur][0] > end:
                out.append([start, end])
                start = intervals[cur][0]
                end = intervals[cur][1]
            else:
                end = intervals[cur][1]
                cur += 1

        temp = []
        for i in out:
            if i not in temp:
                temp.append(i)
            else:
                continue
        out = temp
        return out

    # https://www.youtube.com/watch?v=44H3cEC2fFM
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nLogn)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else: 
                out.append([start, end])
        return output