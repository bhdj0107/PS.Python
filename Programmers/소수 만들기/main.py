from math import sqrt
def solution(nums):
    answer = 0
    
    def isPrime(num):
        if num == 1: return False
        elif num == 2: return True
        else:
            sq = int(sqrt(num))
            for i in range(2, sq+1):
                if num % i == 0: return False
            return True
        
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                answer += int(isPrime(nums[i] + nums[j] + nums[k]))

    return answer