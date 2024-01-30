# sum_numbers.py
def sum_numbers(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

"""
cythonize -i f1_sum_numbers.py
gcc -shared -o f1_sum_numbers.dll f1_sum_numbers.c


"""
if __name__ == "__main__":
    n = 1000000
    print("Sum:", sum_numbers(n))
