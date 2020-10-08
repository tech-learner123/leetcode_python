class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_number, fn_type, time = log.split(':')
            # convert the string to int
            fn_number, time = int(fn_number), int(time)
            if fn_type == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fn_number)
                # Started at the beginning of the timestamp
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                # ended at the end of the timestamp
                prev_time = time + 1
        return ans