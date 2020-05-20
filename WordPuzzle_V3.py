import random

listOfWords = ['apple', 'mango', 'watermelon', 'kiwi', 'banana', 'pineapple']
randomWord = random.choice(listOfWords)

randomWordCharList = list()
print(randomWordCharList)
print('The answer so far is ')
for i in range(0, len(randomWord)):
    print('_', end=' ')
