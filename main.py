from functools import partial
from PIL import Image
import numpy as np

from tkinter import *

from OCRprocessing import *
from SpellChecking import *
from caesarbreaker import *
from Wolfram import *



#General Window
window = Tk()
window.title("OCR Mishmash")
window.geometry("640x800")

#Declare widgets
outputLabel = Label(text="OCR-read output (identified spellings errors are in red", padx=10)
outputText = Text(window, height = 8, width = 70, state=DISABLED, wrap=WORD)

autoCorrectedLabel = Label(text="With autocorrect suggestions")
autoCorrectedText = Text(height= 8, width = 70, wrap=WORD)

teachNewWordLabel = Label(text="Teach New Word")
teachNewWordText = Text(height= 2, width= 35)

OCRcorrectionLabel = Label(text="OCR correction")
incOCRLabel = Label(text="Enter 'incorrect' text")
corOCRLabel = Label(text="enter what it should be")
incorrectOCRText = Text(height= 2, width = 20)
correctedOCRText = Text(height=2, width = 20)

questionLabel = Label(text="If your text was a question you can ask Wolfram")
questionLabel2 = Label(text="This will pull text from the autocorrected text, you can adjust it")

caesarDecryptionLabel = Label(text="If this is caesar ciphered text. Click the button below")

OCRbutton = Button(text="Select Image and Run OCR", command=partial(OCRaction, outputText, autoCorrectedText))
addWordBtn = Button(text="Add word to dictionary", command=partial(addWord, teachNewWordText))
teachOCRbtn = Button(text="Teach OCR correction (use with caution)", command=partial(addOCRcorrection, incorrectOCRText, correctedOCRText))
wolframQuerybtn = Button(text="Ask Wolfram", command=partial(wolframQuery, autoCorrectedText))
caesarDecryptBtn = Button(text="Caesar Decrypt!", command=partial(bruteforcedecrypt, outputText))



#artificially create some padding on the left
blank = Label(text="               ")
blank.grid(column=0, row=0)

OCRbutton.grid(column=1, columnspan=2, row= 0)

outputLabel.grid(column = 1, columnspan=2, row=1)
outputText.grid(column = 1, columnspan=2, row=2)

autoCorrectedLabel.grid(column=1, columnspan=2, row=3)
autoCorrectedText.grid(column=1, columnspan=2, row= 4)

teachNewWordLabel.grid(column = 1, columnspan=2, row=5, pady= 10)
teachNewWordText.grid(column=1, row = 6)
addWordBtn.grid(column=2, row =6)

OCRcorrectionLabel.grid(column=1, columnspan=2, row = 7, ipady=10)

incOCRLabel.grid(column=1, row=8)
corOCRLabel.grid(column=2, row=8)

incorrectOCRText.grid(column=1, row=9)
correctedOCRText.grid(column=2, row=9)
teachOCRbtn.grid(column=1, columnspan=2, row=10)

questionLabel.grid(column=1, columnspan=2, row=11, pady=15)
wolframQuerybtn.grid(column=1, columnspan=2, row=12)

caesarDecryptionLabel.grid(column=1, columnspan=2, row=13, pady=15)
caesarDecryptBtn.grid(column=1, columnspan=2, row = 14)



window.mainloop()






