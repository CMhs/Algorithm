# List []
list1 = [1,2,3,'string']
list1 += ['a','b','c',1,2,3]
print(list1)
print(list1[1:4])
print(list1.index('string'))
print(list1.count(1))
print()

a = "I love you, John!"
a = a.split(' ')
print(a)
print(a.index('John!'))
print(len(a))

#Tuple ()
tuple1 = 1234, 5678, 'abcd', 'efgh'
print(tuple1)
print()
# tuple1[0] = 1024 //[ERROR] tuple can't change elements.

#Set {}
a = set('1234567')
b = set('4567890')
print(a)
print(b)
print(a-b) #차집합
print(a|b) #합집합
print(a&b) #교집합
print(a^b) #합집합 - 교집합
print('10' in a)
print('8' in b)


#a = input()
#print(set(a.split()))

#dictionary

data = {1 : 'a', 2 : 'b'}
print(data.keys())
print(data.values())

data2 = {'김영수' : {'영어' : 80, '수학' : 70},
         '박철수' : {'영어' : 50, '국어' : 55}}
data2['김영수']['국어'] = 88
print(data2)
for i in data2.keys():
    print(i,' : ',data2[i])
print()

data3 = {
    'name' : 'John',
    'phone' : '01012345432',
    'email' : 'test@test.com',
    'birth' : 111213
}
print(data3['name'])
data3['birth'] = 101010
data3['city'] = 'seoul'
del data3['email'] #delete key
for i in data3.keys():
    print(i,' : ',data3[i])

def add_num2(value):
    a,b,c,d = map(int, value.split())
    return a+b+c+d
#value = input("insert 4 integers : ")
#print('the sum of numbers is {}'.format(add_num2(value)))

'''
result = ''
for dan in range(2, 21):
    result += "\n{}단!\n".format(dan)
    for i in range(1,21):
        result += "{} x {} = {}\n".format(dan,i,dan*i)
print(result)
'''
count = 0
for i in range(1,10001):
    for j in str(i):
        if j == '8':
            count+=1
print(count)

while(1):
    input1 = input('> ') + ' '
    if input1 == 'help ':
        print('에코를 해주는 프로그램입니다.')
    elif input1 == 'quit ':
        value = input('> 정말 종료하시겠습니까?(Y/N) ')
        if value == 'Y':
            break
        else:
            pass
    else:
        print(input1 * 3)