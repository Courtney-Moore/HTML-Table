#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#prediction-5
#actual-5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# prediction-error.number_of_days_in_a_week_silicon_or_triangle_sides not defined
# was correct in prediction
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# prediction-5
# was correct in prediction
#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# prediction-5
# was correct in prediction
#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# prediction-5
# was right on the first part, did not think of it actually stating "none"
#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# prediction-error
# was right in prediction
#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# prediction-25
#was right on prediction
#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# prediction-100,10 
# was right on prediction

#9



#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# prediction-8
#was right on prediction

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# prediction-500,300,300,300
#actual-500,500,300,500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#prediction-500,500,500,300
#actual-500,500,300,500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# prediction-500,500,500,300
# acutal-500,500,300,300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# prediction-1,2,3
# actual-1,3,2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# predictions-1,10,3,10
# actual-1,3,5,10