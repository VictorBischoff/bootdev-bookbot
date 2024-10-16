def readContent(bookfile):
    book = open(f"./books/{bookfile}.txt", "r")
    content = book.read()
    print(content)
    book.close()


def getWords(bookfile):
    book = open(f"./books/{bookfile}.txt", "r")
    content = book.read()
    wordCount = len(content.split())
    book.close()
    print(wordCount)


def getChar(bookfile):
    bookfile = open(f"./books/{bookfile}.txt", "r")
    content = bookfile.read()
    charDict = {}
    for char in content:
        char.lower()
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    bookfile.close()
    return charDict


def refineDict(dict):
    for key, value in dict.items():
        if key.isalpha():
            print(f"The {key} charcater was found {value} times")


refineDict(getChar("frankenstein"))

# readContent("frankenstein")
getWords("frankenstein")
# refineDict(getChar(getWords("frankenstein")))
