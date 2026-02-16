# 🚀 Day 02 – Debugging Loops & Off-By-One Errors in Python

Today I continued my Python Debugging Lab (14-Day Series) focusing on one of the most common sources of logical bugs:

👉 Loops & Boundary Errors

---

## 🔍 Topics Covered

- Off-by-one errors in `range()`
- Infinite loop debugging
- Incorrect loop boundaries
- Nested loop mistakes
- Wrong index access inside loops
- Logical vs Runtime errors inside iterations

---

## 💡 Off-by-One Error Example

```python
for i in range(1, 10):
    print(i)
This prints 1 to 9, not 1 to 10.
Reason:
range(start, stop) excludes the stop value.
Correct version:
Python
Copy code
for i in range(1, 11):
    print(i)
💡 Infinite Loop Example
Python
Copy code
i = 0
while i < 5:
    print(i)
This becomes an infinite loop because i is never updated.
Correct version:
Python
Copy code
i = 0
while i < 5:
    print(i)
    i += 1
💡 IndexError Inside Loop
Python
Copy code
x = [1, 2, 3]
for i in range(len(x)):
    print(x[i+1])
This crashes on the last iteration due to invalid index access.
Safer version:
Python
Copy code
for i in range(1, len(x)):
    print(x[i])
🎯 Key Learning
Small mistakes in loop boundaries can:
Produce incorrect results
Cause runtime crashes
Create infinite loops
Break data processing logic
Understanding loop behavior is critical for writing reliable and production-ready Python code.
