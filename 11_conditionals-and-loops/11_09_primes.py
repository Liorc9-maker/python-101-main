# Print out every prime number between 1 and 1000.
for num in range(2,1001):
    is_prime = True
    for prime_num in range(2, int( num ** 0.5) +1):
        if num % prime_num == 0:
            is_prime = False
            break
    if is_prime:
        print(num)