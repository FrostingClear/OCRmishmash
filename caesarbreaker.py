from OCRprocessing import *
from SpellChecking import *

from tkinter import *

def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        #Also ignore any other special characters
        elif ch.isalpha() == False:
            ans+=ch
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    #print(ans)
    return ans

def bruteforcedecrypt(outputText):
    
    message = outputText.get("1.0", "end-1c")
    
    Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    #Will only act on capital letters so capitalise the message
    messageUpper = message.upper()
    
    maxFoundMatches = 0
    currentBestKey = 0
    
    #Apply all possible  keys to the message to produce translation
    for key in range(len(Letters)):
                
        translated = ''
        for ch in messageUpper:
            if ch in Letters:
                num = Letters.find(ch)
                num = num - key
                if num < 0:
                    num = num + len(Letters)
                translated = translated + Letters[num]
            else:
                translated = translated + ch
                
        #For each translation break it up into an array
        translatedArray = translated.split()
        
        foundmatches = 0
        
        for word in translatedArray:
            wordToVerify = word
            
            if word.endswith("?") or word.endswith(",") or word.endswith(".") or word.endswith("!"):
                wordToVerify = word[:-1]
            
            if (validWord(wordToVerify)):
                foundmatches += 1
            
            if foundmatches > maxFoundMatches:
                maxFoundMatches = foundmatches
                currentBestKey = key
    
    result = f"{currentBestKey} {encrypt_text(message, -1*currentBestKey)}"
    decryptionResults = {}
    decryptionResults["key"] = currentBestKey
    decoded = encrypt_text(message, -1 * currentBestKey)
    
    messagebox.showinfo("Decryption Result", f"This is my best guess:\n\n {decoded} \n\n(using key: {currentBestKey})")
    
    

        
            
            
                
   
   