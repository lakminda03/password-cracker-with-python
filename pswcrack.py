import time
from string import ascii_letters, digits, punctuation
from itertools import product

# Define the character set and target password
charset = ascii_letters + digits + punctuation
target_password = "P@ssw0rd"  # Example 8-char password

start_time = time.time()

# Attempt all 8-character combinations
for attempt in product(charset, repeat=8):
    guess = ''.join(attempt)
    if guess == target_password:
        print(f"[+] Password found: {guess}")
        break

end_time = time.time()
print(f"[i] Time taken: {end_time - start_time:.2f} seconds")
