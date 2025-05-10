# Input : A = {1, 2, 3, 4, 5}
# Output : [48]
#          [20, 28] 
#          [8, 12, 16] 
#          [3, 5, 7, 9] 
#          [1, 2, 3, 4, 5] 

# Explanation :
# Here,   [48]
#         [20, 28] -->(20 + 28 = 48)
#         [8, 12, 16] -->(8 + 12 = 20, 12 + 16 = 28)
#         [3, 5, 7, 9] -->(3 + 5 = 8, 5 + 7 = 12, 7 + 9 = 16)
#         [1, 2, 3, 4, 5] -->(1 + 2 = 3, 2 + 3 = 5, 3 + 4 = 7, 4 + 5 = 9)

def sum_of_triangle(arr):
    def triangle(arr):
        if len(arr) == 1:
            print(arr)
            return
        new_arr = []
        for i in range(len(arr) - 1):
            new_arr.append(arr[i] + arr[i + 1])
        triangle(new_arr)
        print(arr)
    triangle(arr)


sum_of_triangle([1,2,3,4,5])
        

        