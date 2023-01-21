import enchant
from tkinter import messagebox

dict = enchant.Dict("en_US")

def loadCustomWords():
    try:
        with open("./CustomWords.txt", encoding="utf-8") as reader:
            for line in reader:
                line = line.removesuffix("\n")
                dict.add_to_session(line)
    except:
        print("File not found")

def addWord(teachNewWordText):
    newWord = teachNewWordText.get("1.0", "end-1c")
    with open("./CustomWords.txt", "a") as filePrinter:
        filePrinter.write(f"{newWord}\n")
    teachNewWordText.delete("1.0","end")
    dict.add_to_session(newWord)
    messagebox.showinfo("Success", f"{newWord} added to dictionary")
    
        

def spellCheckingDemo():
    
    # list of words
    words = ["Zeeland"]
    
    # find those words that may be misspelled
    misspelled =[]
    for word in words:
        if dict.check(word) == False:
            misspelled.append(word)
    print("The misspelled words are : " + str(misspelled))
    
    # suggest the correct spelling of
    # the misspelled words
    for word in misspelled:
        print("Suggestion for " + word + " : " + str(dict.suggest(word)))
        

def spellChecking(wordsList):
    
    # list of words
    words = wordsList
    
    print()
    
    # find those words that may be misspelled
    misspelled =[]
    for word in words:
        
        wordtocheck = word
        
        if word.endswith("?") or word.endswith(",") or word.endswith(".") or word.endswith("!"):
            wordtocheck = word[:-1]
        
        if dict.check(wordtocheck) == False:
            
            if word.isnumeric():
                continue
                
            misspelled.append(word)
    #print()
           
    return misspelled

 
def validWord(word):
    if dict.check(word):
        return True
    else:
        return False  

#Note: since the autocorrect is so dilligent symbols like ? e.g. "Zealand?" would trigger
#a correction, I've applied some code to account for that (this is obviously not an exhaustive correction algorithm!)
def topSuggestion(word):
    
    symbol = ""
    
    if word.endswith("?") or word.endswith(",") or word.endswith(".") or word.endswith("!"):
        symbol = word[-1]
        word = word[:-1]
    
    suggestionsList = dict.suggest(word)
    if len(suggestionsList) > 0:
        
        topsuggestion = suggestionsList[0] + symbol
        return topsuggestion
    else:
        return word + symbol
    
loadCustomWords()
#spellCheckingDemo()


