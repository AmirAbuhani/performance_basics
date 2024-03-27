

# Time complexity is O(2^n)
def recursive_fibonacci_sequence(number):
    fibonacci_sequence = []

    def fibonacci(fib_number):
        if fib_number <= 1:
            return 1
        else:
            return fibonacci(fib_number - 1) + fibonacci(fib_number - 2)

    for i in range(number):
        fibonacci_sequence.append(fibonacci(i))
    return fibonacci_sequence


# Time complexity is 0(n)
def iterative_fibonacci(number):
    fibonacci_list = [1, 1]
    for index in range(2, number):
        fibonacci_list.append(fibonacci_list[index - 1] + fibonacci_list[index - 2])
    return fibonacci_list



