class Solution:
    # Two Sum - Pair with Given Sum
    def twoSum(self, arr, target):
        s = set()
        
        for num in arr:
            req = target - num
            
            if req in s:
                return True
            else:
                s.add(num)
        return False

    # Count Pairs with Sum
    def countPairs(self, arr, target):
        cnt = 0
        freq = {}
        
        for num in arr:
            req = target - num
            
            if req in freq:
                cnt += freq[req]
                
            freq[num] = freq.get(num, 0) + 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    print("Enter Array: ")
    arr = list(map(int, input().split()))

    # Two Sum - Pair with Given Sum
    # target = int(input("Target: "))
    # print(sol.twoSum(arr, target))

    # Count Pairs with Sum
    target = int(input("Target: "))
    print(sol.countPairs(arr, target))
