#This program is supposed to convert a string to camelCase
#split the string into a list
#capitalize every word EXCEPT for the first item in the list
#convert back to a string and remove spaces
#http://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string-python

print("Please enter a string: ")
response = input()
splitResponse = response.split(' ')

responseList = []

for words in splitResponse:

    singleWord = words.capitalize #capitalize first character of each word
    print(singleWord)
    responseList.append(words)

#stringAgain = ''.join(singleWord)
stringAgain = str(splitResponse)
print(responseList)
print(splitResponse)
print(stringAgain)
