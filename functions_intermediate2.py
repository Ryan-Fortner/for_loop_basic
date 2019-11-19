# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
#a.) answer
x[[1][0]] = [15,8,9]

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#b.) answer
students[0]['last_name'] = 'Bryant'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
#c.) answer
sports_directory['soccer'][0] = 'Andres' 


#d.) answer
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30



# 2. Iterate Through the List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#answer
def iterate_Dictionary(students):
    for curr_dict in students:
        display_str = ""
        for curr_key in curr_dict.keys():
            display_str += f"{curr_key} - {curr_dict[curr_key]},"
        print(display_str)
iterate_Dictionary(students)

#3. Get Values from a list of dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#answer
def iterate_Dictionary2(first_name, students):
    for curr_dict in students:
        print(curr_dict['first_name'])
iterate_Dictionary2('first_name', students)

def iterate_Dictionary2(last_name, students):
    for curr_dict in students:
        print(curr_dict['last_name'])
iterate_Dictionary2('last_name', students)

#4. Iterate through a dictionary with list values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#answer
def printInfo(dojo):
    for curr_key in dojo.keys():
        print(f"{len(dojo['locations'])} {'locations'.upper()}")
        for item in dojo['locations']:
            print(item)
        print('\n')
    for curr_key in dojo.keys():
        print(f"{len(dojo['instructors'])} {'instructors'.upper()}")
        for item in dojo['instructors']:
            print(item)
        print('\n')
printInfo(dojo)



