import sys

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

n = int(input())

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
    else:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number

if odd_min != sys.maxsize or odd_max != -sys.maxsize:
    print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},")
else:
    print(f"OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,")

if even_min != sys.maxsize or even_max != -sys.maxsize:
    print(f"EvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")
else:
    print(f"EvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")