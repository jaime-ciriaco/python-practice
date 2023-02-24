def is_prime(value):
    if value % 2 != 1:
        return str(value) + " is not a prime value"
    else:
        return str(value) + " is a prime value"


prime = is_prime(13)
print(prime)