###################################
# CSC FINAL
###################################
from Tkinter import *
from time import sleep
import RPi.GPIO as GPIO
from pygame import *
from random import randint
import sys

GPIO.setwarnings(False)


init()
mixer.init()
right = mixer.Sound("right.wav")
wrong = mixer.Sound("wrong.wav")
grr = mixer.Sound("grr.wav")
win = mixer.Sound("win.wav")
main = mixer.Sound("mainmenu.wav")
music = mixer.music.load("backgroundact.mp3")

mixer.music.set_volume(0.4)


#Question class is what defines the question object each question consisting of a question picture, and an answer
class Question(object):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


#the next 3 functions sets how many points are deducted for getting a question wrong
def setDifficultyMed():
    Game.r = 2

def setDifficultyEasy():
    Game.r = 1

def setDifficultyHard():
    Game.r = 3

def constellations():
    for i in range(0,7):
        GUI.screen(7+i)
        root.update()
        sleep(2)


#the main game class
class Game(Frame):
    def __init__ (self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.currentQuestion = 0


    #the function that sets up the buttons that allow you to pick a difficulty
    def makeButtons(self):
        self.b = Frame(root)
        self.b.pack(side = BOTTOM)
        Game.buttonmed = Button(self.master, text = "Easy", command = setDifficultyEasy)
        Game.buttonmed.pack(in_ = self.b, side = LEFT)
        Game.buttoneasy = Button(self.master, text = "Medium", command = setDifficultyMed)
        Game.buttoneasy.pack(in_ = self.b, side = LEFT)
        Game.buttonhard = Button(self.master, text = "Hard", command = setDifficultyHard)
        Game.buttonhard.pack(in_ = self.b, side = LEFT)
        
        


    def init_window(self):
        self.master.title("GUI")
        Game.question = Label(root, image = self.currentQuestion.question)
        Game.question.pack()
        

    #sets what the screen should be if its not currently displaying a question i.e. if its the start screen
    def screen(self, index):
        start = PhotoImage(file = "start.gif") #index value 0
        lose1 = PhotoImage(file = "lose.gif") #index value 1
        lose2 = PhotoImage(file = "background.gif")# 2
        win1 = PhotoImage(file = "win.gif")# 3
        win2 = PhotoImage(file = "background.gif") # 4
        correct = PhotoImage(file = "right.gif") # 5
        wrong = PhotoImage(file = "wrong.gif") # 6
        con1 = PhotoImage(file = "con1.gif")#7
        con2 = PhotoImage(file = "con2.gif")#8
        con3 = PhotoImage(file = "con3.gif")#9
        con4 = PhotoImage(file = "con4.gif")#10
        con5 = PhotoImage(file = "con5.gif")#11
        con6 = PhotoImage(file = "con6.gif")#12
        con7 = PhotoImage(file = "con7.gif")#13
        con8 = PhotoImage(file = "con8.gif")#14
        screenArray = [win1, win2, lose1, lose2, start, correct, wrong, con1, con2, con3, con4, con5, con6, con7, con8]
        Game.img = screenArray[index]
        Game.question.config(image = Game.img)
        Game.question.image = Game.img

    #tells the game what question is to be shown
    def setQuestion(self):
        Game.img = self.currentQuestion.question
        Game.question.config(image = Game.img)
        Game.question.image = Game.img

    #calls the question class to actually make the question objects
    def createQuestions(self):
        #first sets img# to a file location
        img1 = PhotoImage(file = "q1.gif")
        img2 = PhotoImage(file = "q2.gif")
        img3 = PhotoImage(file = "q3.gif")
        img4 = PhotoImage(file = "q4.gif")
        img5 = PhotoImage(file = "q5.gif")
        img6 = PhotoImage(file = "q6.gif")
        img7 = PhotoImage(file = "q7.gif")
        img8 = PhotoImage(file = "q8.gif")
        img9 = PhotoImage(file = "q9.gif")
        img10 = PhotoImage(file = "q10.gif")
        img11 = PhotoImage(file = "q11.gif")
        img12 = PhotoImage(file = "q12.gif")
        img13 = PhotoImage(file = "q13.gif")
        img14 = PhotoImage(file = "q14.gif")
        img15 = PhotoImage(file = "q15.gif")
        img16 = PhotoImage(file = "q16.gif")
        img17 = PhotoImage(file = "q17.gif")
        img18 = PhotoImage(file = "q18.gif")
        img19 = PhotoImage(file = "q19.gif")
        img20 = PhotoImage(file = "q20.gif")
        img21 = PhotoImage(file = "q21.gif")
        img22 = PhotoImage(file = "q22.gif")
        img23 = PhotoImage(file = "q23.gif")
        img24 = PhotoImage(file = "q24.gif")
        img25 = PhotoImage(file = "q25.gif")
        img26 = PhotoImage(file = "q26.gif")
        img27 = PhotoImage(file = "q27.gif")
        img28 = PhotoImage(file = "q28.gif")
        img29 = PhotoImage(file = "q29.gif")
        img30 = PhotoImage(file = "q30.gif")
        img31 = PhotoImage(file = "q31.gif")
        img32 = PhotoImage(file = "q32.gif")
        img33 = PhotoImage(file = "q33.gif")
              
        

        #actually creates the question, first argument assigns a picture second argument assigns an answer
        Game.q1 = Question(img1, 0)
        Game.q2 = Question(img2, 1)
        Game.q3 = Question(img3, 2)
        Game.q4 = Question(img4, 3)
        Game.q5 = Question(img5, 4)
        Game.q6 = Question(img6, 5)
        Game.q7 = Question(img7, 6)
        Game.q8 = Question(img8, 7)
        Game.q9 = Question(img9, 5)
        Game.q10 = Question(img10, 4)
        Game.q11 = Question(img11, 5)
        Game.q12 = Question(img12, 3)
        Game.q13 = Question(img13, 4)
        Game.q14 = Question(img14, 0)
        Game.q15 = Question(img15, 0)
        Game.q16 = Question(img16, 1)
        Game.q17 = Question(img17, 2)
        Game.q18 = Question(img18, 1)
        Game.q19 = Question(img19, 2)
        Game.q20 = Question(img20, 2)
        Game.q21 = Question(img21, 3)
        Game.q22 = Question(img22, 6)
        Game.q23 = Question(img23, 6)
        Game.q24 = Question(img24, 7)
        Game.q25 = Question(img25, 7)
        Game.q26 = Question(img26, 6)
        Game.q27 = Question(img27, 7)
        Game.q28 = Question(img28, 5)
        Game.q29 = Question(img29, 4)
        Game.q30 = Question(img30, 3)
        Game.q31 = Question(img31, 2)
        Game.q32 = Question(img32, 1)
        Game.q33 = Question(img33, 0)
        
        

        #list of the questions to pull from
        self.tempquestions = [Game.q1, Game.q2, Game.q3, Game.q4, Game.q5, Game.q6, Game.q7, Game.q8, Game.q9, Game.q10, Game.q11, Game.q12, Game.q13, Game.q14, Game.q15, Game.q16, Game.q17, Game.q18, Game.q19, Game.q20, Game.q21, Game.q22, Game.q23, Game.q24, Game.q25, Game.q26, Game.q27, Game.q28, Game.q29, Game.q30, Game.q31, Game.q32, Game.q33]
        #this is the randomized question blank that the game uses each instance
        self.questions = []
        #randomized self.questions array
        for i in range(len(self.tempquestions)):
            if len(self.tempquestions) > 1:
                x = randint(0,len(self.tempquestions)-1)
                self.questions.append(self.tempquestions[x])
                self.tempquestions.remove(self.tempquestions[x])
            else:
                self.questions.append(self.tempquestions[0])
        
    def imageDisplay(self):     
        self.currentQuestion = self.questions[Game.a]
        
        
    #calls on each function
    def play(self):
        Game.a = 0
        Game.makeButtons(self)
        self.createQuestions()
        self.imageDisplay()
        self.init_window()
        self.setQuestion()
        self.screen(4)
        
        
        
        

    def UpdateQ(self, value):
        if Game.a == len(self.questions) - 1:
            Game.a = 0
        else:
            Game.a += value
        self.imageDisplay()
        self.setQuestion()
        
        
#the fun stuff that makes the GUI
root = Tk()
#root.overridedirect removes the bar across the top making the game fullscreen
root.overrideredirect(1)
root.geometry("800x480")
root.focus_set()
root.bind("<Escape>", sys.exit)
GUI = Game(root)
GUI.play()

##########################################################


leds = [26,19,13,6,5,22,27,17]
button = [21,20,16,12,25,24,23,18]

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)


x = 0
GPIO.output(leds, False)


root.update()
    
Game.r = 1

#detects when to go past the start screen and start the game
while(True):
    main.play(-1)
    pressed = False
    while (not pressed):
        for i in range (len(button)):
            while (GPIO.input(button[i]) == True):
                pressed = True
                GUI.b.pack_forget()
                root.update()
                constellations()
                GUI.UpdateQ(0)
                root.update()              
    main.stop()
    mixer.music.play(-1)
    while(True):
        pressed = False
        while (not pressed):
            for i in range (len(button)):
                while (GPIO.input(button[i]) == True):
                     val = i
                     pressed =True
                    

        if val == GUI.currentQuestion.answer:
            GPIO.output(leds[x], True)
            right.play()
            GUI.screen(5)
            root.update()
            sleep(1)
            if x < 7:

                x += 1
                GUI.UpdateQ(1)
                root.update()

            else:
                win.play()
                GPIO.output(leds[7], True)
                sleep(1)            
                GPIO.output(leds, False)
                
                for i in range(0,4):
                    mixer.music.stop()
                    
                    GPIO.output(leds,True)
                    GUI.screen(0)
                    root.update()
                    sleep(0.5)
                    GPIO.output(leds, False)
                    GUI.screen(1)
                    root.update()
                    sleep(0.5)
                GUI.screen(0)
                root.update()
                sleep(4)
                root.destroy()
                GPIO.cleanup()
                exit()
        else:
            #when you get a question wrong
                
                x = x - 1
                GPIO.output(leds[x], False)
                if Game.r > 1:
                    x = x - 1
                    GPIO.output(leds[x], False)
                if Game.r > 2:
                    x = x - 1
                    GPIO.output(leds[x], False)
                if x < 0:
                    mixer.music.stop()
                    grr.play()
                    
                    
                    #Update Image to lose
                    for i in range(0,2):
                        
                        GUI.screen(2)
                        root.update()
                        for i in range(0, 7):
                            GPIO.output(leds[i], True)
                            sleep(0.1)
                            GPIO.output(leds[i], False)
                            sleep(0.1)
                        GUI.screen(3)
                        root.update()
                        for i in range(7, 0, -1):
                            GPIO.output(leds[i], True)
                            sleep(0.1)
                            GPIO.output(leds[i], False)
                            sleep(0.1)
                    GUI.screen(2)
                    root.update()
                    sleep(4)
                    root.destroy()
                    GPIO.cleanup()
                    exit()
                wrong.play()
                GUI.screen(6)
                root.update()
                sleep(1)
                GUI.UpdateQ(1)
                root.update()


#######################################################
