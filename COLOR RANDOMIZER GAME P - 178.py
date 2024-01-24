from tkinter import *
import random

root = Tk()
root.geometry("500x600")
root.title("Encapsulation")

label_name = Label(root, font = ("Sans", 20), bg = "white")
label_name.place(relx = 0.5, rely = 0.5, anchor = CENTER)

class Game():
    def __init__(self):
        self.__score = 0
        
    def update_game(self):
        self.text = ["WHITE", "BLACK", "ORANGE", "BLUE", "GREEN", "YELLOW", "RED", "PRUPLE", "PINK", "GREY"]
        self.random_number_for_text = random.randint(0, 9)
        
        self.color = ["black", "orange", "blue", "green", "yellow", "red", "purple", "pink", "grey"]
        self.random_number_for_color = random.randint(0, 9)
        
        label_name["text"] = self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]
        
obj1 = Game()

btn = Button(root, text = "Start", command = obj1.update_game, bg = "green", fg = "white", relief = FLAT, padx = 10, pady = 10, font = ("Sans", 10, "bold"))
btn.place(relx = 0.6, rely = 0.7, anchor = CENTER)        

root.mainloop()