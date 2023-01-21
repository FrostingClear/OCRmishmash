


import cv2
import pytesseract
from PIL import Image
import numpy as np

from SpellChecking import *
from tkinter import END, INSERT, filedialog
from pytesseract import Output

OCRadjustments = {}


def loadAdjustments():
    try:
        with open("./OCRcorrections.txt") as reader:
            for line in reader:
                line = line.removesuffix("\n")
                correction = line.split()
                key = correction[0]
                value = correction[1]
                
                OCRadjustments[key] = value
            #print(OCRadjustments)
    except:
        print("no corrections file found")
        
def addOCRcorrection(incorrectOCRText, correctedOCRText):
    incorrect = incorrectOCRText.get("1.0", "end-1c")
    correct = correctedOCRText.get("1.0", "end-1c")
    correctionEntry = f"{incorrect} {correct}\n"
    
    try:
        with open("./OCRcorrections.txt", "a") as printer:
            printer.write(correctionEntry) #update the file for next load
            OCRadjustments[incorrect] = correct #update the map for next read in the session
            messagebox.showinfo("Success", "Correction file updated")

    except:
        print("no corrections file found")


def imageProcessing(img):
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    img = cv2.GaussianBlur(img, (1, 1), 0)
    return img

def OCRprocessTextWithProcessing(filepath):
    img = np.array(Image.open(filepath))
    img = imageProcessing(img)
    text = pytesseract.image_to_string(img)
    
    text = text.removesuffix("\n")
           
    return text

def OCRprocessText(filepath):
    img = np.array(Image.open(filepath))

    text = pytesseract.image_to_string(img)

    # print("Result: " + text)
    
    return text

def OCRaction(outputText, autoCorrectedText):
    #File selection
    filePath = filedialog.askopenfilename()
    
    interpretedText = OCRprocessTextWithProcessing(filePath)
    interpretedTextArray = interpretedText.split()
    interpretedTextArray = applyTrainedCorrections(interpretedTextArray)
    
    #print(interpretedTextArray)
    
    possibleErrors = spellChecking(interpretedTextArray)
    
    fillOutputWidget(outputText, interpretedTextArray, possibleErrors)
    fillAutoCorrectedWidget(autoCorrectedText,interpretedTextArray, possibleErrors)
    showTesseractVision(filePath)
    

def showTesseractVision(filePath):
    
    img = cv2.imread(filePath)
    img = imageProcessing(img)
    
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow(filePath, img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

    
def applyTrainedCorrections(interpretedTextArray):
    pos = 0
    for word in interpretedTextArray:
        if OCRadjustments.get(word) != None:
            interpretedTextArray[pos] = OCRadjustments.get(word)
            pos += 1
        
    return interpretedTextArray

    
def fillAutoCorrectedWidget(autoCorrectedText, interpretedTextArray, possibleErrors):
    
    autoCorrectedText.delete("1.0","end")
    
    outputPos = 0

    for word in interpretedTextArray:
        
        if word in possibleErrors:
            autoCorrectedText.insert(INSERT, topSuggestion(word) + " ")
        else:
            autoCorrectedText.insert(INSERT, word + " ")
    
    
    
def fillOutputWidget(outputText, interpretedTextArray, possibleErrors):
    #Output the raw result to the output
    #Make the text widget editable, clear it, insert the relevant text then make it read only again
    outputText.config(state = "normal")
    outputText.delete("1.0","end")
    
    outputPos = 0
    
    for word in interpretedTextArray:
        
        startPos = outputPos
        endPos = startPos + len(word)
        
        outputText.insert(INSERT, word + " ")
        if word in possibleErrors:
            outputText.tag_add("mispelling", "1." + str(startPos), "1." + str(endPos))
            outputText.tag_config("mispelling", background="white", foreground="red")
        
        #The +1 accounts for the extra " " we add with each word insertion
        outputPos = endPos + 1
            
    outputText.config(state = "disabled")
    
    
    
    
    
    
loadAdjustments()

