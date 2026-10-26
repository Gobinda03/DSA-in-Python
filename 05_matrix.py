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
            if top <= buttom:
                for i in range (right, left-1, -1):
                    res.append(arr[buttom][i])
                buttom -= 1
            if left <= right:
                for i in range (buttom, top-1, -1):
                    res.append(arr[i][left])
                left += 1
        return res

    # Rotate by 90 degree
    def rotate_matrix(self, mat):
        n = len(mat)

        for i in range(n):
            mat[i].reverse()

        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        return mat

    # Search in a Row-Column Sorted
    def mat_search(self, mat, x):
        row = len(mat)
        col = len(mat[0])
        i = 0
        j = col - 1
        
        while i < row and j >= 0:
            if x > mat[i][j]:
                i += 1
            elif x < mat[i][j]:
                j -= 1
            else:
                return True
        return False

if __name__=="__main__":
    n = int(input("Enter the row number: "))
    print("Input Array:")
    arr = [list(map(int, input().split())) for _ in range (n)]
    sol = Solution()


    # spiral matrix
    # print(sol.spiral_matrix(arr))

    # Rotate by 90 degree
    # print(sol.rotate_matrix(arr))

    # Search in a Row-Column Sorted
    target = int(input("Target: "))
    print(sol.mat_search(arr, target))