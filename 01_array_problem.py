class Solution:
    def second_largest(self, arr):
        largest = slargest = -1
        for item in arr:
            if item > largest:
                slargest = largest # largest became the second largest
                largest = item # new largest
            elif item > slargest and item != slargest: 
                slargest = item # find soething which is greater than seacond largest and not the largest
        return slargest

    def move_zero_to_end(self, arr):
        zero = 0
        # Have to iterate the array and found out the non zero number then swap with the zero, pointed by the zero pointer
        for item in arr:
            if item != 0:
                item, arr[zero] = arr[zero], item
                zero += 1
        return arr

    def reverse_array(self, arr):
        left = 0
        right = len(arr)-1

        while left < right:
            # Swap first and last element then move both
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
        return arr

    def reverse(self, arr, left, right):
        while left < right:
            # Swap first and last element then move both
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
        return arr
    def rotate_array(self, arr, pos):
        pos = pos % len(arr)
        self.reverse(arr, 0, pos-1)
        self.reverse(arr, pos, len(arr)-1)
        self.reverse(arr, 0 , len(arr)-1)
        return arr
    
    def next_permutation(self, arr):
        n = len(arr)
        ind = -1
        # find rightmost index of minimum element
        for i in range (n-2, -1, -1):
            if arr[i] < arr[i+1]:
                ind = i
                break
        # Find the rightmost element greater than arr[ind]
        if ind != -1:
            for i in range (n-1, ind, -1):
                if arr[i] > arr[ind]:
                    arr[ind], arr[i] = arr[i], arr[ind]
                    break
        arr[ind+1:] = arr[ind+1:][::-1]
        return arr

    def stock_buy_sell(self, arr):
        min_price = float('inf')
        max_profit = 0

        for price in arr:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price-min_price)
        return max_profit

    def stock_buy_sell_multiple_trans(self, arr):
        total = 0

        for i in range (1, len(arr)):
            if arr[i] > arr[i-1]:
                total += (arr[i]-arr[i-1])
        return total

    def majority_element(self, arr):
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        # finding the candidate value by checking all item
        for item in arr:
            if item == candidate1:
                count1 += 1
            elif item == candidate2:
                count2 += 1 
            elif count1 == 0:
                candidate1 = item
                count1 = 1
            elif count2 == 0:
                candidate2 = item
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        ans = []
        # validating the answer
        if arr.count(candidate1) > len(arr)//3:
            ans.append(candidate1)
        if arr.count(candidate2) > len(arr)//3:
            ans.append(candidate2)
        return ans

    def get_min_diff(self, arr, k):
        n = len(arr)
        if n <= 1:
            return 0
        arr.sort()
        ans = arr[-1] - arr[0]
        for i in range (1, n):
            if arr[i] - k < 0:
                continue
            small = min(arr[0]+k, arr[i]-k)
            big = max(arr[-1]-k, arr[i-1]+k)

            ans = min(ans, big-small)
        return ans

    def kadane_algo(self, arr):
        max_so_far = float('-inf')
        curr_max = 0
        start = end = 0

        for i in range (len(arr)):
            curr_max += arr[i]

            if curr_max > max_so_far:
                max_so_far = curr_max
                end = i
            if curr_max < 0:
                curr_max = 0
                start = i+1
        return arr[start:end+1]

    def max_product(self, arr):
        n = len(arr)
        result = float('-inf')
        pre = suff = 1
        for i in range(n):
            if pre == 0:
                pre = 1
            pre *= arr[i]

            if suff == 0:
                suff = 1
            suff *= arr[n-1-i]

            result = max(result, max(pre, suff))
        return result

    def max_circular_sub(self, arr):
        total = sum(arr)

        curr_max = max_so_far = arr[0]
        curr_min = min_so_far = arr[0]

        for i in range (len(arr)):
            curr_max = max(curr_max, curr_max+arr[i])
            max_so_far = max(max_so_far, curr_max)

            curr_min = min(curr_min, curr_min+arr[i])
            min_so_far = min(min_so_far, curr_min)

        if max_so_far < 0:
            return max_so_far
        circular_sum = total-min_so_far
        return max(max_so_far, circular_sum)

    def missing_number(self, arr):
        n = len(arr)
        for i in range (n):
            while 1 <= arr[i] <= n:
                correct = arr[i]-1
                if arr[i] == arr[correct]:
                    break
                arr[i], arr[correct] = arr[correct], arr[i]
        for i in range (n):
            if arr[i] != i + 1:
                return i+1
        return n+1
     
if __name__ == "__main__":
    n = int(input("Enter the length of the array: "))
    arr = list(map(int, input().split()))
    sol = Solution()

    # Second largest element of the array
    # print(sol.second_largest(arr))

    # Move zero to the end
    # print(sol.move_zero_to_end(arr))

    # Reverse the array
    # print(sol.reverse_array(arr))

    # Rotate the given array
    # pos = int(input("Enter the postition from which u want to rorate: "))
    # print(sol.rotate_array(arr, pos))

    # Next Permutation
    # print(sol.next_permutation(arr))

    # Stock buy and sell
    # print(sol.stock_buy_sell(arr))

    # Stock buyt and sell multiple transaction allowed
    # print(sol.stock_buy_sell_multiple_trans(arr))

    # Majority element(n/3)
    # print(sol.majority_element(arr))

    # Get the minimum height of the tower
    # k = int(input("Enter the value of k: "))
    # print(sol.get_min_diff(arr, k))

    # Kadane's Algorithm
    # print(sol.kadane_algo(arr))

    # Maximum products subbarray
    # print(sol.max_product(arr))

    #  Maximum circular subarray
    # print(sol.max_circular_sum(arr))

    # find the missing integer
    # print(sol.missing_number(arr))