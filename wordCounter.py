def countWordsFromFile():
    path = input("Give your file path : ")
    fileName = open(path,'r')
    numberOfWords = 0
    for line in fileName:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("The number of words in your file are : ") 
    print(numberOfWords)

countWordsFromFile()