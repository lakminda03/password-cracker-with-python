from string import ascii_letters, digits, punctuation
from itertools import product

charset = ascii_letters + digits + punctuation

# WARNING: This will take forever
for combo in product(charset, repeat=8):
    password = ''.join(combo)
    print(password)
