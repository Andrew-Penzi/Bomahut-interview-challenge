def find_max_min_numbers(matrix):
    max_rows = set()
    min_cols = set()
    result = 0

    # Find maximum value in each row
    for i in range(len(matrix)):
        max_val = max(matrix[i])
        max_rows.add(i)
        for j in range(len(matrix[i])):
            # Check if element is the maximum in the row
            if matrix[i][j] == max_val:
                # Check if element is also the minimum in the column
                if j not in min_cols and matrix[i][j] == min([matrix[k][j] for k in range(len(matrix))]):
                    result = (matrix[i][j])
                    min_cols.add(j)

    return result

matrix_1 = [[5,16,20],
         [9,11,18],
         [15,16,17]]
matrix_2 = [[100,60,20, 50],
                  [70,80,10,90],
                  [10,50,44,30]]


if __name__ == "__main__":
    res = find_max_min_numbers(matrix_1)
    print(res)