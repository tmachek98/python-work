#These are all commands used to make/modify lists.

#Making an empty list. 
AWSservices = []

#Adding to the list using append or insert functions.
AWSservices.append("EC2")
AWSservices.append("DynamoDB")
AWSservices.append("Lambda")
AWSservices.append("IAM")
AWSservices.insert(0,"VPC")
AWSservices.insert(5,"Cloud9")

#Printing the list and the length of it.
print(AWSservices) 
print(len(AWSservices))

#Remove items from list.
del AWSservices[0]
del AWSservices[3]

#Printed again for testing.
print(AWSservices) 
print(len(AWSservices))
