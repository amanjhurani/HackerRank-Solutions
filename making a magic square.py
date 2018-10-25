matrix_list = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
              [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
              [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
              [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
              [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
              [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
              [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
              [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]


input_matrix = []
r0 = raw_input()
r0 = r0.split()
input_matrix.append(r0)
r1 = raw_input()
r1 = r1.split()
input_matrix.append(r1)
r2 = raw_input()
r2 = r2.split()
input_matrix.append(r2)

total_cost = []
for ref_matrix in matrix_list:
    diff = 0
    cost = 0
    for i in range(3):
        for j in range(3):
            if input_matrix[i][j] != ref_matrix[i][j]:
                diff = abs(int(input_matrix[i][j]) - int(ref_matrix[i][j]))
                cost += diff
    total_cost.append(cost)
print(min(total_cost))
