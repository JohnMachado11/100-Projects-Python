# "A natural number which has exactly two factors, i.e. 1 and the number itself, is a prime number. 
# In simple words, if a number is only divisible by 1 and itself, then it is a prime number. 
# Every prime number is an odd number except number 2."

def prime_checker(number):
    is_prime = True

    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
