# === Challenge 1: Collatz Conjecture ===
# =======================
print("=== Challenge 1: Collatz Conjecture ===")

# Show prompt exactly like the sample (no newline after the prompt label)
print("Enter starting number: ", end="")
current_number = int(input())
step_count = 0

print("Sequence:", end=" ")
print(current_number, end=" ")

# Collatz while loop (unknown iterations → while)
while current_number != 1:
    if current_number % 2 == 0:
        current_number //= 2
    else:
        current_number = current_number * 3 + 1
    print(current_number, end=" ")
    step_count += 1

print()
print(f"Steps: {step_count}")
print()  # blank line ⏎

# =======================
# === Challenge 2: Prime Number Checker ===
# =======================
print("=== Challenge 2: Prime Number Checker ===")

# Prompt exactly like sample
print("Enter a number: ", end="")
n = int(input())

# Known range 2..n-1 → for loop
print(f"Testing divisors from 2 to {n-1}...")
is_prime = True
first_divisor = None

for d in range(2, n):
    if n % d == 0:
        is_prime = False
        first_divisor = d
        break

if is_prime:
    print(f"{n} is prime!")
else:
    print(f"{n} is not prime (divisible by {first_divisor})")
print()  # blank line ⏎

# =======================
# === Challenge 3: Multiplication Table ===
# =======================
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

# Header spacing: sample shows 6 spaces before the first "1"
print("      ", end="")             # 6 spaces
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

# Rows: sample shows row label in width 2, then 4 spaces before first product
for row in range(1, 11):
    print(f"{row:2}", end="")
    print("    ", end="")           # 4 spaces after row label to match sample
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()