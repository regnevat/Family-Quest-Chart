"""Class for Character"""
# 1. Standard python libraries
from uuid import uuid4

# 2. Third party modules

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class Character:
    """Character are the player."""
    def __init__(self, username, first_name='', last_name='', email='', points='0', inventory=''):
        """Initialize the character class"""
        self.uuid = uuid4()
        self.username = 'username'
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        # self.birthday = ''
        self.points = 0
        self.inventory = []
        self.quests = []
        self.completed_quests = [[]]
        self.uncompleted_quests = []

    def assign_quest(self, quest, new_day):
        if new_day:
            if len(self.quests):
                self.uncompleted_quests = self.quests
            self.quests = []
        self.quests.append(quest)


    def read_character(self):
        pass

# username
# first name
# last name
# email
# birthdate
# count of points
# inventory
# uuid