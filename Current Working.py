###################################
# GUI TEST
###################################
from Tkinter import *
from time import sleep
import RPi.GPIO as GPIO
from pygame import *

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



class Question(object):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        

class Game(Frame):
    def __init__ (self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.currentQuestion = 0



    def init_window(self):
        self.master.title("GUI")
        Game.question = Label(root, image = self.currentQuestion.question)
        Game.question.pack()


    def screen(self, index):
        start = PhotoImage(file = "start.gif") #index value 0
        lose1 = PhotoImage(file = "lose.gif") #index value 1
        lose2 = PhotoImage(file = "background.gif")# 2
        win1 = PhotoImage(file = "win.gif")# 3
        win2 = PhotoImage(file = "background.gif") # 4
        correct = PhotoImage(file = "right.gif") # 5
        wrong = PhotoImage(file = "wrong.gif") # 6
        screenArray = [win1, win2, lose1, lose2, start, correct, wrong]
        Game.img = screenArray[index]
        Game.question.config(image = Game.img)
        Game.question.image = Game.img
        
    def setQuestion(self):
        Game.img = self.currentQuestion.question
        Game.question.config(image = Game.img)
        Game.question.image = Game.img
    
    def createQuestions(self):
        img1 = PhotoImage(file = "q1.gif")
        img2 = PhotoImage(file = "q2.gif")
        img3 = PhotoImage(file = "q3.gif")
        img4 = PhotoImage(file = "q4.gif")
        img5 = PhotoImage(file = "q5.gif")
        img6 = PhotoImage(file = "q6.gif")
        img7 = PhotoImage(file = "q7.gif")
        img8 = PhotoImage(file = "q8.gif")
        Game.q1 = Question(img1, 0)
        Game.q2 = Question(img2, 1)
        Game.q3 = Question(img3, 2)
        Game.q4 = Question(img4, 3)
        Game.q5 = Question(img5, 4)
        Game.q6 = Question(img6, 5)
        Game.q7 = Question(img7, 6)
        Game.q8 = Question(img8, 7)

    def imageDisplay(self):
        questions = [Game.q1, Game.q2, Game.q3, Game.q4, Game.q5, Game.q6, Game.q7, Game.q8]
        self.currentQuestion = questions[Game.a]
        

    def play(self):
        Game.a = 0
        self.createQuestions()
        self.imageDisplay()
        self.init_window()
        self.setQuestion()
        self.screen(4)

    def UpdateQ(self, value):
        Game.a += value
        self.imageDisplay()
        self.setQuestion()
        
        

root = Tk()
root.overrideredirect(1)
root.geometry("800x480")
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
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



while(True):
    main.play(-1)
    pressed = False
    while (not pressed):
        for i in range (len(button)):
            while (GPIO.input(button[i]) == True):
                pressed = True
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
            
            
            if x == 0:
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
            else:
                
                x = x - 1
                GPIO.output(leds[x], False)
                wrong.play()
                GUI.screen(6)
                root.update()
                sleep(1)
                GUI.UpdateQ(-1)
                root.update()


#######################################################
