from flask import Flask,jsonify, request
app = Flask(__name__)



#function for getting combinations of x

def generateCombo(word):
    #print("word",word)
    allCombinations = []
    lengthOfText = len(word)
    lastIndex = lengthOfText - 1
    #print("lastIndex",lastIndex)

    for i in range(0,lengthOfText):
        #print(i)
        if i == 0 :
            nextIndex = i +1
            
            newWord = word[nextIndex:]
            
            lastIndex = len(newWord) - 1
            allCombo = swapLetters(newWord,0,lastIndex)
            #print(word[0])
            
            #print("combo",allCombo)
            for x in allCombo:
                lengthOfX = len(x)
                a = lengthOfText-1
                if  lengthOfX == a:
                    combo = ''.join(x)
                    combo = word[0] + combo
                    allCombinations.append(combo)
                    
            
        if i == lastIndex :
            
            newWord = word[:i]
            lastIndex = len(newWord) - 1
            allCombo = swapLetters(newWord,0,lastIndex)
            #print("*"*20)
            #print(word[lastIndex])
            #print("combo",allCombo)
            
            
            for x in allCombo:
                lengthOfX = len(x)
                a = lengthOfText-1
                if lengthOfX == a:
                    combo = ''.join(x)
                    combo = word[lastIndex] + combo
                    allCombinations.append(combo)
            
            
        if i != 0 and i != lastIndex :
            #print("*"*20)
            #print(word[i])
            nextIndex = i + 1
            newWord = word[:i] + word[nextIndex:]
            #print("newWord",newWord)
            
            lastIndex = len(newWord) - 1
            allCombo = swapLetters(newWord,0,lastIndex)
            #print("combo",allCombo)
            #print("b",word[i])
            
            for x in allCombo:
                lengthOfX = len(x)
                a = lengthOfText-1
                if lengthOfX == a:
                    combo = ''.join(x)
                    combo = word[i] + combo
                    allCombinations.append(combo)
            
    return allCombinations



#function for swapping the letters in a word
def swapLetters(words,startingIndex,lastIndex):
    combinations = []
    lengthOfWords = len(words)
    lastIndex = lengthOfWords -1
    copyOfWords = []

    for letter in words:
        copyOfWords.append(letter)
    
    if startingIndex == lastIndex :
        combinations.append(copyOfWords)
        
        
    else :
        for i in range(lengthOfWords):
            if i < lengthOfWords:
                copyOfWords[startingIndex],copyOfWords[i] = copyOfWords[i], copyOfWords[startingIndex]
                combinations+=swapLetters(copyOfWords,startingIndex+1,lastIndex)
                copyOfWords[startingIndex],copyOfWords[i] = copyOfWords[i], copyOfWords[startingIndex]
        
    return combinations
    
    
#function for sorting the words
def sortList (words):
    sortedWords = sorted(words)
    return sortedWords

#function for creating unique lists
def createUniqueList(words):
    uniqueList = []
    for word in words:
        if word not in uniqueList:
            uniqueList.append(word)
    return uniqueList

#function for finding index of a word
def findIndex(term, Word):
    if term in Word:
        index = Word.index(term)
        return index 
    else:
        errorMessage = "not Found"
        return errorMessage






#function for generating error strings
# Error code 1 - wrong format 
# Error code 2 - wrong request type
# Error code 3 - wrong route
def getErrorStatements(errorCode):
    errorMessage1 = "You have entered a wrong format. Kindly retry request using string format"
    errorMessage2 = "You used a wrong format for the request, kindly use a GET request to the route /permutation-index"
    errorMessage3 = "You have gone to the wrong route, kindly visit /permutation-index"
    defaultErrorMEssage= "Something went wrong, please contact the administrator"

    if errorCode == 1 :
        return errorMessage1
    elif errorCode == 2 :
        return errorMessage2
    elif errorCode == 3:
        return errorMessage3
    else :
        return defaultErrorMEssage

#Flask API routes

@app.route('/',methods=['GET','POST'])
def index():
    #some_json = request.get_json()
    response = getErrorStatements(3)
    return jsonify({'Error' : response}),201

@app.route('/permutation-index/<string:word>',methods=['GET'])
def getPermutation(word):
    if (request.method == 'GET'):
       #get the input
        wordInput = word

        #generate all possible permutations
        word = generateCombo(word)

        #sort list alphabetically
        word = sortList(word)

        #remove duplicates
        word = createUniqueList(word)

        #find the index of the word
        findWord = findIndex(wordInput,word)
        index = findWord + 1

        #return the index

        return jsonify({"indexOfGivenPermutation" : index}),201
    else:
        response = getErrorStatements(2)
        return jsonify({"Error":response})

if __name__ == '__main__':
    app.run(debug=True)