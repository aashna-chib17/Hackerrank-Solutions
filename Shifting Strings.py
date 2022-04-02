s = input()
s = list(s)
leftShifts = int(input())
rightShifts = int(input())
for _ in range(leftShifts):
    a = s.pop(0)
    s.append(a)
for _ in range(rightShifts):
    a = s.pop()
    s.insert(0,a)
print(''.join(s))
