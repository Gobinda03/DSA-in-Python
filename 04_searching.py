class Solution:
    # No of occurance TC = O(log N) + O(log N)
    def first_occurance(self, arr, target):
        left, right = 0, len(arr)-1
        idx = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                idx = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return idx
    def last_occurance(self, arr, target):
        left, right = 0, len(arr)-1
        idx = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                idx = mid
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return idx
    def count_freq(self, arr, target):
        if not arr or arr[0] > target or target > arr[-1]:
            return 0
        first = self.first_occurance(arr, target)
        if first == -1:
            return 0
        last = self.last_occurance(arr, target)
        
        return last - first + 1

    # minimum element within a rotated sorted array
    def find_min(self, arr):
        low , high = 0, len(arr)-1
        
        while low < high:
            if arr[low] < arr[high]:
                return arr[low]
            mid = (low+high)//2
            if arr[high] < arr[mid]:
                low = mid + 1
            else:
                high = mid
        return arr[low]

    # Search in rotated sorted array
    def search_in_rotated_sorted_array(self, arr, key):
        n = len(arr)
        low, high = 0, n-1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                return mid
            
            if arr[mid] >= arr[low]:
                if key < arr[mid] and key >= arr[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if key <= arr[high] and key > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

    # find the peak element
    def peak_element(self, arr):
        n = len(arr)
        
        # if the array has only one element then that would be peak
        if n == 1:
            return 0
        # if first element is the greater than next one, that is peak
        if arr[0] > arr[1]:
            return 0
        # if last element is the greater than the prev, that is the peak
        if arr[n-1] > arr[n-2]:
            return n-1
        
        low, high = 1, n-2
        while low <= high:
            mid = ( low + high ) // 2
            
            # check whether the mid element is peak or not
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            
            # if mid element is lesser than prev then there is a chance of being the peak on right
            if arr[mid] < arr[mid+1]:
                low = mid + 1
            else:
                high = mid - 1

    # k-th element of two sorted array
    def kth_element(self, a, b, k):
        n, m = len(a), len(b)
        # binary search on smaller array
        if n > m:
            return self.kthElement(b, a, k)
            
        low = max(0, k - m)
        high = min(k, n)
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = k - mid1
            
            l1 = l2 = float('-inf')
            r1 = r2 = float('inf')
            
            if mid1 < n:
                r1 = a[mid1]
            if mid2 < m:
                r2 = b[mid2]
            if (mid1 - 1) >= 0:
                l1 = a[mid1 - 1]
            if (mid2 - 1) >= 0:
                l2 = b[mid2 - 1]
                
            # check if valid parition or not
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            # too many element taken from left
            elif l1 > r2:
                high = mid1 - 1
            # too less element taken from left
            else:
                low = mid1 +  1
        return -1

    # Aggressive cow
    def can_placed(self, arr, k , dist):
        cnt = 1
        prev = arr[0]
        
        for i in range (1, len(arr)):
            if arr[i] - prev >= dist:
                cnt += 1
                prev = arr[i]
                
        return cnt >= k
    def aggressive_cows(self, arr, k):
        arr.sort()
        ans = 0
        
        # minimun dist can be 1 and maximun can be the highest pos - lowest pos
        low, high = 1, arr[-1] - arr[0]
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.can_placed(arr, k, mid):
                ans = mid
                # if mid is possible then lesser than mid is also possible 
                # no need to check as we need max value
                low = mid + 1
            else:
                # if mid is'nt possible then all greater than mid not possible
                # no need to check them
                high = mid - 1
        return ans


if __name__=="__main__":
    print("Input Array:")
    arr = list(map(int, input().split()))
    sol = Solution()

    # No of occurance in a sorted array
    # target = int(input("Target: "))
    # print(sol.count_freq(arr, target))

    # Minimum element with a given rotated sorted array
    # print(sol.find_min(arr))

    # Search in rotated sorted array
    # key = int(input("Key: "))
    # print(sol.search_in_rotated_sorted_array(arr, key))

    # find the peak element
    # print(sol.peak_element(arr))

    # k-th element of the two sorted
    # print("Another Array:")
    # arr2 = list(map(int, input().split()))
    # k = int(input("Enter value of k: "))
    # print(sol.kth_element(arr, arr2, k))

    # Aggressive cows
    # cows = int(input("No of cows: "))
    # print(sol.aggressive_cows(arr, cows))