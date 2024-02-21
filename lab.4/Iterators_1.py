def square_generator(N):
    for i in range(N):
        yield i ** 2

# Пример использования:
N = 5
squares = square_generator(N)
for square in squares:
    print(square)
