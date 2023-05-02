#Creating a dictionary and using more functions to define it.

emails = {}

#adding users and their associated emails.

emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'
print(emails)

#deleting one user from the dictionary.

del emails['craig']
print(emails)

#adding a new user to the dictionary.

emails['dalton'] = 'dalton@example.com'
print(emails)

#Creating new variables to define certain aspects of our dictionary.  

users = list(emails.keys())
print(users)

email_list = list(emails.values())
print(email_list)

pairs = list(emails.items())
print(pairs)
