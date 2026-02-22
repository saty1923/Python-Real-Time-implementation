

# 1️⃣ Deep Reverse All Strings in Nested Structure

### 📝 Question:

Reverse every string at any depth inside nested list.

### ✅ Answer:

```python
data = [["hello", ["world"]], ["python", ["AI", ["code"]]]]

def deep_reverse(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(deep_reverse(item))
        else:
            result.append(item[::-1])
    return result

print(deep_reverse(data))
```

---

# 2️⃣ Count Total Vowels Recursively

```python
data = [["hello", ["world"]], ["AI"]]

def count_vowels(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_vowels(item)
        else:
            for ch in item.lower():
                if ch in "aeiou":
                    count += 1
    return count

print(count_vowels(data))
```

---

# 3️⃣ Find Deepest Level String

```python
data = [["a", ["bb"]], [["ccc", ["dddd"]]]]

def deepest_string(lst, level=0):
    max_word = ""
    max_level = -1
    for item in lst:
        if isinstance(item, list):
            word, lvl = deepest_string(item, level+1)
            if lvl > max_level:
                max_word, max_level = word, lvl
        else:
            if level > max_level:
                max_word, max_level = item, level
    return max_word, max_level

print(deepest_string(data))
```

---

# 4️⃣ Flatten Nested and Sort by Length

```python
data = [["apple", ["kiwi"]], ["banana"]]

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)
    return result

flat = flatten(data)
flat.sort(key=len)

print(flat)
```

---

# 5️⃣ Validate Nested Email Strings

```python
data = [["test@gmail.com"], ["invalid@", ["user@yahoo.com"]]]

def validate(lst):
    valid = []
    for item in lst:
        if isinstance(item, list):
            valid += validate(item)
        else:
            if "@" in item and "." in item:
                valid.append(item)
    return valid

print(validate(data))
```

---

# 6️⃣ Replace All Numeric Strings with Their Squares

```python
data = [["12", ["5"]], ["abc", "7"]]

def process(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(process(item))
        else:
            if item.isdigit():
                result.append(str(int(item)**2))
            else:
                result.append(item)
    return result

print(process(data))
```

---

# 7️⃣ Decode Nested Pattern "3[a2[b]]"

```python
def decode(s):
    stack = []
    current = ""
    num = 0

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((current, num))
            current = ""
            num = 0
        elif ch == "]":
            prev, repeat = stack.pop()
            current = prev + current * repeat
        else:
            current += ch
    return current

print(decode("3[a2[b]]"))
```

---

# 8️⃣ Count Words with Only Unique Characters

```python
data = [["abc", ["hello"]], ["xyz"]]

def count_unique(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_unique(item)
        else:
            if len(set(item)) == len(item):
                count += 1
    return count

print(count_unique(data))
```

---

# 9️⃣ Extract All Palindromes Deeply

```python
data = [["madam", ["hello"]], ["level"]]

def find_palindrome(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result += find_palindrome(item)
        else:
            if item == item[::-1]:
                result.append(item)
    return result

print(find_palindrome(data))
```

---

# 🔟 Deep Longest Word Finder

```python
data = [["hi"], ["python", ["artificial", "AI"]]]

def longest(lst):
    max_word = ""
    for item in lst:
        if isinstance(item, list):
            word = longest(item)
            if len(word) > len(max_word):
                max_word = word
        else:
            if len(item) > len(max_word):
                max_word = item
    return max_word

print(longest(data))
```

---

# 1️⃣1️⃣ Convert All Strings to Uppercase Deeply

```python
data = [["hello"], ["world", ["python"]]]

def upper_all(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(upper_all(item))
        else:
            result.append(item.upper())
    return result

print(upper_all(data))
```

---

# 1️⃣2️⃣ Count Total Characters Ignoring Spaces

```python
data = [["hello world"], ["AI"]]

def count_chars(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_chars(item)
        else:
            count += len(item.replace(" ", ""))
    return count

print(count_chars(data))
```

---

# 1️⃣3️⃣ Remove Words Shorter Than 3 Deeply

```python
data = [["hi", ["python"]], ["AI", "code"]]

def remove_short(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(remove_short(item))
        else:
            if len(item) >= 3:
                result.append(item)
    return result

print(remove_short(data))
```

---

# 1️⃣4️⃣ Count Occurrence of Specific Character

```python
data = [["apple"], ["banana", ["grape"]]]

def count_char(lst, ch):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_char(item, ch)
        else:
            count += item.count(ch)
    return count

print(count_char(data, "a"))
```

---

# 1️⃣5️⃣ Detect Nested Duplicate Words

```python
data = [["apple"], ["banana", ["apple"]]]

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)
    return result

flat = flatten(data)

duplicates = set([x for x in flat if flat.count(x) > 1])

print("Duplicates:", duplicates)
```

---

# 1️⃣6️⃣ Build Frequency Dictionary Deeply

```python
data = [["abc"], ["de", ["abc"]]]

def build_freq(lst, freq={}):
    for item in lst:
        if isinstance(item, list):
            build_freq(item, freq)
        else:
            freq[item] = freq.get(item, 0) + 1
    return freq

print(build_freq(data, {}))
```

---

# 1️⃣7️⃣ Find Word with Maximum Vowels

```python
data = [["apple"], ["banana", ["education"]]]

def max_vowels(lst):
    max_word = ""
    max_count = 0
    for item in lst:
        if isinstance(item, list):
            word = max_vowels(item)
            if word:
                v = sum(1 for c in word if c in "aeiou")
                if v > max_count:
                    max_word, max_count = word, v
        else:
            v = sum(1 for c in item if c in "aeiou")
            if v > max_count:
                max_word, max_count = item, v
    return max_word

print(max_vowels(data))
```

---

# 1️⃣8️⃣ Check If Any Word Is Numeric Only

```python
data = [["123"], ["abc", ["4567"]]]

def contains_numeric(lst):
    for item in lst:
        if isinstance(item, list):
            if contains_numeric(item):
                return True
        else:
            if item.isdigit():
                return True
    return False

print(contains_numeric(data))
```

---

# 1️⃣9️⃣ Deep Replace Substring

```python
data = [["hello world"], ["world peace"]]

def replace_word(lst, old, new):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(replace_word(item, old, new))
        else:
            result.append(item.replace(old, new))
    return result

print(replace_word(data, "world", "earth"))
```

---

# 2️⃣0️⃣ Validate Balanced Brackets in Nested Strings

```python
data = [["(abc)"], ["{[()]}", ["(]]"]]

def is_balanced(s):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

def check_all(lst):
    for item in lst:
        if isinstance(item, list):
            check_all(item)
        else:
            print(item, "->", is_balanced(item))

check_all(data)
```


