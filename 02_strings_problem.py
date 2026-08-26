class Solution:
    def atoi(self, str):
        n = len(str)
        i = 0
        # Eliminate space
        while i < n and str[i] == ' ':
            i += 1
        # sign
        sign = 1
        if i < n and str[i] == '-':
            sign *= -1
            i += 1
        elif i < n and str[i] == '+':
            i += 1
        # Number
        number = 0
        while i < n and '0' <= str[i] <= '9':
            digit = ord(str[i]) - ord('0')
            number = number * 10 + digit
            i += 1

        return sign*number

    def trim_leading_zeros(self, s):
        # find first one
        find_one = s.find('1')
        return s[find_one:] if find_one != -1 else '0'
    def binary_sum(self, s1, s2):
        # trim leading zeros
        s1 = self.trim_leading_zeros(s1)
        s2 = self.trim_leading_zeros(s2)

        if len(s2) > len(s1):
            return self.binary_sum(s2, s1)
        n = len(s1)
        m = len(s2)
        
        j = m - 1
        carry = 0
        result = []
        for i in range (n-1, -1, -1):
            bit1 = int(s1[i])
            bit_sum = bit1 + carry

            if j >= 0:
                bit2 = int(s2[j])
                bit_sum += bit2
                j -= 1

            bit = bit_sum % 2
            carry = bit_sum // 2
            result.append(str(bit))
        if carry > 0:
            result.append('1')
        return ''.join(result[::-1])

    def check_anagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        freq = [0]*26

        for ch in s1:
            freq[ord(ch) - ord('a')] += 1
        for ch in s2:
            freq[ord(ch) - ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False
        return True

    def non_repeating_char(self, s):
        freq = [0]*26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in s:
            if freq[ord(ch) - ord('a')] == 1:
                return ch
        return '$'
    
if __name__=="__main__":
    str1 = input("Enter the strings: ")
    sol = Solution()

    # Atoi funtion
    # print(sol.atoi(str1))

    # Binary sum
    # str2 = input("Enter another string: ")
    # print(sol.binary_sum(str1, str2))

    # Check Anagrams
    # str2 = input("Enter another string: ")
    # print(sol.check_anagrams(str1, str2))

    # First non-repeating Character
    # print(sol.non_repeating_char(str1))

