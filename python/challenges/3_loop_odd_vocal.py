# TODO: Program untuk mencetak bilangan ganjil dari 1 hingga 15
odd_numbers = []
for i in range(1, 16):       # dari 1 sampai 15
    if i % 2 != 0:           # jika sisa bagi 2 bukan 0 → ganjil
        odd_numbers.append(i)

print("Bilangan ganjil dari 1 sampai 15:", odd_numbers)

# TODO: Program menghitung jumlah huruf vokal
word = input("Masukkan kata: ").lower()

vowels = "aiueo"
count = 0

for kata in word:
    if kata in vowels:
        count += 1

print("Jumlah huruf vokal:", count)
