class Solution:
    def sort_zero_one_two(self, arr):
        n = len(arr)
        if n <= 0:
            return arr
        zero = one = 0
        two = n - 1

        while one <= two:
            if arr[one] == 0:
                arr[zero], arr[one] = arr[one], arr[zero]
                zero += 1
                one += 1
            elif arr[one] == 1:
                one += 1
            else:
                arr[one], arr[two] = arr[two], arr[one]
                two -= 1

        return arr

    def h_index(self, arr):
        n = len(arr)
        freq = [0]*(n+1)

        for el in arr:
            if el > n: 
                freq[n] += 1
            else:
                freq[el] += 1   

        idx = n
        s = freq[n]
        while s < idx:
            idx -= 1
            s += freq[idx]
        return idx


    def count_merge(self, arr, l, mid, r):
        n1 = mid - l + 1
        n2 = r - mid

        left = arr[l:mid + 1]
        right = arr[mid + 1:r + 1]

        res = 0
        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:

            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                res += n1 - i
                j += 1

            k += 1

        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1

        return res

    def count_inv(self, arr, l, r):
        ans = 0

        if l < r:
            mid = l + (r - l) // 2

            ans += self.count_inv(arr, l, mid)
            ans += self.count_inv(arr, mid + 1, r)

            ans += self.count_merge(arr, l, mid, r)

        return ans

    def inversion_count(self, arr):
        return self.count_inv(arr, 0, len(arr) - 1)

    def overlapping_intervals(self, arr):
        arr.sort()
        res = []
        res.append(arr[0])
        for i in range (1, len(arr)):
            end = res[-1]
            curr = arr[i]
            
            if(curr[0] <= end[1]):
                end[1] = max(curr[1], end[1])
            else:
                res.append(arr[i])
        return res
    
    def insert_interval(self, intervals, new_interval):
        intervals.append(new_interval)
        return self.overlapping_intervals(intervals)

    def min_interval_remove(self, intervals):
        intervals.sort(key = lambda x : x[1])
        cnt = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                cnt += 1
            else:
                end = intervals[i][1]   
        return cnt

    def merge_arrays(self, arr1, arr2):
        n, m = len(arr1), len(arr2)
        left, right = n-1, 0
        while left >= 0 and right < m:
            if arr1[left] > arr2[right]:
                arr1[left], arr2[right] = arr2[right], arr1[left]
                left -= 1
                right += 1
            else:
                break
        arr1.sort()
        arr2.sort()


if __name__ == "__main__":
    n = int(input("Enter the length of the array: "))
    arr = list(map(int, input().split()))
    sol = Solution()

    # Sort 0s, 1s and 2s
    # print(sol.sort_zero_one_two(arr))

    # Find H-Index
    # print(sol.h_index(arr))

    # Inversion Count
    # print(sol.inversion_count(arr))

    # Merge overlaping intervals
    # arr = [list(map(int, input().split())) for _ in range (n)]
    # print(sol.overlapping_intervals(arr))

    # Insert new Interval
    # interval = [list(map(int, input().split())) for _ in range (n)]
    # new_interval = list(map(int, input().split()))
    # print(sol.insert_interval(interval, new_interval))

    # non-overlapping intervals
    # interval = [list(map(int, input().split())) for _ in range(n)]
    # print(sol.min_interval_remove(interval))

    # Merge Without Extra Space
    # m = int(input("Enter the length of other array: "))
    # arr2 = list(map(int, input().split))