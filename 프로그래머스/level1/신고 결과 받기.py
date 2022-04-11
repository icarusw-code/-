from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    
    user_report = defaultdict(set)
    num_report = defaultdict(int)
    warning = []
    
    for r in report:
        from_report, to_report = r.split()
        
        num_report[to_report] += 1
        user_report[from_report].add(to_report)
    
        if num_report[to_report] == k:
            warning.append(to_report)
    
    for w in warning:
        for i in range(len(id_list)):
            if w in user_report[id_list[i]]:
                answer[i] += 1
    
    return answer