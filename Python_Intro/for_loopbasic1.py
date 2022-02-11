# basic
for i in range(1, 150+1):
    print(i)


for seq in range(150+1):
    print(seq)

# multiples of 5
for seq in range(0, 151, 5):
    print(seq)

# counting, the dojo way
for i in range (1,101,1):
        if i % 5 == 0:
            print ('Coding')
        if i % 10 == 0:
            print (' Codining Dojo')


#Sucker's Huge
minimum= int(0)
maximum= int(500000)
total=0
for number in range(minimum, maximum+1):
    if(number % 2 !=0):
        print("{0}".format(number))
        total=total + number
print(total)

#Count down by 4
for seq in range(2018,0,-4):
    print(seq)

#Flexible Counter

lowNum=2
highNum=20
mult=2

for seq in range(2,20,2):
    print(seq)