def solution(word):
    answer = 0
    dic = {"A":0, "E":1, "I":2, "O":3, "U":4}
    
    for i in range(len(word)):
        for j in range(4, i, -1):
            answer += 5** (j-i) *dic[word[i]]
        answer += 1 + dic[word[i]]
    
    return answer