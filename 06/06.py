with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

answers = ''
groupAnswers = []

for line in data:
    if line != '':
        answers += line
    else:
        groupAnswers.append(answers)
        answers = ''
#catch the last set of answers
groupAnswers.append(answers)

totalQuestions = 0
for answers in groupAnswers:
    uniqueChars = set(answers)
    totalQuestions += int(len(uniqueChars))

print(totalQuestions)