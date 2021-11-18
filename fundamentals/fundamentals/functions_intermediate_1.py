x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1- Update values in Dictionaries and lists
    # a
x[1][0] = 15
print(x)

    # b
students[0]["last_name"] = "Bryant"
print(students)

    # c
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

    # d
z[0]['y'] = 30
print(z)
# 2- Iterate through a list of dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(some_list):
    for i in range(0,len(some_list)):
        print(some_list[i].items())

iterate_dictionary(students) 

# 3- Get values from a list of dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary_2(key_name, some_list):
    for i in range(0, len(some_list)):
        print(some_list[i][key_name])

iterate_dictionary_2('first_name', students) 

# 4- Iterate through a dictionary with list values
def print_info(some_dict):
    for i in some_dict:
        list_size = len(some_dict[i])
        print(list_size, i.upper())
        for j in some_dict[i]:
            list_size += 1
            print(j)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print_info(dojo)