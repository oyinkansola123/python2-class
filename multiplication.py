num = int(input('Which table you need write it here:'))
start_range = int(input('write the number from where to start:'))
end_range = int(input('write the end of the number you need:'))
print('This is the table of', num)
for i in range(start_range, end_range + 1):
   print(num, 'x', i, '=', num*i)

for a in range(1,13):
    for b in range(1,13):
        # print(b)
        print(a ,'x',b,'=',a*b)
        # print(b)