# 1️⃣ Longest Substring Without Repeating Characters

### 📝 Question:

Find the length of the longest substring without repeating characters.

### ✅ Answer:

```python
s = input("Enter string: ")

max_len = 0
start = 0
used = {}

for i in range(len(s)):
    if s[i] in used and used[s[i]] >= start:
        start = used[s[i]] + 1
    used[s[i]] = i
    max_len = max(max_len, i - start + 1)

print("Longest Length:", max_len)
```

---

# 2️⃣ Check if Two Strings Are Anagrams

```python
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
```

---

# 3️⃣ First Non-Repeating Character

```python
s = input("Enter string: ")

for ch in s:
    if s.count(ch) == 1:
        print("First Non-Repeating:", ch)
        break
```

---

# 4️⃣ Count Vowels, Consonants, Digits, Special Characters

```python
s = input("Enter string: ")

vowels = consonants = digits = special = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special:", special)
```

---

# 5️⃣ Remove All Duplicate Characters

```python
s = input("Enter string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Without Duplicates:", result)
```

---

# 6️⃣ Longest Palindromic Substring (Brute Force)

```python
s = input("Enter string: ")

longest = ""

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        temp = s[i:j]
        if temp == temp[::-1] and len(temp) > len(longest):
            longest = temp

print("Longest Palindrome:", longest)
```

---

# 7️⃣ Compress String (aaabb → a3b2)

```python
s = input("Enter string: ")

compressed = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        compressed += s[i-1] + str(count)
        count = 1

compressed += s[-1] + str(count)

print("Compressed:", compressed)
```

---

# 8️⃣ Check Rotated String

```python
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s2 in (s1 + s1):
    print("Rotation of each other")
else:
    print("Not rotation")
```

---

# 9️⃣ Find All Substrings

```python
s = input("Enter string: ")

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])
```

---

# 🔟 Reverse Words in Sentence

```python
s = input("Enter sentence: ")

words = s.split()
reversed_sentence = " ".join(words[::-1])

print("Reversed Sentence:", reversed_sentence)
```

---

# 1️⃣1️⃣ Check Pangram

```python
import string

s = input("Enter sentence: ").lower()

if set(string.ascii_lowercase).issubset(set(s)):
    print("Pangram")
else:
    print("Not Pangram")
```

---

# 1️⃣2️⃣ Find Most Frequent Character

```python
s = input("Enter string: ")

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

max_char = max(freq, key=freq.get)

print("Most Frequent:", max_char)
```

---

# 1️⃣3️⃣ Count Palindromic Words in Sentence

```python
s = input("Enter sentence: ")

words = s.split()
count = 0

for word in words:
    if word == word[::-1]:
        count += 1

print("Palindrome Words Count:", count)
```

---

# 1️⃣4️⃣ Remove Adjacent Duplicates (Stack Logic)

```python
s = input("Enter string: ")

stack = []

for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)

print("Result:", "".join(stack))
```

---

# 1️⃣5️⃣ Find Smallest Window Containing All Characters

```python
from collections import Counter

s = input("Enter main string: ")
t = input("Enter target string: ")

need = Counter(t)
have = {}
left = 0
min_len = float('inf')
result = ""

for right in range(len(s)):
    have[s[right]] = have.get(s[right], 0) + 1

    while all(have.get(c,0) >= need[c] for c in need):
        if right - left + 1 < min_len:
            min_len = right - left + 1
            result = s[left:right+1]

        have[s[left]] -= 1
        left += 1

print("Smallest Window:", result)
```

---

# 1️⃣6️⃣ Check Balanced Parentheses

```python
s = input("Enter parentheses string: ")

stack = []
pairs = {')':'(', '}':'{', ']':'['}

for ch in s:
    if ch in "({[":
        stack.append(ch)
    elif ch in ")}]":
        if not stack or stack[-1] != pairs[ch]:
            print("Not Balanced")
            break
        stack.pop()
else:
    print("Balanced" if not stack else "Not Balanced")
```

---

# 1️⃣7️⃣ Find Longest Common Prefix

```python
strs = input("Enter words separated by space: ").split()

prefix = strs[0]

for word in strs[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Longest Common Prefix:", prefix)
```

---

# 1️⃣8️⃣ Multiply Large Numbers as Strings

```python
num1 = input("Enter number1: ")
num2 = input("Enter number2: ")

print("Product:", str(int(num1) * int(num2)))
```

---

# 1️⃣9️⃣ Check if String Contains Only Unique Characters

```python
s = input("Enter string: ")

if len(set(s)) == len(s):
    print("All characters unique")
else:
    print("Duplicates present")
```

---

# 2️⃣0️⃣ Find All Permutations of String

```python
from itertools import permutations

s = input("Enter string: ")

for p in permutations(s):
    print("".join(p))
```


