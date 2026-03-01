import re

# 1️ 'a' followed by zero or more 'b'
print("1:", bool(re.fullmatch(r"ab*", "abbb")))

# 2️ 'a' followed by 2 to 3 'b'
print("2:", bool(re.fullmatch(r"ab{2,3}", "abb")))

# 3️ sequences of lowercase letters joined with underscore
text3 = "hello_world test_value abc"
print("3:", re.findall(r"[a-z]+_[a-z]+", text3))

# 4️ one uppercase letter followed by lowercase letters
text4 = "Hello world Python Language"
print("4:", re.findall(r"[A-Z][a-z]+", text4))

# 5️ 'a' followed by anything, ending in 'b'
print("5:", bool(re.fullmatch(r"a.*b", "a123b")))

# 6️ replace space, comma, dot with colon
text6 = "Hello, world. Python is fun"
print("6:", re.sub(r"[ ,\.]", ":", text6))

# 7️ snake_case to camelCase
snake = "snake_case_string"
camel = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), snake)
print("7:", camel)

# 8️ split string at uppercase letters
text8 = "SplitThisString"
print("8:", re.split(r"(?=[A-Z])", text8))

# 9️ insert spaces before capital letters
text9 = "InsertSpacesBetweenWords"
print("9:", re.sub(r"(?<!^)([A-Z])", r" \1", text9))

# 10 camelCase to snake_case
camel10 = "camelCaseStringExample"
snake10 = re.sub(r"([A-Z])", r"_\1", camel10).lower()
print("10:", snake10)