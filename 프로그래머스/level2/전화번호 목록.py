def solution(phone_book):
    
    hashMap = {}
    for i in phone_book:
        hashMap[i] = 1

    for phone_number in phone_book:
        pre = ""
        for number in phone_number:
            pre += number
            if pre in hashMap and pre != phone_number:
                return False
    
    return True