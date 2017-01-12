#This program is supposed to convert a string to camelCase
#split the string into a list
#capitalize every word EXCEPT for the first item in the list
#convert back to a string and remove spaces
#http://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string-python

print("Please enter a string: ")
response = input()
splitResponse = response.split(' ')

print("test please: ")
s = input()
lst = [word[0].upper() + word[1:] for word in s.split()]
a = "".join(lst)
print(a)


#stringAgain = str(splitResponse)
