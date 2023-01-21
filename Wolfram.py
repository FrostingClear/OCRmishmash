from tkinter import messagebox
import wolframalpha

def wolframQuery(questionWidget):
    
    question = questionWidget.get("1.0", "end-1c")
    app_id = "Enter your own appID here"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    
    try:
        answer = next(res.results).text
        messagebox.showinfo("Wolfram Answers:", f"Wolfram Answers: {answer}")
    except:
        messagebox.showinfo("Wolfram Answers:", f"That wasn't a question")
