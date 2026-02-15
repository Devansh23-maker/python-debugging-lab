🚀 Day 1 – Building Strong Debugging Foundations in Python

Today I started my Python Debugging Lab to strengthen one of the most underrated but powerful skills in programming — debugging.

Instead of just writing code, I focused on understanding why errors happen and how to systematically fix them.

🔍 Topics Covered

✅ Syntax Errors
✅ TypeError vs Logical Error
✅ IndexError in loops
✅ KeyError in Pandas
✅ Handling Missing Values (NaN behavior in .mean())
✅ Reference vs Copy in Python Lists

💡 Key Learning

One important realization:

a = [1,2,3]
b = a
b.append(4)


This modifies both variables because they reference the same memory location.

Understanding memory behavior prevents silent bugs in:

Data preprocessing

ML pipelines

Feature engineering

Real-world production code

📊 Pandas Insight

Aggregation functions like:

df["salary"].mean()


Ignore missing values by default (skipna=True).

Small details like this matter a lot in real datasets.

🎯 Why I’m Doing This

Strong debugging skills help in:

Cleaning messy datasets

Fixing SQL joins

Solving DAX errors in Power BI

Writing reliable production-ready code

This is part of my journey toward becoming a:

Full-Stack Cloud AI & Data Engineer
