# lambda_with_sorted.py

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# Example 1: sort by score
print(sorted(students, key=lambda s: s["score"]))

# Example 2: sort by name
print(sorted(students, key=lambda s: s["name"]))

# Example 3: reverse sort by score
print(sorted(students, key=lambda s: s["score"], reverse=True))

# Example 4: sort by name length
print(sorted(students, key=lambda s: len(s["name"])))
