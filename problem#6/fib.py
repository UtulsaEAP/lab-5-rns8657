def fibonacci(n):
    Fibonacci_sequence = [0, 1]
    if (n > 0):
        for i in range(n - 1):
            Fibonacci_sequence.append(Fibonacci_sequence[i + 1] + Fibonacci_sequence[i])
        return Fibonacci_sequence[len(Fibonacci_sequence) - 1]
    elif(n == 0):
        return(0)
    else: 
        return(-1)
    




if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')