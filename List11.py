

# 1️⃣ E-Commerce Order Analysis

### 📝 Question:

Given a list of order amounts,

* Remove orders below ₹100
* Apply 10% discount on orders above ₹5000
* Print final processed list and total revenue.

### ✅ Answer:

```python
orders = list(map(float, input("Enter order amounts: ").split()))

processed = []
total = 0

for amount in orders:
    if amount >= 100:
        if amount > 5000:
            amount = amount - (amount * 0.10)
        processed.append(amount)
        total += amount

print("Processed Orders:", processed)
print("Total Revenue:", total)
```

---

# 2️⃣ Student Performance Filtering

### 📝 Question:

Given list of marks,

* Remove marks < 35
* Add 5 grace marks to students scoring between 35–40
* Print updated list.

### ✅ Answer:

```python
marks = list(map(int, input("Enter marks: ").split()))

updated = []

for m in marks:
    if m >= 35:
        if 35 <= m <= 40:
            m += 5
        updated.append(m)

print("Updated Marks:", updated)
```

---

# 3️⃣ Inventory Stock Alert System

### 📝 Question:

Given stock quantities list,

* Print items with stock < 10
* Calculate total stock.

### ✅ Answer:

```python
stock = list(map(int, input("Enter stock quantities: ").split()))

low_stock = []
total = 0

for qty in stock:
    if qty < 10:
        low_stock.append(qty)
    total += qty

print("Low Stock Items:", low_stock)
print("Total Stock:", total)
```

---

# 4️⃣ Salary Tax Processing

### 📝 Question:

Given salary list,

* Deduct 10% tax if salary > 50000
* Deduct 5% if salary > 30000
* Print net salaries.

### ✅ Answer:

```python
salaries = list(map(float, input("Enter salaries: ").split()))

net = []

for s in salaries:
    if s > 50000:
        s -= s * 0.10
    elif s > 30000:
        s -= s * 0.05
    net.append(s)

print("Net Salaries:", net)
```

---

# 5️⃣ Fraud Transaction Detection

### 📝 Question:

Given transaction amounts,

* Flag transactions > ₹100000
* Count suspicious transactions.

### ✅ Answer:

```python
transactions = list(map(float, input("Enter transactions: ").split()))

fraud = 0

for t in transactions:
    if t > 100000:
        print("Suspicious Transaction:", t)
        fraud += 1

print("Total Suspicious Transactions:", fraud)
```

---

# 6️⃣ Delivery Time Optimization

### 📝 Question:

Given delivery times in minutes,

* Remove deliveries > 120 mins
* Find average delivery time.

### ✅ Answer:

```python
times = list(map(int, input("Enter delivery times: ").split()))

valid = []
total = 0

for t in times:
    if t <= 120:
        valid.append(t)
        total += t

average = total / len(valid)
print("Valid Deliveries:", valid)
print("Average Time:", average)
```

---

# 7️⃣ Product Price Update

### 📝 Question:

Increase price by 8% if price < 1000
Decrease price by 5% if price > 5000

### ✅ Answer:

```python
prices = list(map(float, input("Enter product prices: ").split()))

updated = []

for p in prices:
    if p < 1000:
        p += p * 0.08
    elif p > 5000:
        p -= p * 0.05
    updated.append(p)

print("Updated Prices:", updated)
```

---

# 8️⃣ Employee Attendance Analysis

### 📝 Question:

Given attendance days list,

* Mark employees with attendance < 20 as "Low Attendance".

### ✅ Answer:

```python
attendance = list(map(int, input("Enter attendance days: ").split()))

for days in attendance:
    if days < 20:
        print(days, "- Low Attendance")
    else:
        print(days, "- Good Attendance")
```

---

# 9️⃣ Bank Balance Minimum Check

### 📝 Question:

Given balances list,

* Add penalty ₹500 if balance < 1000
* Print updated balances.

### ✅ Answer:

```python
balances = list(map(float, input("Enter balances: ").split()))

updated = []

for b in balances:
    if b < 1000:
        b -= 500
    updated.append(b)

print("Updated Balances:", updated)
```

---

# 🔟 Sales Commission Calculation

### 📝 Question:

If sales > ₹1,00,000 → 10% commission
If > ₹50,000 → 5%

### ✅ Answer:

```python
sales = list(map(float, input("Enter sales amounts: ").split()))

for s in sales:
    if s > 100000:
        commission = s * 0.10
    elif s > 50000:
        commission = s * 0.05
    else:
        commission = 0
    print("Sales:", s, "Commission:", commission)
```

---

# 1️⃣1️⃣ Remove Negative Numbers

```python
nums = list(map(int, input("Enter numbers: ").split()))

positive = []

for n in nums:
    if n >= 0:
        positive.append(n)

print("Without Negatives:", positive)
```

---

# 1️⃣2️⃣ Find Top 3 Scores

```python
scores = list(map(int, input("Enter scores: ").split()))

scores.sort(reverse=True)
print("Top 3 Scores:", scores[:3])
```

---

# 1️⃣3️⃣ Merge Two Lists Without Duplicates

```python
list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

merged = list(set(list1 + list2))

print("Merged List:", merged)
```

---

# 1️⃣4️⃣ Detect Consecutive Duplicates

```python
nums = list(map(int, input("Enter numbers: ").split()))

for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        print("Consecutive duplicate found:", nums[i])
```

---

# 1️⃣5️⃣ Rotate List Right by 1 Position

```python
nums = list(map(int, input("Enter numbers: ").split()))

last = nums[-1]
nums = [last] + nums[:-1]

print("Rotated List:", nums)
```


