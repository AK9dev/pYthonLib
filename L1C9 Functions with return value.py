def is_prime(count):
    for x in range(2, count):
        if count % x == 0:
            return False

        else:
            return True


def print_primt(imit):
    for num in range(2,limit+1):
        if (is_prime(num)):
            print(num)


limit = int(input("Please enter the upper limit for prome number series?"))
print_prime(limit)
