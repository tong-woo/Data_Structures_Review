# define the fibonacci() function below...
def fibonacci(n):
    if n == 1 or n == 0:
        return n

    sum = fibonacci(n-1) + fibonacci(n-2)
    return sum



fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "N"