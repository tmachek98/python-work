#Creating a empty list.

users = []

#Adding users with append function.

users.append('kevin')
users.append('bob')
users.append('alice')
print(users) 

#Deleting user with del function.

del users[1]
print(users)

#Reversing the current list by crearing a new variable.

rev_users = list(reversed(users))
print(rev_users) 

#Adding a new user using the insert function with a specific index.

users.insert(1, 'melody')
print(users)

#Concatnating to the list with more new users.

users += ['andy', 'wanda', 'jim']
print(users)

#Creating a new variable to show middle users with indexing.

center_users = users[2:4] 
print(center_users)

