import sys
class Solution:
    def security_msg(self, msg):
        n = len(msg)
        flips = 0
        for i in range(0, n, 2):
            if msg[i] != msg[i+1]:
                flips += 1
        return flips 

    def min_moves(self, str):
        freq = {}

        for ch in str:
            freq[ch] = freq.get(ch, 0) + 1

        cnt = 0
        for moves in freq.values():
            cnt += moves // 2

        return cnt 

    def stock_cost(self, arr, d):
        cnt = 0
        for i in range (len(arr)-2):
            for j in range (i + 1, len(arr)-1):
                for k in range (j + 1, len(arr)):
                    sum = arr[i] + arr[j] + arr[k]

                    if sum % d == 0:
                        cnt += 1
        return cnt

    def fizzbuzz(self, n):
        for i in range(1, n+1):
            if i % 15 == 0:
                print('FizzBuzz')
            elif i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
            else:
                print(i)
        
    def pig_latin(self, str):
        ans = ''
        consonant = ''
        vowel = ['a', 'e', 'i', 'o', 'u']
        i = 0
        if str[0] in vowel:
            return str + '-yay'
        else:
            while str[i] not in vowel:
                consonant+=str[i]
                i += 1
        return str[i:] + '-' +consonant + 'ay'

    def validate_license_plate(self, plate):
        plate = plate.upper()
        ans = []
        if not plate.isalnum() and not 2 <= len(plate) <= 10:
            return 'INVALID'
        if not any (ch.isdigit() for ch in plate):
            return 'INVALID'

        i = 0
        while i < len(plate):
            ans.append(plate[i : i+3])
            i += 3
        return '-'.join(ans)

    def sortRequests(self, requests):
        resources = []
        for url in requests:
            parts = url.split('/')
            names = []
            for part in parts:
                if part.startswith('resource'):
                    names.append(part)
            resources.append('/'.join(names))
        resources.sort(key = lambda x: (x.count('/')+1, x))
        return resources

    def sum_numbers(self, str):
        total = 0
        curr = 0
        for ch in str:
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            else:
                total += curr
                curr = 0
        return total + curr

    def second_largest(self, arr):
        large = float('-inf')
        slarge = large

        for num in arr:
            if num > large:
                slarge = large
                large = num
            if num > slarge and num != large:
                slarge = num

        return -1 if slarge == float('-inf') else slarge

    def non_repeat(self, str):
        mp = [0]*26

        for ch in str:
            mp[ord(ch) - ord('a')] += 1
        for ch in str:
            if mp[ord(ch) - ord('a')] == 1:
                return ch
        return -1

    def longest_sub(self, str):
        freq = {}
        cnt = 0
        n = len(str)
        left = 0
        for i in range (n):
            freq[str[i]] = freq.get(str[i], 0) + 1

            while freq[str[i]] > 1:
                freq[str[left]] -= 1
                left += 1

            cnt = max(cnt, i-left+1)
        return cnt

    def sub_with_sum_k(self, arr, k):
        freq = {}
        freq[0] = 1
        curr_sum = 0
        cnt = 0
        for num in arr:
            curr_sum += num
            need = curr_sum - k

            if need in freq:
                cnt += freq[need]
            freq[curr_sum] = freq.get(curr_sum, 0)+1
        return cnt

    def longest_consecutive(self, arr):
        st = set(arr)
        max_occur = 0
        
        for num in arr:
            if (num - 1) not in st:
                cnt = 1
                curr = num

                while curr + 1 in st:
                    curr += 1
                    cnt += 1

                max_occur = max(max_occur, cnt)
        return max_occur

    def move_zero(self, arr):
        z = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[z] = arr[z], arr[i]
                z += 1

        return arr

    def max_sum(self, arr, k):
        n = len(arr)
        new_sum = sum(arr[:k])
        maxi = new_sum

        for i in range (k, n):
            new_sum += arr[i]
            new_sum -= arr[i-k]

            maxi = max(new_sum, maxi)
        return maxi

    def move_negative(self, arr):
        n = len(arr)
        negative = 0

        for i in range (n):
            if arr[i] < 0:
                arr[i], arr[negative] = arr[negative], arr[i]
                negative += 1
        return arr

    def remove_dup(self, arr):
        cnt = 1
        for i in range (1, len(arr)):
            if arr[i] == arr[i-1]:
                continue
            else:
                cnt += 1
        return cnt

    def missing_num(self, arr):
        total = sum(arr)
        n = len(arr)
        missing = ((n+1) * n // 2) - total

        if missing == 0:
            return len(arr)
        else:
            return missing

    def two_sum(self, arr, k):
        seen = {}

        for i in range(len(arr)):
            complement = k - arr[i]

            if complement in seen:
                return [seen[complement], i]
            seen[arr[i]] = i

        return [-1, -1]

    def count_pair(self, arr, target):
        seen = {}
        cnt = 0

        for i in range (len(arr)):
            complement = target - arr[i]

            if complement in seen:
                cnt += seen[complement]
            seen[arr[i]] = seen.get(arr[i], 0)+1
        return cnt
    
    def sort_zero_one_two(self, arr):
        low, mid = 0, 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr

    def majority_el(self, arr):
        major = arr[0]
        cnt = 0

        for i in range (1, len(arr)):
            if cnt == 0:
                major = arr[i]

            if arr[i] == major:
                cnt += 1
            else:
                cnt -= 1
        c = 0
        for num in arr:
            if num == major:
                c += 1

        if c > (len(arr))//2:
            return major
        else:
            return -1

    def stock_buy_sell(self, arr):
        price = float('inf')
        profit = 0

        for i in range (len(arr)):
            if arr[i] < price:
                price = arr[i]
            else:
                profit = max(profit, arr[i]-price)
        return profit

    def max_sub_sum(self, arr):
        max_so_far = arr[0]
        maxi = arr[0]

        for i in range(1, len(arr)):
            maxi += arr[i]

            if maxi < 0:
                maxi = 0
            max_so_far = max(max_so_far, maxi)
        return max_so_far


    def Alphabet_Wheel_Decryption(self, str, k):
        ans = ''
        for ch in str:
            new = (ord(ch) - ord('A') - k) % 26
            ans += chr(new + ord('A'))
        return ans


    def arriving_packets(self, arr):
        res = 0
        carry = 0

        for num in arr:
            total = num + carry
            power = 1 << ((total.bit_length) - 1)
            carry = total - power
            res = max(res, power)
        return res

    def countIncreasingSegments(self, ycor, k):
        n = len(ycor)

        if k == 1:
            return n
        run = 1
        cnt = 0
        for i in range (1, n):
            if ycor[i] > ycor[i-1]:
                run += 1
            else:
                run = 1

            if run >= k:
                cnt += 1
        return cnt

    def anagram_half(self, str):
        n = len(str)
        mp1 = [0] * 10
        mp2 = [0] * 10
        half = n//2
        for i in range(half):
            mp1[int(str[i])] += 1
            mp2[int(str[i+half])] += 1

        cnt = 0
        for i in range(10):
            if mp1[i] > mp2[i]:
                cnt += mp1[i] - mp2[i]
        return cnt

    def mars_rover(self, mat, commands):
        row = col = 0

        for c in commands:
            if c == 'UP':
                if row > 0:
                    row -= 1
            elif c == 'DOWN':
                if row < mat-1:
                    row += 1
            

if __name__ == "__main__":
    sol = Solution()
    # msg = sys.stdin.readline()
    # msg = input("Enter the msg: ")
    # print(msg)
    # print(sol.security_msg(msg))

    # str = input("Enter the String: ")
    # print(sol.min_moves(str))

    # arr = list(map(int, input().split()))
    # d = int(input())
    # print(sol.stock_cost(arr, d))

    # n = int(input("Enter range: "))
    # sol.fizzbuzz(n)

    # str = input("Enter: ")
    # print(sol.pig_latin(str))

    # plate = input("Enter: ")
    # print(sol.validate_license_plate(plate))

    # requests = [
    # "https://api.example.com/resource2/id/resource3/id2",
    # "https://api.example.com/resource3/",
    # "https://api.example.com/resource2/id",
    # "https://api.example.com/resource1/id/resource3/id2"
    # ]
    # print(sol.sortRequests(requests))
    # str = "ab12cd003ef5x20"
    # print(sol.sum_numbers(str))

    # arr = [4, 4, 4, 4]
    # print(sol.second_largest(arr))

    # str = "aabbcddee"
    # print(sol.non_repeat(str))

    # arr = list(map(int, input().split()))
    # k = int(input())
    # print(sol.sub_with_sum_k(arr, k))

    # arr = list(map(int, input().split()))
    # print(sol.longest_consecutive(arr))

    # arr = list(map(int, input().split()))
    # print(sol.move_zero(arr))


    arr = [2, 0, 2, 1, 1, 0]
    print(sol.sort_zero_one_two(arr))