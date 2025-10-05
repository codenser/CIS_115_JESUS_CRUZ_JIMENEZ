#this program uses a previous for loop example and introduces a nested for loop

def printWordList():
    words = ["Apples", "Bananas", "Pears", "Carrots"]
    for word in words:
        print(word)
        for char in word:
            print(char)

printWordList()