def solution(s, n):
    answer = ''
        
    for i in s:
        if i == " ":
            answer += " "
        if "a" <= i <= "z":
            if ord(i) + n > ord("z"):
                answer += chr(ord(i) + n - 26)
            else: answer += (chr(ord(i) + n))
        if "A" <= i <= "Z":
            if ord(i) + n > ord("Z"):
                answer += chr(ord(i) + n - 26)
            else: answer += (chr(ord(i) + n))
        
    return answer