class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            log_list = log.split(' ')
            if log_list[1].isalpha():
                letter_logs.append(log_list)
            else:
                # digit logs append the sting.
                digit_logs.append(log)
        # sort the letter log
        sort_letter_log = sorted(letter_logs, key=lambda x: (x[1:], x[0]))
        sort_letter_log = [' '.join(i) for i in sort_letter_log]
        sort_letter_log.extend(digit_logs)

        return sort_letter_log