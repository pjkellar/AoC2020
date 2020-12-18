import re

with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

answers = []
groupAnswers = []

for line in data:
    if line != '':
        answers.append(line)
    else:
        groupAnswers.append(answers)
        answers = []

#catch the last set of answers
groupAnswers.append(answers)

p1 = 0
p2 = 0

for answers in groupAnswers:
    charString = ''
    for person in answers:
        charString += person 
    uniqueChars = set(charString)
    p1 += len(uniqueChars)

print(p1)
print(p2)