

# 1️⃣ Sum of All Elements in a Tuple

### 📝 Question:

Find the sum of all numbers in a tuple.

### ✅ Answer:

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

total = 0
for i in nums:
    total += i

print("Sum:", total)
```

---

# 2️⃣ Find Maximum and Minimum in Tuple

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

max_val = nums[0]
min_val = nums[0]

for i in nums:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Max:", max_val)
print("Min:", min_val)
```

---

# 3️⃣ Count Occurrence of an Element

```python
nums = tuple(map(int, input("Enter numbers: ").split()))
search = int(input("Enter element to count: "))

count = 0
for i in nums:
    if i == search:
        count += 1

print("Count:", count)
```

---

# 4️⃣ Remove Duplicates (Convert Back to Tuple)

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

unique = tuple(set(nums))

print("Tuple without duplicates:", unique)
```

---

# 5️⃣ Tuple of Squares

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

squares = tuple(i*i for i in nums)

print("Squares Tuple:", squares)
```

---

# 6️⃣ Nested Tuple Sum

### 📝 Question:

Find total sum of nested tuple like ((1,2),(3,4)).

```python
nested = ((1,2),(3,4))

total = 0
for t in nested:
    for num in t:
        total += num

print("Total Sum:", total)
```

---

# 7️⃣ Check If Tuple is Palindrome

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

if nums == nums[::-1]:
    print("Palindrome Tuple")
else:
    print("Not Palindrome")
```

---

# 8️⃣ Find Second Largest in Tuple

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

temp = list(set(nums))
temp.sort()

print("Second Largest:", temp[-2])
```

---

# 9️⃣ Swap First and Last Element

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

nums = (nums[-1],) + nums[1:-1] + (nums[0],)

print("Updated Tuple:", nums)
```

---

# 🔟 Tuple of Even Numbers Only

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

even = tuple(i for i in nums if i % 2 == 0)

print("Even Tuple:", even)
```

---

# 1️⃣1️⃣ Employee Salary Analysis (Tuple of Tuples)

### 📝 Question:

Find highest salary from employee data.

```python
employees = (("Amit",50000),("Ravi",75000),("Neha",60000))

max_salary = 0
top_employee = ""

for name, salary in employees:
    if salary > max_salary:
        max_salary = salary
        top_employee = name

print("Highest Salary:", max_salary)
print("Employee:", top_employee)
```

---

# 1️⃣2️⃣ Sort Tuple by Second Value

```python
data = (("A",3),("B",1),("C",2))

sorted_data = tuple(sorted(data, key=lambda x: x[1]))

print("Sorted Tuple:", sorted_data)
```

---

# 1️⃣3️⃣ Multiply All Elements in Tuple

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

product = 1
for i in nums:
    product *= i

print("Product:", product)
```

---

# 1️⃣4️⃣ Tuple Matrix Diagonal Sum

```python
matrix = ((1,2,3),(4,5,6),(7,8,9))

total = 0
for i in range(len(matrix)):
    total += matrix[i][i]

print("Primary Diagonal Sum:", total)
```

---

# 1️⃣5️⃣ Find Common Elements Between Two Tuples

```python
t1 = tuple(map(int, input("Enter tuple1: ").split()))
t2 = tuple(map(int, input("Enter tuple2: ").split()))

common = tuple(i for i in t1 if i in t2)

print("Common Elements:", common)
```

---

# 1️⃣6️⃣ Count Prime Numbers in Tuple

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

nums = tuple(map(int, input("Enter numbers: ").split()))

count = 0
for i in nums:
    if is_prime(i):
        count += 1

print("Prime Count:", count)
```

---

# 1️⃣7️⃣ Flatten Nested Tuple

```python
nested = ((1,2),(3,4),(5,6))

flat = ()

for t in nested:
    for num in t:
        flat += (num,)

print("Flattened Tuple:", flat)
```

---

# 1️⃣8️⃣ Frequency Dictionary from Tuple

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

freq = {}

for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency:", freq)
```

---

# 1️⃣9️⃣ Tuple Rotation Left by 2 Positions

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

rotated = nums[2:] + nums[:2]

print("Rotated Tuple:", rotated)
```

---

# 2️⃣0️⃣ Check If All Elements Unique

```python
nums = tuple(map(int, input("Enter numbers: ").split()))

if len(nums) == len(set(nums)):
    print("All elements are unique")
else:
    print("Duplicates found")
```


