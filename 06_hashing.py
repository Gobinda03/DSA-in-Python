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
    
    # Intersection of Two arrays with Duplicate Elements
    def intersect(self, arr1, arr2):
        s = set(arr1)
        ans = []

        for num in arr2:
            if num in s:
                ans.append(num)
                s.pop()
        return ans
    
    # Union of Arrays with Duplicates
    def union(self, arr1, arr2):
        s = set(arr1)
        for num in arr2:
            if num not in s:
                s.add(num)
        return s


if __name__ == "__main__":
    sol = Solution()
    print("Enter Array: ")
    arr = list(map(int, input().split()))

    # Two Sum - Pair with Given Sum
    # target = int(input("Target: "))
    # print(sol.twoSum(arr, target))

    # Count Pairs with Sum
    # target = int(input("Target: "))
    # print(sol.countPairs(arr, target))

    # Intersection of Two arrays with Duplicate Elements
    # arr2 = list(map(int, input().split()))
    # print(sol.intersect(arr, arr2))

    # Union of Arrays with Duplicates
    # arr2 = list(map(int, input().split()))
    # print(sol.union(arr, arr2))