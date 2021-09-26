# Task1
#person1 = int(input())
#person2 = int(input())
#result = ''
#if person1 == person2:
#    result = 'draw'
#elif (person1 == 1 and person2 == 2) or \
#     (person1 == 2 and person2 == 3) or \
#     (person1 == 3 and person2 == 1):
#    result = 'first'
#else:
#    result = 'second'
#print(result)

# Task2
#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#if (a <= c and b <= d) or (a <= d and b <= c):
#    result = 'YES'
#else:
#    result = 'NO'
#print(result)

# Task3
#n = int(input())
#half = n // 2 + 1
#count = 2
#for cur_num in range(2,half):    
#    if n % cur_num == 0:
#        count += 1
#print(count)

# Task4
#x = int(input())
#count = 0
#while x > 0:
#    if x % 10 == 2:
#        count += 1
#    x = x // 10
#print(count)

# Task5
#x = int(input())
#sqrt_ex = (8 * x - 7) ** 0.5
#if (sqrt_ex - int(sqrt_ex)) != 0:
#    result = 0
#else:
#    result = 1
#print(result)

# Task6
#x,k = map(int,input().split())
#cur = x
#x = 2 * x
#years = 0
#while cur < x:
#    years += 1
#    cur = cur + (cur * k // 100)
#print(years)

# Task7
#words = input().split()
#s = ''
#for el in words:
#    s = el + ' ' + s
#print(s)

# Task8
#in_file = open('input.txt','r')
#lines = in_file.readlines()
#in_file.close()
#count = 0
#for line in lines:
#    words = line.split()
#    for el in words:
#        if len(el) <= 3:
#            count += 1
#print(count)

# Task9
#words = input().split()
#max = len(words[0])
#for el in words:
#    if max < len(el):
#        max = len(el)
#print(max)

# Task10
#n = input()
#elems = [int(a) for a in input().split()]
#flag = False
#sum1 = 0
#sum2 = 0
#for el in elems:
#    if flag:
#        sum1 += el
#    if el % 2 == 0:
#        sum2 += el
#    flag = not(flag)
#print(sum1,sum2)

# Task11
#n = int(input()) - 1
#elems = [int(a) for a in input().split()]
#i = 1
#s = ''
#while i < n:
#    if elems[i] == elems[i-1] + elems[i+1]:
#        s = s + ' ' + str(elems[i])
#    i += 1
#print(s)

# Task12
n = int(input()) - 1
elems = input().split()
d = {}
for el in elems:
    if el in d:
        d[el] += 1
    else:
        d[el] = 1
print(sorted(d,key=d.get)[-1])