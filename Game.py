# candidate number:299167

from Room import Room
from Player import Player
import tkinter as tk
from tkinter import scrolledtext,PhotoImage,Menu,messagebox

"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game.  Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, create an instance of this class and call the "play"
    method.

    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game.  It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage
"""

bgText='''
You are the king of Wakanda,
and your empire has been invaded by outsiders,
and you must defend your kingdom.
So you set out to find The Heart-Shaped Grass that will give you the protection of the Black Panther god Buster.
You need to explore the road in different terrain
deal with the difficulties on the path, 
and get the heart-shaped grass to protect your kingdom'
'''
endText='''
Congratulations!
You finally get the heart-shaped grass and win the protection of the Black Panther God. 
You will return to Wakanda and fight alongside your people. 
Your story continues...
'''

class Game(tk.Frame):
    def __init__(self,win):
        """
            Initialises the GUI and other settings
        """
        super().__init__(master=win)
        win.title('Black Panther')
        win.resizable(False, False)
        # Get screen resolution
        a2 = win.maxsize()
        # print(a2)
        k, g = a2
        win.geometry(f'{int(k * 0.5)}x{int(g * 0.5)}+{int(k * 0.2)}+{int(g * 0.2)}')
        # fixed screen
        win.geometry('700x500')
        win.iconbitmap('img/ic2.ico')

        self.pack(fill=tk.BOTH, expand=1)
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var, width=50)
        self.entry.pack(padx=10, pady=5)
        # Using ScrolledText as output box
        self.msg = scrolledtext.ScrolledText(self, width=90, height=10)
        self.msg.pack(padx=10, pady=5)
        self.entry.bind('<Return>', self.get_command)

        self.background_label = tk.Label(self)
        self.background_label.pack(padx=20, pady=40)
        self.load_background("img/Forest.png")

        # Creating Menu
        menubar = Menu(master=win)
        self.master.config(menu=menubar)

        # Creating settings  Menu
        settings_menu = Menu(menubar, tearoff=0)
        settings_menu.add_command(label="quit", command=self.master.destroy)
        settings_menu.add_command(label="about", command=self.about)
        menubar.add_cascade(label="Settings", menu=settings_menu)

        self.items_lst = ['Compass', 'Flashlight', 'Bandage', 'Map']    #items in the shop
        self.coins=20   #to buy somthing
        self.egg_key=0
        self.createRooms()
        self.currentRoom = self.forest
        self.bag=[]
        self.buy_flag = False
        self.player = Player()  #create Player() object
        #Initialization Text
        with open("log.txt", "w", encoding='utf-8') as file:
            pass
        self.printWelcome()

    def initfun(self):
        """
            Initialises the game
        """
        self.items_lst = ['Compass', 'Flashlight', 'Bandage', 'Map']    #items in the shop
        self.coins=20   #to buy somthing
        self.egg_key=0
        self.createRooms()
        self.currentRoom = self.forest
        self.bag=[]
        with open("log.txt", "w", encoding='utf-8') as file:
            pass
        self.printWelcome()

    def about(self):
        messagebox.showinfo("About", "Written by zxc\nemil:1756956492@qq.com")

    def load_background(self, image_path):
        """
             load background
        :param image_path:
        :return: None
        """
        try:
            bg_image = PhotoImage(file=image_path)
            self.background_label.config(image=bg_image)
            self.background_label.image = bg_image  # Avoid image spamming back
        except tk.TclError as e:
            print(f"Error Image: {e}")

    def change_background(self,room):
        """
            changes the background
        :param room: current room
        :return:
        """
        if room=="cave":
            self.load_background("img/cave.png")
        elif room=="forest":
            self.load_background("img/Forest.png")
        elif room=="cave1":
            self.load_background("img/cave1.png")
        elif room=="cave2":
            self.load_background("img/cave2.png")
        elif room=="lake":
            self.load_background("img/lake.png")
        elif room=="lake1":
            self.load_background("img/lake1.png")
        elif room=="mountain":
            self.load_background("img/mountain.png")
        elif room=="mountain1":
            self.load_background("img/mountain1.png")
        elif room=="mountain2":
            self.load_background("img/mountain2.png")
        elif room=="temple":
            self.load_background("img/temple.png")
        else:
            self.printtoTextUI("error place !")

    def get_command(self, event):
        """

        :param event:
        :return:
        """
        command = self.entry_var.get()
        self.process_command(command)
        self.entry_var.set('')  # clear the entry box

    def process_command(self, command):
        quit_flag=self.processCommand(self.getCommand(command))
        if quit_flag:
            self.master.destroy()

    def getCommand(self, command):
        """
            Fetches a command from the console
        :return: a 2-tuple of the form (commandWord, secondWord)
        """
        word1 = None
        word2 = None
        inputLine = command

        if inputLine != "":
            # #Try to capture error input
            try:
                allWords = inputLine.split()
                word1 = allWords[0]
                if len(allWords) > 1:
                    word2 = allWords[1]
                else:
                    word2 = None
            except IndexError:
                print('Invalid input!!')
            # Just ignore any other words
        return (word1, word2)

    def printtoTextUI(self, text):
        """
            Used to print text to msg
        :param text:
        :return:
        """
        try:
            self.msg.insert(tk.END, text + '\n')
            self.msg.see(tk.END)  # go to bottom
        except tk.TclError as e:
            print(f"Error accessing scrolledtext: {e}")

    def storyTextUI(self, part):
        """
            Displays text to the console
        :param text: Text to be displayed
        :return: None
        """
        if part == "background":
            self.printtoTextUI(bgText)
        elif part == "epilogue":
            self.printtoTextUI(endText)

    def createRooms(self):
        """
            Sets up all room assets
        :return: None
        """
        self.forest = Room("You are Emi Forest",'forest')
        self.mountain = Room("The entrance to Tianguan Mountain",'mountain')
        self.mountain1 = Room("Inside of the Tianguan Cave",'mountain1')
        self.mountain2 = Room("Deep in the Tianguan Cave",'mountain2')
        self.lake = Room("at the mouth of Xinqi Lake",'lake')
        self.lake1 = Room("at the the bottom of the lake",'lake1')
        self.cave = Room("in the bat cave",'cave')
        self.cave1 = Room("in the Underground cavern",'cave1')
        self.cave2 = Room("in the Underground mine",'cave2')
        self.temple = Room("in the Geocentric temple",'temple')

        self.forest.setExit("east", self.cave)
        self.forest.setExit("south", self.mountain)
        self.forest.setExit("west", self.lake)
        self.cave.setExit("south", self.cave1)
        self.cave.setExit("west", self.forest)
        self.cave1.setExit("south", self.cave2)
        self.cave1.setExit("north", self.cave)
        self.cave2.setExit("west", self.mountain2)
        self.cave2.setExit("north", self.cave1)
        self.mountain.setExit("south", self.mountain1)
        self.mountain.setExit("north", self.forest)
        self.mountain1.setExit("south", self.mountain2)
        self.mountain1.setExit("north", self.mountain)
        self.mountain2.setExit("south", self.temple)
        self.mountain2.setExit("north", self.mountain1)
        self.mountain2.setExit("east", self.cave2)
        self.mountain2.setExit("west", self.lake1)
        self.lake.setExit("east", self.forest)
        self.lake.setExit("south", self.lake1)
        self.lake1.setExit("east", self.mountain2)
        self.lake1.setExit("north", self.lake)

    def printWelcome(self):
        """
            Displays a welcome message
        :return:
        """
        # self.player.input_name()
        self.printtoTextUI(f'Hi! {self.player.name}')
        # self.typewriter("Welcome to the Black Panther!")
        self.storyTextUI("background")
        # self.typewriter("You are lost. You are alone. You wander")
        # self.typewriter("around the deserted complex.")
        self.printtoTextUI("")
        self.printtoTextUI(f'Your current position is:{self.currentRoom.name}')
        self.printtoTextUI(f'Your command words are: {self.showCommandWords()}')
        self.printtoTextUI("You have four directions to choose:['south', 'west', 'east', 'north']")

    def showCommandWords(self):
        """
            Show a list of available commands
        :return: None
        """
        return ['help', 'go', 'quit','restart', 'pickup', 'shop', 'bag']

    def show_items(self, itme_lst):
        """
            Show all items
        :return: None
        """
        for itme in itme_lst:
            self.printtoTextUI(itme)
        self.printtoTextUI('')

    def openshop(self,item_lst):
        """
            For the trading of goods by wandering merchants
        :return: None
        """
        self.printtoTextUI("Welcome to the shop! Here's something you can use.")
        self.printtoTextUI("Items:")
        self.show_items(item_lst)

    def buy_fun(self,items,buycommand):
        """
            Use this function to pick up items
        :param command: import the command to buy items
        :return: None
        """
        self.printtoTextUI('You can buy something you want:')
        self.printtoTextUI("Please type in a structure like this:'buy map'")
        # Try to capture error type
        finished = False
        try:
            command = buycommand  # Returns a 2-tuple
            self.player.save(command)
        except TypeError:
            print('Warning: TypeError!')
        if (finished == False):
            if command[0] == 'buy':
                if command[1] == 'map':
                    self.bag.append("Map")
                    items.remove("Map")
                    self.printtoTextUI('Deal! You bought a Map')
                    #display the other items
                    self.printtoTextUI("Items:")
                    self.show_items(items)
                elif command[1] == 'compass':
                    self.bag.append("Compass")
                    items.remove("Compass")
                    self.printtoTextUI('Deal! You bought a Compass')
                    self.printtoTextUI("Items:")
                    self.show_items(items)
                elif command[1] == 'flashlight':
                    self.bag.append("Flashlight")
                    items.remove("Flashlight")
                    self.printtoTextUI('Deal! You bought a Flashlight')
                    self.printtoTextUI("Items:")
                    self.show_items(items)
                elif command[1] == 'bandage':
                    self.bag.append("Bandage")
                    items.remove("Bandage")
                    self.printtoTextUI('Deal! You bought a Bandage')
                    self.printtoTextUI("Items:")
                    self.show_items(items)
                else:
                    self.printtoTextUI('There is no such item here.')
            elif command[0] == 'quit':
                finished = True
                self.buy_flag = False
                self.printtoTextUI('You left the store.')
            else:
                self.printtoTextUI("Error! Your command words are:'quit','buy'")


    def pickfun(self,secondWord):
        """
            Use this function to pick up items
        :param secondWord: Do player want to pick or drop
        :return: None
        """
        if secondWord == 'y':
            if self.currentRoom.name=="lake1":
                if not self.bag:
                    self.printtoTextUI("Congratulations! You found the temple key.")
                    self.bag.append("the temple key")
                else:
                    for itme in self.bag:
                        if itme == 'the temple key':
                            self.printtoTextUI("You already have the key")
                        else:
                            self.printtoTextUI("Congratulations! You found the temple key.")
                            self.bag.append("the temple key")
            elif self.currentRoom.name=="temple":
                for itme in self.bag:
                    if itme == 'the heart-shaped grass':
                        self.printtoTextUI("You already have the heart-shaped grass")
                    else:
                        self.printtoTextUI("Congratulations! You finally found the heart-shaped grass.")
                        self.bag.append("the heart-shaped grass")
                        self.storyTextUI('epilogue')
                        break

        elif secondWord == 'n':
            self.printtoTextUI("The item is still here.")
        else:
            self.printtoTextUI("Don't know what you mean,please type:'pickup y or n'")

    def openbag(self):
        """
            Use this function to view the items in your backpack
        :return: None
        """
        self.printtoTextUI("You have:")
        for itme in self.bag:
            self.printtoTextUI(f'{itme}')
        self.printtoTextUI('')

    def temple_key_check(self,nextR):
        """
            Use this function to check the key in your backpack
        :param nextR:to judge the next room
        :return: key: boolen
        """
        if nextR.name == "temple":
            for itme in self.bag:
                if itme == 'the temple key':
                    temple_Doorlock = True
                    self.printtoTextUI("You used the temple key to unlock the door, and it slowly opened.")
                    return temple_Doorlock
                else:
                    self.printtoTextUI('The front door of the temple is closed and you need to find the key.1')

    def egg(self):
        """
            Game egg
        :return: None
        """
        self.printtoTextUI('''
          ________                      ___________               
         /  _____/_____    _____   ____ \_   _____/  ____   ____  
        /   \  ___\__  \  /     \_/ __ \ |    __)_  / ___\ / ___\ 
        \    \_\  \/ __ \|  Y Y  \  ___/ |        \/ /_/  > /_/  >
         \______  (____  /__|_|  /\___  >_______  /\___  /\___  / 
                \/     \/      \/     \/        \//_____//_____/ 
        ''')
        self.printtoTextUI('''
            T'Challa, or Black Panther, created by editor Stan Lee and comic book artist Jack Kirby, 
            was the first black African-American hero to debut in a mainstream American comic book company. 
            A graduate of Oxford University in England, 
            he succeeded Black Panther as King of Wakanda after the death of his father, 
            T'Chaka, and later joined the Avengers.
            Like his best friend Iron Man, 
            T'Chaka is a highly intelligent scientist 
            who often develops a variety of high-tech weaponry for members of the Avengers.
        ''')

    def processCommand(self, command):
        """
            Process a command from the TextUI
        :param command: a 2-tuple of the form (commandWord, secondWord)
        :return: True if the game has been quit, False otherwise
        """
        commandWord, secondWord = command
        # save the direction or moves
        self.player.save(command)
        # self.player.save(secondWord)

        if commandWord != None:
            commandWord = commandWord.upper()

        wantToQuit = False
        if self.buy_flag:
            self.buy_fun(self.items_lst,command)
        else:
            if commandWord == "HELP":
                self.doPrintHelp()
            elif commandWord == "GO":
                self.doGoCommand(secondWord)
            elif commandWord == "QUIT":
                wantToQuit = True
            elif commandWord == "PICKUP":
                if self.currentRoom.name == "lake1":
                    self.pickfun(secondWord)
                elif self.currentRoom.name == "temple":
                    self.pickfun(secondWord)
                else:
                    self.printtoTextUI("There's nothing to pick up here.")
            elif commandWord == "SHOP" and secondWord == None:
                if self.currentRoom.name=="cave1":
                    self.buy_flag=True
                    self.openshop(self.items_lst)
                else:
                    self.printtoTextUI("There are no shops here.")
            elif commandWord == "BAG" and secondWord == None:
                self.openbag()
            elif commandWord == "RESTART" and secondWord == None:
                self.initfun()
            else:
                self.printtoTextUI("Don't know what you mean")
        return wantToQuit

    def doPrintHelp(self):
        """
            Display some useful help text
        :return: None
        """
        self.printtoTextUI("If you want to go somewhere,you have four directions to choose:['south', 'west', 'east', 'north']")
        self.printtoTextUI("Please type in a structure like this:'go south' ")
        self.printtoTextUI("")
        self.printtoTextUI(f'Your command words are: {self.showCommandWords()}')

    def doGoCommand(self, secondWord):
        """
            Performs the GO command
        :param secondWord: the direction the player wishes to travel in
        :return: None
        """
        temple_Doorlock = False
        if secondWord == None:
            # Missing second word ...
            self.printtoTextUI("Go where?")
            return
        #save the room name
        self.player.save(self.currentRoom.name)
        nextRoom = self.currentRoom.getExit(secondWord)
        # print(nextRoom.name)
        # print(nextRoom)     #try to print a object  <Room.Room object at 0x0000027C61D73888>
        if nextRoom == None:
            if self.currentRoom.name == "temple" :
                if self.egg_key < 3:
                    self.egg_key+=1
                else:
                    self.egg()
            self.printtoTextUI("There is no road!")
        else:
            if self.currentRoom.name == "mountain2":
                if nextRoom.name == "temple":

                    # If the current room is m2 and the next room is temp, the key is judged.
                    if self.temple_key_check(nextRoom):
                        self.currentRoom = nextRoom
                    else:
                        self.printtoTextUI("The front door of the temple is closed and you need to find the key.")
                # If the current room is m2 but the next room is not temp, Come and go as you please.
                else:
                    self.currentRoom = nextRoom
            # If the current room is not m2, Come and go as you please.
            else:
                self.currentRoom = nextRoom
            self.change_background(self.currentRoom.name)
            self.printtoTextUI(self.currentRoom.getLongDescription())
            self.printtoTextUI(self.currentRoom.getmoredetail())     # Fetch a more description


def main():
    root = tk.Tk()
    game = Game(root)
    game.mainloop()
if __name__ == "__main__":
    main()