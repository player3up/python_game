"""
    Create a room described "description". Initially, it has
    no exits. 'description' is something like 'kitchen' or
    'an open court yard'
"""

class Room:
    def __init__(self, description,name):
        """
            Constructor method
        :param description: text description for this room
        """
        self.description = description
        self.name = name
        self.exits = {}     # Dictionary

    # def __str__(self):        #use str try to print key and value
    #     return ', '.join(f"{k}: {v.name}" for k, v in self.exits.items())            #'\n'.join(f"{k}: {v.name}" for k, v in self.exits.items())

    def setExit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room)
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def getShortDescription(self):
        """
            Fetch a short text description
        :return: text description
        """
        return self.description

    def getLongDescription(self):
        """
            Fetch a longer description including available exits
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.getExits()} '

    def getmoredetail(self):
        """
            Fetch a more description like: NPC,Items
        :return: text description
        """
        if self.name=='cave1':
            return 'Detail: There is a wandering merchant here, you can go to him to buy some props'
        elif self.name=='lake1':
            return 'Detail: There is something in here. Do you want to pick it up?(y/n)'
        elif self.name=='temple':
            return 'Detail: There is something shiny up ahead. Do you want to pick it up?(y/n)'
        else:
            return 'Detail: Nothing'

    def getExits(self):
        """
            Fetch all available exits as a list
        :return: list of all available exits
        """
        allExits = self.exits.keys()
        return list(allExits)

    def getExit(self, direction):
        """
            Fetch an exit in a specified direction
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            # print(self.exits.get(direction,'no'))
            return self.exits[direction]
        else:
            return None
