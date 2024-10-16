import random
from bit import Key
import string

# The string we are searching for
search = "1kid".lower()


# Generate a random secret key
def random_secret():
    return ''.join(random.choice(string.hexdigits) for _ in range(64))


# Extract the Bitcoin address from a secret key
def bitcoin_address(secret):
    key = Key.from_hex(secret)
    return key.address


# Case insensitive comparison with the search string
def match_found(address):
    return address[1:1 + len(search)] == search


def main():
    # Loop continuously
    while True:
        # Generate a random secret
        secret = random_secret()
        # Get the address
        address = bitcoin_address(secret)
        # Does it match our search string? (1kid)
        if match_found(address.lower()):
            # Success!
            print(f"Found vanity address! {address}")
            print(f"Secret: {secret}")
            break


if __name__ == "__main__":
    main()
