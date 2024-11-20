"""
    This class is used to store
    and call the player's data
"""
import time

class Player:
    def __init__(self):
        """
            Initialises the player data
        """
        self.name=''
    def input_name(self):
        """
            Importing names into the save.txt and storing them
        :return: None
        """
        # Try to capture error type
        try:
            self.name = input("What is your name ? \n>")
            with open("log.txt", "w",encoding='utf-8') as file:
                file.write('name:')
                file.write(self.name)
                file.write('\n')
        except TypeError:
            file.write('Warning: TypeError!')
            print('Warning: TypeError!')
    def save(self,text):
        """
            Save all player's data
        :param text to save
        :return: None
        """
        with open("log.txt", "a",encoding='utf-8') as file:
            file.write('N_time:')
            file.write(time.ctime())
            file.write('\t data:')
            #Try to capture error type
            try:
                file.writelines(str(text))
            except TypeError:
                file.write('Warning: TypeError!')
                print('Warning: TypeError!')
            file.write('\n')


