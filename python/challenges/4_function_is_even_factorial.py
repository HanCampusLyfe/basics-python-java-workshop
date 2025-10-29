# Fungsi untuk memeriksa apakah sebuah bilangan genap
def is_even(num):
    return num % 2 == 0   # True kalau genap, False kalau ganjil

# Tes fungsi
print(is_even(4))   # True
print(is_even(7))   # False


# Fungsi untuk menghitung faktorial (iteratif)
def factorial(n):
    if n < 0:
        raise ValueError("Faktorial tidak didefinisikan untuk bilangan negatif.")
    if n == 0 or n == 1:
        return 1
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

# Tes fungsi
print(factorial(5))  # 120
print(factorial(0))  # 1
