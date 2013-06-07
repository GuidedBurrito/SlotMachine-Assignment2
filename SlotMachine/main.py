from Tkinter import *

import random

#create the MyApp Class
class MySlotMachine:
    #Background and buttons are placed on the screen
    def __init__(self, parent):
        self.myParent = parent
        #creates a frame
        self.myContainer1 = Frame(parent)
        #show it on the screen
        self.myContainer1.pack()
        
        #Sets the Background
        self.BackgroundImage = PhotoImage(file="slot-machine.gif")
        self.BackgroundLabel = Label(self.myContainer1)
        self.BackgroundLabel.configure(image = self.BackgroundImage, compound=CENTER)
        self.BackgroundLabel.pack()
        
        #Sets the spin buttons image
        SpinButton = PhotoImage(file="SpinButton.gif")
        
        #the SpinButton attributes
        self.SpinButton = Button(self.myContainer1)
        self.SpinButton.configure(image=SpinButton, height=50, width=60)
        #display SpinButton
        self.SpinButton.pack()
        self.SpinButton.place(x=315, y=340)
        #Bind SpinButton with SpinButtonClick
        PlayerCredits = 500
        PlayerBet = 0
        self.SpinButton.bind("<Button-1>", self.SpinButtonClick)
        self.SpinButton.image = SpinButton
        
        #Sets the reset buttons image
        ResetButton = PhotoImage(file="Reset.gif")
        
        #the ResetButton attributes
        self.ResetButton = Button(self.myContainer1)
        self.ResetButton.configure(image=ResetButton, height=35, width=35 )
        #display ResetButton
        self.ResetButton.pack()
        self.ResetButton.place(x=40, y=350)
        #Bind ResetButton with ResetButtonClick
        self.ResetButton.bind("<Button-1>", self.ResetButtonClick)
        self.ResetButton.image = ResetButton
        
        #Sets the bet one image
        BetOneButton = PhotoImage(file="BetOne.gif")
        
        #the BetOneButton attributes
        self.BetOneButton = Button(self.myContainer1)
        self.BetOneButton.configure(image=BetOneButton, height=35, width=35 )
        #display BetOneButton
        self.BetOneButton.pack()
        self.BetOneButton.place(x=155, y=350)
        #Bind BetOneButton with BetOneButtonClick
        self.BetOneButton.bind("<Button-1>", self.BetOneButtonClick)
        self.BetOneButton.image = BetOneButton

        #Sets the bet tens button image
        BetTenButton = PhotoImage(file="BetTen.gif")
        
        #the BetTenButton attributes
        self.BetTenButton = Button(self.myContainer1)
        self.BetTenButton.configure(image=BetTenButton, height=35, width=35 )
        #display BetTenButton
        self.BetTenButton.pack()
        self.BetTenButton.place(x=128, y=403)
        #Bind BetTenButton with BetTenButtonClick
        self.BetTenButton.bind("<Button-1>", self.BetTenButtonClick)
        self.BetTenButton.image = BetTenButton
        
        #Sets the betfive buttons image
        BetFiveButton = PhotoImage(file="BetFive.gif")
        
        #the BetFiveButton attributes
        self.BetFiveButton = Button(self.myContainer1)
        self.BetFiveButton.configure(image=BetFiveButton, height=35, width=35 )
        #display BetFiveButton
        self.BetFiveButton.pack()
        self.BetFiveButton.place(x=67, y=403)
        #Bind BetFiveButton with BetFiveButtonClick
        self.BetFiveButton.bind("<Button-1>", self.BetFiveButtonClick)
        self.BetFiveButton.image = BetFiveButton
        
        #Sets the bet fifty buttons image
        BetFiftyButton = PhotoImage(file="BetFifty.gif")
        
        #the BetFiftyButton attributes
        self.BetFiftyButton = Button(self.myContainer1)
        self.BetFiftyButton.configure(image=BetFiftyButton, height=35, width=35 )
        #display BetFiftyButton
        self.BetFiftyButton.pack()
        self.BetFiftyButton.place(x=188, y=403)
        #Bind BetFiftyButton with BetFiftyButtonClick
        self.BetFiftyButton.bind("<Button-1>", self.BetFiftyButtonClick)
        self.BetFiftyButton.image = BetFiftyButton
        
        #Sets the Max Bet Buttons image
        BetMaxButton = PhotoImage(file="BetMax.gif")
        
        #the BetMaxButton attributes
        self.BetMaxButton = Button(self.myContainer1)
        self.BetMaxButton.configure(image=BetMaxButton, height=35, width=35 )
        #display BetMaxButton
        self.BetMaxButton.pack()
        self.BetMaxButton.place(x=214, y=350)
        #Bind BetMaxButton with BetMaxButtonClick
        self.BetMaxButton.bind("<Button-1>", self.BetMaxButtonClick)
        self.BetMaxButton.image = BetMaxButton
        
        #Sets and displays the Bet Text Label Text and Colour      
        self.BetTextLabel = Label(self.myContainer1)
        self.BetTextLabel.configure(text = (PlayerBet), fg="#FF4500", bg="#000000", font="DS_DIGI.TTF")
        self.BetTextLabel.pack()
        self.BetTextLabel.place(x=170, y=260)
        
        #sets and displays the Credit Text label text and colour
        self.CreditTextLabel = Label(self.myContainer1)
        self.CreditTextLabel.configure(text = (PlayerCredits), fg="#FF4500", bg="#000000", font="DS_DIGI.TTF")
        self.CreditTextLabel.pack()
        self.CreditTextLabel.place(x=100, y=260)
    
    #When the spin button is clicked
    def SpinButtonClick(self, event): 
        
        #Calls the random spin function
        Fruit_Reel = self.SpinReels()
    
    
        #Gets the values from the spin and assigns an image to the value. Image is then posted to the screen
        
        #Image for the first reel
        if Fruit_Reel[0] >= 1 and Fruit_Reel[0] <=26:
            Reel1Image = PhotoImage(file="Blank.gif")
            self.Reel1Label = Label(self.myContainer1)
            self.Reel1Label.configure(image = Reel1Image)
            self.Reel1Label.pack()
            self.Reel1Label.place(x=60, y=145)
            self.Reel1Label.image = Reel1Image     
        elif Fruit_Reel[0] >= 27 and Fruit_Reel[0] <=36:
            Reel1Image = PhotoImage(file="Strawberry.gif")
            self.Reel1Label = Label(self.myContainer1)
            self.Reel1Label.configure(image = Reel1Image)
            self.Reel1Label.pack()
            self.Reel1Label.place(x=60, y=145)
            self.Reel1Label.image = Reel1Image
        elif Fruit_Reel[0] >= 37 and Fruit_Reel[0] <=45:
            Reel1Image = PhotoImage(file="Apple.gif")
            self.Reel1Label = Label(self.myContainer1)
            self.Reel1Label.configure(image = Reel1Image)
            self.Reel1Label.pack()
            self.Reel1Label.place(x=60, y=145)
            self.Reel1Label.image = Reel1Image
        elif Fruit_Reel[0] >= 46 and Fruit_Reel[0] <=53:
            Reel1Image = PhotoImage(file="HorseShoe.gif")
            self.Reel1Label = Label(self.myContainer1)
            self.Reel1Label.configure(image = Reel1Image)
            self.Reel1Label.pack()
            self.Reel1Label.place(x=60, y=145)
            self.Reel1Label.image = Reel1Image
        elif Fruit_Reel[0] >= 54 and Fruit_Reel[0] <=58:
            Reel1Image = PhotoImage(file="Clover.gif")
            self.Reel1Label = Label(self.myContainer1)
            self.Reel1Label.configure(image = Reel1Image)
            self.Reel1Label.pack()
            self.Reel1Label.place(x=60, y=145)
            self.Reel1Label.image = Reel1Image
        elif Fruit_Reel[0] >= 59 and Fruit_Reel[0] <=61:
            Reel1Image = PhotoImage(file="Bell.gif")
            self.Reel1Label = Label(self.myContainer1)
            self.Reel1Label.configure(image = Reel1Image)
            self.Reel1Label.pack()
            self.Reel1Label.place(x=60, y=145)
            self.Reel1Label.image = Reel1Image
        elif Fruit_Reel[0] >= 62 and Fruit_Reel[0] <= 63:
            Reel1Image = PhotoImage(file="Diamond.gif")
            self.Reel1Label = Label(self.myContainer1)
            self.Reel1Label.configure(image = Reel1Image)
            self.Reel1Label.pack()
            self.Reel1Label.place(x=60, y=145)
            self.Reel1Label.image = Reel1Image
        elif Fruit_Reel[0] == 64:
            Reel1Image = PhotoImage(file="Seven.gif")
            self.Reel1Label = Label(self.myContainer1)
            self.Reel1Label.configure(image = Reel1Image)
            self.Reel1Label.pack()
            self.Reel1Label.place(x=60, y=145)
            self.Reel1Label.image = Reel1Image
           
        #Image for reel 2 
        if Fruit_Reel[1] >= 1 and Fruit_Reel[1] <=26:
            Reel2Image = PhotoImage(file="Blank.gif")
            self.Reel2Label = Label(self.myContainer1)
            self.Reel2Label.configure(image = Reel2Image)
            self.Reel2Label.pack()
            self.Reel2Label.place(x=170, y=145)
            self.Reel2Label.image = Reel2Image     
        elif Fruit_Reel[1] >= 27 and Fruit_Reel[1] <=36:
            Reel2Image = PhotoImage(file="Strawberry.gif")
            self.Reel2Label = Label(self.myContainer1)
            self.Reel2Label.configure(image = Reel1Image)
            self.Reel2Label.pack()
            self.Reel2Label.place(x=170, y=145)
            self.Reel2Label.image = Reel2Image
        elif Fruit_Reel[1] >= 37 and Fruit_Reel[1] <=45:
            Reel2Image = PhotoImage(file="Apple.gif")
            self.Reel2Label = Label(self.myContainer1)
            self.Reel2Label.configure(image = Reel2Image)
            self.Reel2Label.pack()
            self.Reel2Label.place(x=170, y=145)
            self.Reel2Label.image = Reel2Image
        elif Fruit_Reel[1] >= 46 and Fruit_Reel[1] <=53:
            Reel2Image = PhotoImage(file="HorseShoe.gif")
            self.Reel2Label = Label(self.myContainer1)
            self.Reel2Label.configure(image = Reel2Image)
            self.Reel2Label.pack()
            self.Reel2Label.place(x=170, y=145)
            self.Reel2Label.image = Reel2Image
        elif Fruit_Reel[1] >= 54 and Fruit_Reel[1] <=58:
            Reel2Image = PhotoImage(file="Clover.gif")
            self.Reel1Label = Label(self.myContainer1)
            self.Reel2Label.configure(image = Reel2Image)
            self.Reel2Label.pack()
            self.Reel2Label.place(x=170, y=145)
            self.Reel2Label.image = Reel2Image
        elif Fruit_Reel[1] >= 59 and Fruit_Reel[1] <=61:
            Reel2Image = PhotoImage(file="Bell.gif")
            self.Reel2Label = Label(self.myContainer1)
            self.Reel2Label.configure(image = Reel2Image)
            self.Reel2Label.pack()
            self.Reel2Label.place(x=170, y=145)
            self.Reel2Label.image = Reel2Image
        elif Fruit_Reel[1] >= 62 and Fruit_Reel[1] <= 63:
            Reel2Image = PhotoImage(file="Diamond.gif")
            self.Reel2Label = Label(self.myContainer1)
            self.Reel2Label.configure(image = Reel2Image)
            self.Reel2Label.pack()
            self.Reel2Label.place(x=170, y=145)
            self.Reel2Label.image = Reel2Image
        elif Fruit_Reel[1] == 64:
            Reel2Image = PhotoImage(file="Seven.gif")
            self.Reel2Label = Label(self.myContainer1)
            self.Reel2Label.configure(image = Reel2Image)
            self.Reel2Label.pack()
            self.Reel2Label.place(x=170, y=145)
            self.Reel2Label.image = Reel2Image
        
        #Image for reel 3           
        if Fruit_Reel[2] >= 1 and Fruit_Reel[2] <=26:
            Reel3Image = PhotoImage(file="Blank.gif")
            self.Reel3Label = Label(self.myContainer1)
            self.Reel3Label.configure(image = Reel3Image)
            self.Reel3Label.pack()
            self.Reel3Label.place(x=270, y=145)
            self.Reel3Label.image = Reel3Image     
        elif Fruit_Reel[2] >= 27 and Fruit_Reel[2] <=36:
            Reel3Image = PhotoImage(file="Strawberry.gif")
            self.Reel3Label = Label(self.myContainer1)
            self.Reel3Label.configure(image = Reel3Image)
            self.Reel3Label.pack()
            self.Reel3Label.place(x=270, y=145)
            self.Reel3Label.image = Reel3Image
        elif Fruit_Reel[2] >= 37 and Fruit_Reel[2] <=45:
            Reel3Image = PhotoImage(file="Apple.gif")
            self.Reel3Label = Label(self.myContainer1)
            self.Reel3Label.configure(image = Reel3Image)
            self.Reel3Label.pack()
            self.Reel3Label.place(x=270, y=145)
            self.Reel3Label.image = Reel3Image
        elif Fruit_Reel[2] >= 46 and Fruit_Reel[2] <=53:
            Reel3Image = PhotoImage(file="HorseShoe.gif")
            self.Reel3Label = Label(self.myContainer1)
            self.Reel3Label.configure(image = Reel3Image)
            self.Reel3Label.pack()
            self.Reel3Label.place(x=270, y=145)
            self.Reel3Label.image = Reel3Image
        elif Fruit_Reel[2] >= 54 and Fruit_Reel[2] <=58:
            Reel3Image = PhotoImage(file="Clover.gif")
            self.Reel3Label = Label(self.myContainer1)
            self.Reel3Label.configure(image = Reel3Image)
            self.Reel3Label.pack()
            self.Reel3Label.place(x=270, y=145)
            self.Reel3Label.image = Reel3Image
        elif Fruit_Reel[2] >= 59 and Fruit_Reel[2] <=61:
            Reel3Image = PhotoImage(file="Bell.gif")
            self.Reel3Label = Label(self.myContainer1)
            self.Reel3Label.configure(image = Reel3Image)
            self.Reel3Label.pack()
            self.Reel3Label.place(x=270, y=145)
            self.Reel3Label.image = Reel3Image
        elif Fruit_Reel[2] >= 62 and Fruit_Reel[2] <= 63:
            Reel3Image = PhotoImage(file="Diamond.gif")
            self.Reel3Label = Label(self.myContainer1)
            self.Reel3Label.configure(image = Reel3Image)
            self.Reel3Label.pack()
            self.Reel3Label.place(x=270, y=145)
            self.Reel3Label.image = Reel3Image
        elif Fruit_Reel[2] == 64:
            Reel3Image = PhotoImage(file="Seven.gif")
            self.Reel3Label = Label(self.myContainer1)
            self.Reel3Label.configure(image = Reel3Image)
            self.Reel3Label.pack()
            self.Reel3Label.place(x=270, y=145)
            self.Reel3Label.image = Reel3Image

    #The random spin function
    def SpinReels(self):
            Bet_Line = [" "," "," "]
            Outcome = [0,0,0]
    
            # Spin those reels
            for spin in range(3):
                Outcome[spin] = random.randrange(1,65,1)
                # Spin those Reels!
                if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
                    Bet_Line[spin] = "Blank"
                if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
                    Bet_Line[spin] = "Strawbeery"
                if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
                    Bet_Line[spin] = "Apple"
                if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
                    Bet_Line[spin] = "HorseShoe"
                if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
                    Bet_Line[spin] = "Clover"
                if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
                    Bet_Line[spin] = "Bell"
                if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
                    Bet_Line[spin] = "Diamond"  
                if Outcome[spin] == 64:                         # 1.56%  Chance
                    Bet_Line[spin] = "Seven"    
            return Outcome
    
    #Button that closes the window
    def ResetButtonClick(self, event):
        self.myParent.destroy()
     
    #Changes the bet value    
    def BetOneButtonClick(self, event):
        self.BetTextLabel.configure(text = "       ", bg="#000000")
        PlayerBet = 1
        self.BetTextLabel = Label(self.myContainer1)
        self.BetTextLabel.configure(text = (PlayerBet), fg="#FF4500", bg="#000000", font="DS_DIGI.TTF")
        self.BetTextLabel.pack()
        self.BetTextLabel.place(x=170, y=260)

    #Changes the bet value
    def BetFiveButtonClick(self, event):
        self.BetTextLabel.configure(text = "       ", bg="#000000")
        PlayerBet = 5
        self.BetTextLabel = Label(self.myContainer1)
        self.BetTextLabel.configure(text = (PlayerBet), fg="#FF4500", bg="#000000", font="DS_DIGI.TTF")
        self.BetTextLabel.pack()
        self.BetTextLabel.place(x=170, y=260)
    
    #Changes the bet value
    def BetTenButtonClick(self, event):
        self.BetTextLabel.configure(text = "       ", bg="#000000")
        PlayerBet = 10
        self.BetTextLabel = Label(self.myContainer1)
        self.BetTextLabel.configure(text = (PlayerBet), fg="#FF4500", bg="#000000", font="DS_DIGI.TTF")
        self.BetTextLabel.pack()
        self.BetTextLabel.place(x=170, y=260)
    
    #Changes the bet value
    def BetFiftyButtonClick(self, event):
        self.BetTextLabel.configure(text = "       ", bg="#000000")
        PlayerBet = 50
        self.BetTextLabel = Label(self.myContainer1)
        self.BetTextLabel.configure(text = (PlayerBet), fg="#FF4500", bg="#000000", font="DS_DIGI.TTF")
        self.BetTextLabel.pack()
        self.BetTextLabel.place(x=170, y=260)
    
    #Changes the bet value
    def BetMaxButtonClick(self, event):
        self.BetTextLabel.configure(text = "       ", bg="#000000")
        PlayerBet = 100
        self.BetTextLabel = Label(self.myContainer1)
        self.BetTextLabel.configure(text = (PlayerBet), fg="#FF4500", bg="#000000", font="DS_DIGI.TTF")
        self.BetTextLabel.pack()
        self.BetTextLabel.place(x=170, y=260)
        
    
#Main function    
def main():
    #create a top-level window
    root = Tk()
    #call the MySlotmachine class
    myapp = MySlotMachine(root)
    #execute the mainloop method of the "root" object
    root.mainloop()

if __name__ == "__main__": main()