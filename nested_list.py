# 1️⃣ Matrix Row-wise Sum

### 📝 Question:

Take a 2D list (matrix) and print the sum of each row.

### ✅ Answer:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    print("Row Sum:", sum(row))
```

---

# 2️⃣ Column-wise Sum

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]

for col in range(len(matrix[0])):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][col]
    print("Column Sum:", total)
```

---

# 3️⃣ Diagonal Sum (Primary)

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]

total = 0
for i in range(len(matrix)):
    total += matrix[i][i]

print("Primary Diagonal Sum:", total)
```

---

# 4️⃣ Secondary Diagonal Sum

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)
total = 0
for i in range(n):
    total += matrix[i][n-i-1]

print("Secondary Diagonal Sum:", total)
```

---

# 5️⃣ Matrix Multiplication (2x2)

```python
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

result = [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]

print("Result:", result)
```

---

# 6️⃣ Count Even & Odd in Matrix

```python
matrix = [[1,2,3],[4,5,6]]

even = 0
odd = 0

for row in matrix:
    for num in row:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

print("Even:", even, "Odd:", odd)
```

---

# 7️⃣ Find Maximum Element in Matrix

```python
matrix = [[10,20],[5,50],[30,40]]

max_val = matrix[0][0]

for row in matrix:
    for num in row:
        if num > max_val:
            max_val = num

print("Maximum:", max_val)
```

---

# 8️⃣ Transpose of Matrix

```python
matrix = [[1,2,3],[4,5,6]]

transpose = []

for col in range(len(matrix[0])):
    new_row = []
    for row in range(len(matrix)):
        new_row.append(matrix[row][col])
    transpose.append(new_row)

print("Transpose:", transpose)
```

---

# 9️⃣ Check Identity Matrix

```python
matrix = [[1,0,0],[0,1,0],[0,0,1]]

is_identity = True

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j and matrix[i][j] != 1:
            is_identity = False
        elif i != j and matrix[i][j] != 0:
            is_identity = False

print("Identity Matrix:", is_identity)
```

---

# 🔟 Saddle Point (Hard Logic)

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matrix)):
    row_min = min(matrix[i])
    col_index = matrix[i].index(row_min)

    is_saddle = True
    for k in range(len(matrix)):
        if matrix[k][col_index] > row_min:
            is_saddle = False

    if is_saddle:
        print("Saddle Point:", row_min)
```

---

# 1️⃣1️⃣ Count Prime Numbers in Matrix

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

matrix = [[2,4,5],[7,8,9]]

count = 0

for row in matrix:
    for num in row:
        if is_prime(num):
            count += 1

print("Prime Count:", count)
```

---

# 1️⃣2️⃣ Flatten Matrix and Find Median

```python
matrix = [[1,3,5],[2,6,9]]

flat = []

for row in matrix:
    for num in row:
        flat.append(num)

flat.sort()
n = len(flat)

if n % 2 == 0:
    median = (flat[n//2 -1] + flat[n//2]) / 2
else:
    median = flat[n//2]

print("Median:", median)
```

---

# 1️⃣3️⃣ Rotate Matrix 90° Clockwise

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)
rotated = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated[j][n-i-1] = matrix[i][j]

print("Rotated Matrix:", rotated)
```

---

# 1️⃣4️⃣ Matrix Determinant (2x2)

```python
matrix = [[a,b],[c,d]]

det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

print("Determinant:", det)
```

---

# 1️⃣5️⃣ Find Row with Maximum Sum

```python
matrix = [[1,2,3],[10,5,1],[4,4,4]]

max_sum = 0

for row in matrix:
    if sum(row) > max_sum:
        max_sum = sum(row)

print("Max Row Sum:", max_sum)
```

---

# 1️⃣6️⃣ Check Symmetric Matrix

```python
matrix = [[1,2,3],[2,5,6],[3,6,9]]

is_symmetric = True

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False

print("Symmetric:", is_symmetric)
```

---

# 1️⃣7️⃣ Multiply Each Row by Its Index

```python
matrix = [[1,2],[3,4],[5,6]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] *= i

print(matrix)
```

---

# 1️⃣8️⃣ Count Elements Greater Than Row Average

```python
matrix = [[1,5,3],[7,2,9]]

count = 0

for row in matrix:
    avg = sum(row)/len(row)
    for num in row:
        if num > avg:
            count += 1

print("Count:", count)
```

---

# 1️⃣9️⃣ Replace Diagonal with 0

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matrix)):
    matrix[i][i] = 0

print(matrix)
```

---

# 2️⃣0️⃣ Check Magic Square

```python
matrix = [[8,1,6],[3,5,7],[4,9,2]]

target = sum(matrix[0])
magic = True

# Check rows
for row in matrix:
    if sum(row) != target:
        magic = False

# Check columns
for col in range(len(matrix)):
    col_sum = 0
    for row in range(len(matrix)):
        col_sum += matrix[row][col]
    if col_sum != target:
        magic = False

# Check diagonals
diag1 = sum(matrix[i][i] for i in range(len(matrix)))
diag2 = sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix)))

if diag1 != target or diag2 != target:
    magic = False

print("Magic Square:", magic)
```


