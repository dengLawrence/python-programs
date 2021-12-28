def hawkID():
    return "lldeng"

import tkinter
import random

mainWindow = None
num1 = None
num2 = None
operandRoll = None
operand = None
history = []
guesses = 0
attemptedQuestions = 0
solvedQuestions = 0
solvedGuesses = []

def isCorrect(roll, num1, num2, guess):
    if roll == 1 and num1 + num2 == guess:
        return True
    if roll == 2 and num1 - num2 == guess:
        return True
    if roll == 3 and num1 * num2 == guess:
        return True
    if roll == 4 and num1 / num2 == guess:
        return True
    else:
        return False

def checkAnswer():
    global operandRoll
    global num1
    global num2
    global answerEntry
    global statusLabel
    global solvedQuestions
    global guesses
    global solvedGuesses
    global checkButton
    global attemptedQuestions
    guess = int(answerEntry.get())
    if guesses == 0:
        attemptedQuestions = attemptedQuestions + 1
    if isCorrect(operandRoll, num1, num2, guess):
        guesses = guesses + 1
        statusLabel.configure(text = str(guess) + " is correct. Guesses: {}".format(guesses))
        answerEntry.delete(0, tkinter.END)
        checkButton['state'] = 'disabled'
        answerEntry['state'] = 'disabled'
        solvedQuestions = solvedQuestions + 1
        solvedGuesses.append(guesses)
    else:
        guesses = guesses + 1
        statusLabel.configure(text = str(guess) + " is incorrect. Guesses: {}".format(guesses))
        answerEntry.delete(0, tkinter.END)
    
def generateProblem():
    global operandRoll
    global operand
    global num1
    global num2
    global history
    global v
    operandRoll = v.get()
    if operandRoll == 0:
        operandRoll = random.randint(1, 4)
    if operandRoll == 1:
        operand = "+"
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
    elif operandRoll == 2:
        operand = "-"
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, num1)
    elif operandRoll == 3:
        operand = "*"
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    elif operandRoll == 4:
        operand = "/"
        num2 = random.randint(1, 32)
        multiple = random.randint(1, 1000//num2)
        num1 = multiple * num2
    problemSet = [operand, num1, num2]
    if problemSet in history:
        generateProblem()
    else:
        history.append(problemSet)

def newProblem():
    global problemLabel
    global num1
    global operand
    global num2
    global answerEntry
    global checkButton
    global guesses
    guesses = 0
    generateProblem()
    problemLabel.configure(text="{} {} {} = ".format(num1, operand, num2))
    statusLabel.configure(text="Make a guess. Guesses: 0")
    checkButton['state'] = 'normal'
    answerEntry['state'] = 'normal'

def quitGame():
    global solvedGuesses
    global solvedQuestions
    global attemptedQuestions
    mainWindow.destroy()
    if solvedGuesses == []:
        averageGuesses = None
    else:
        averageGuesses = sum(solvedGuesses) / len(solvedGuesses)
    print("Attempted Problems: {} \nSolved Problems: {}\nAverage Number of Guesses for Solved Problems: {}".format(attemptedQuestions, solvedQuestions, averageGuesses))

def initialWindow():
    global operand
    global num1
    global num2
    global mainWindow
    global answerEntry
    global statusLabel
    global problemLabel
    global checkButton
    global v
    mainWindow = tkinter.Tk()
    mainWindow.title("Basic Math Game")

    topFrame = tkinter.Frame()
    topFrame.pack()
    
    midFrame = tkinter.Frame()
    midFrame.pack()

    bottomFrame = tkinter.Frame()
    bottomFrame.pack()

    v = tkinter.IntVar()
    v.set(0)

    generateProblem()

    problemLabel = tkinter.Label(topFrame, text="{} {} {} = ".format(num1, operand, num2))
    problemLabel.pack(side=tkinter.LEFT)
    answerEntry = tkinter.Entry(topFrame)
    answerEntry.pack(side=tkinter.LEFT)
    checkButton = tkinter.Button(topFrame, text="Check", command=checkAnswer)
    checkButton.pack()
    
    statusLabel = tkinter.Label(midFrame, text="Make a guess. Guesses: 0")
    statusLabel.pack(side=tkinter.LEFT)
    problemButton = tkinter.Button(midFrame, text="New Problem", command = newProblem)
    problemButton.pack()

    problemTypeLabel = tkinter.Label(bottomFrame, text="Problem type:")
    problemTypeLabel.pack()
    anyButton = tkinter.Radiobutton(bottomFrame, text="Anything", variable=v, value=0)
    anyButton.pack()
    plusButton = tkinter.Radiobutton(bottomFrame, text="+", variable=v, value=1)
    plusButton.pack()
    minusButton = tkinter.Radiobutton(bottomFrame, text="-", variable=v, value=2)
    minusButton.pack()
    timesButton = tkinter.Radiobutton(bottomFrame, text="*", variable=v, value=3)
    timesButton.pack()
    divideButton = tkinter.Radiobutton(bottomFrame, text="/", variable=v, value=4)
    divideButton.pack()

    quitButton = tkinter.Button(bottomFrame, text="Quit Game", command=quitGame)
    quitButton.pack()

initialWindow()
mainWindow.mainloop()
