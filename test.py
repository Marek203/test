n = int(input('zadaj pocet: '))
for i in range(n):
print(' '*(n-1-i) + '*'*(2*i+1))
for i in range(n):
print(' '*i + '*'*(2*n-2*i-1))
