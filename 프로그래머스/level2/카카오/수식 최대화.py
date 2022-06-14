from itertools import permutations

def cal(do, seq, exp):
    if exp.isdigit():
        return str(exp)
    else:
        if do[seq] == "*":
            data = exp.split("*")
            tmp = []
            for s in data:
                tmp.append(cal(do, seq+1, s))
            return str(eval("*".join(tmp)))
        
        if do[seq] == "+":
            data = exp.split("+")
            tmp = []
            for s in data:
                tmp.append(cal(do, seq+1, s))
            return str(eval("+".join(tmp)))
    
        if do[seq] == "-":
            data = exp.split("-")
            tmp = []
            for s in data:
                tmp.append(cal(do, seq+1, s))
            return str(eval("-".join(tmp)))
    

def solution(expression):
    answer = 0
    arr = ["*", "+", "-"]
    dos = list(permutations(arr, 3))
    
    for do in dos:
        result = abs(int(cal(do, 0, expression)))

        if result > answer:
            answer = result

    return answer

print(solution("100-200*300-500+20"))