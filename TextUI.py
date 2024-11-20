"""
    A simple text based User Interface (UI) for the
    Adventure World game
"""
import time

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

class TextUI:

    def __init__(self,GUI_instance):
        # Nothing to do ...
        self.app=GUI_instance

    def getCommand(self):
        """
            Fetches a command from the console
        :return: a 2-tuple of the form (commandWord, secondWord)
        """
        word1 = None
        word2 = None
        self.app.msg.set_output('>', end='')# print('> ', end='')
        inputLine = self.app.get_command() #input()
        self.app.entry.delete(0, 'end')  # 清空输入框
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

    def typewriter(self,text,delay=0.05):
        """
           typewriter funciton to Displays text to the console more smoothly
        :param text: Text to be displayed
        :return: None
        """
        # for sentence in text:
        for char in text:
            print(char,end='',flush=True)
            time.sleep(delay)
        print(flush=True)  # Line feed after printing all characters

    def printtoTextUI(self, text):
        """
            Displays text to the console
        :param text: Text to be displayed
        :return: None
        """
        self.app.win.update_idletasks()  # 更新GUI
        self.app.msg.set_output(text + '\n')
        # print(text)


    def storyTextUI(self, part):
        """
            Displays text to the console
        :param text: Text to be displayed
        :return: None
        """
        if part == "background":
            print(bgText)
        elif part == "epilogue":
            self.typewriter(endText)





