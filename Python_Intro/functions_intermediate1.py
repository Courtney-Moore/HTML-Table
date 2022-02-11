# 1.Update Values in Dictionaries and Lists
# -Change the value 10 in x to 15
# -Change the last name of the first student from Jorda to Bryant
# -In the sports_directory, change 'Messi' to Andres'
# Change the value 20 in z to 30

x = [[5, 2, 3], [10, 8, 9]]
x[1][0]=15
print(x)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = "Bryant"
print(students)

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)

z = [{'x': 10,'y': 20}]
z[0] = 30
print(z)
# Create a function iterateDictionary(some_list)that give a list of dictinaries, the function loops through each dictinary in the list and prints each key and the associated value.


students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterateDictionary(students):
    for i in range(len(students)):
        print(students[i]['first_name'],students[i]['last_name'])
iterateDictionary(students)




# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonelcopy
# # Get Values From a List of Dictionaries