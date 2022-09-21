n = float(input())
m = 0.0
i = 0

while i < 2:
    if n >= 0 and n <= 10:
        i = i + 1
        m = m + n
    if n < 0 or n > 10:
        print('nota invalida')

m = m / 2
print('media = {:.2f}'.format(m))
