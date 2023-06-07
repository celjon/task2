import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time} секунд")
        return result
    return wrapper

@measure_time
def read_and_calculate(file_name):
    with open(file_name, 'r') as file:
        a, b = map(int, file.read().split())
    result = a + b
    with open("output.txt", 'w') as output_file:
        output_file.write(str(result))
    print(f"Результат вычисления сохранен в файле output.txt")

# Тестирование декоратора на функции read_and_calculate
read_and_calculate("input.txt")
