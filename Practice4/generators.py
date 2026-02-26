# generators.py

# --- Using iter() and next() ---
print("ITERATOR with iter() and next():")
numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))


# --- Custom Iterator ---
print("\nCUSTOM ITERATOR:")

class CountUp:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = CountUp(5)

for num in counter:
    print(num)


# --- Generator Function ---
print("\nGENERATOR FUNCTION:")

def my_generator(n):
    for i in range(n):
        yield i

for value in my_generator(5):
    print(value)


# --- Generator Expression ---
print("\nGENERATOR EXPRESSION:")

squares = (x*x for x in range(5))

for s in squares:
    print(s)