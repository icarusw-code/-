from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    now = 0 
    stack = deque([0 for _ in range(bridge_length)])
    
    while len(truck_weights) or now > 0:
        removedTruck = stack.popleft()
        now -= removedTruck
        
        if len(truck_weights) and now + truck_weights[0] <= weight:
            newTruck = truck_weights.popleft()
            now += newTruck
            stack.append(newTruck)
        
        else:
            stack.append(0)
            
        answer += 1

    return answer