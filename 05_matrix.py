class Solution:

    # spiral matrix
    def spiral_matrix(self, arr):
        left, right = 0, len(arr[0])-1
        top, buttom = 0, len(arr)-1
        res = []
        while left <= right and top <= buttom:
            
            for i in range (left, right+1):
                res.append(arr[top][i])
            top += 1
            for i in range (top, buttom+1, 1):
                res.append(arr[i][right])
            right -= 1
            for i in range (right, left-1, -1):
                res.append(arr[buttom][i])
            buttom -= 1
            for i in range (buttom, top-1, -1):
                res.append(arr[i][left])
            left += 1
        return res



if __name__=="__main__":
    n = int(input("Enter the row number: "))
    print("Input Array:")
    arr = [list(map(int, input().split())) for _ in range (n)]
    sol = Solution()


    # spiral matrix
    print(sol.spiral_matrix(arr))