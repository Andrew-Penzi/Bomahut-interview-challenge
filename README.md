# Bomahut-interview-challenge
# Bomahut-interview-challenge 

# a) Write an algorithm that given an M X N  matrix return all numbers that are the maximum value in its row but the minimum in its column


# For example if given the matrix
# Input:matrix = [[5,16,20],[9,11,18],[15,16,17]]
# Output:[17]
# Explanation:17 is the only number since it is the maximum in its row and the minimum in its column.


# Input:matrix = [[100,60,20, 50],
                  [70,80,10,90],
                  [10,50,44,30]]
# Output:[50]
# Explanation:50 is the only number since it is the maximum in its row and the minimum in its column.
# Constraints:
# ● m == mat.length
# ● n == mat[i].length
# ● 1 <= n, m <= 50
# ● 1 <= matrix[i][j] <= 105.
# ● All elements in the matrix are distinct.

# b) What is the space and time complexity of your solution?
The time complexity of the find_max_min_numbers function is O(M * N^2), where M is the number of rows in the matrix and N is the number of columns. This is because we loop through each row in the matrix and for each row, we loop through each element in the row and then loop through each row again to find the minimum value in the column. Finding the maximum value in the row takes O(N) time, and finding the minimum value in the column takes O(M) time, so the overall time complexity is O(M * N^2).

The space complexity of the function is O(M + N), because we create two sets to store the indices of the maximum value rows and minimum value columns, respectively. The maximum number of elements in each set is min(M, N), so the overall space complexity is O(M + N).

# c) Write 1-2 tests that you run to validate your answer.