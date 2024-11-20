import unittest
from Game import Game
import tkinter as tk
"""
This class is used to test the initialisation, 
room creation and purchasing functions in Game
"""

class TestGame(unittest.TestCase):
    def setUp(self):
        """
            Set up the test environment, create a Game instance.
        :return: None
        """
        self.root = tk.Tk()
        self.game = Game(self.root)

    def test_initialization(self):
        """
            Test if the game initializes correctly with rooms and player.
        :return: None
        """
        self.assertIsNotNone(self.game.currentRoom, "Current room should not be None after initialization")
        self.assertEqual(len(self.game.bag), 0, "Bag should be empty initially")

    def test_room_navigation(self):
        """
            Test room navigation functionality.
            Suppose we know that the exit from the forest is a cave
        :return: None
        """
        self.game.currentRoom = self.game.forest
        self.game.doGoCommand("east")
        self.assertEqual(self.game.currentRoom.name, "cave", "Should navigate to cave from forest")

    def test_item_purchase(self):
        """
            Test the item purchase functionality.
            Assuming there is a shop in cave1
            :return: None
        """
        self.game.currentRoom = self.game.cave1
        self.game.buy_flag = True
        self.game.items_lst = ['Compass', 'Flashlight']
        self.game.buy_fun(self.game.items_lst, ('buy', 'compass'))
        self.assertIn('Compass', self.game.bag, "Compass should be in the bag after purchase")

    def test_quit_game(self):
        """
            Test the game quit functionality.
            Simulate a quit command
            :return: None
        """
        quit_flag = self.game.processCommand(("QUIT", None))
        self.assertTrue(quit_flag, "Game should quit after receiving QUIT command")

if __name__ == '__main__':
    unittest.main()