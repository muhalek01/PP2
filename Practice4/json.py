# json.py

import json

# --- JSON string to Python ---
json_text = '{"name": "Ali", "age": 20, "city": "Almaty"}'
data = json.loads(json_text)

print("Name:", data["name"])


# --- Python to JSON string ---
person = {
    "name": "Ali",
    "age": 20,
    "city": "Almaty"
}

json_string = json.dumps(person, indent=4)
print("\nJSON string:")
print(json_string)


# --- Write JSON to file ---
with open("data.json", "w") as f:
    json.dump(person, f, indent=4)

print("\nData written to data.json")


# --- Read JSON from file ---
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("Loaded from file:", loaded_data)


# --- Working with sample-data.json ---
# (работает если файл есть в папке)

try:
    with open("sample-data.json") as f:
        sample = json.load(f)
        print("\nSample data:")
        print(sample)
except FileNotFoundError:
    print("\nsample-data.json not found (skip if not provided)")