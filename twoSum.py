def twoSum(nums, target):
    result = {}
    for i, num in enumerate(nums):
        r = target - num
        if r in result:
            return [result[r], i]
        result[num] = i
    return []

def main():
    testNumbers = [5, 1, 2, 10, 5, 9]
    
    print(f"The answer: {twoSum(testNumbers, 19)}")

main()