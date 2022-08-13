"""Class for QuestGiver"""
# 1. Standard python libraries
from uuid import uuid4

# 2. Third party modules

# 3. Family modules

# 4. Local modules

__copyright__ = "(C) Copyright Aaron Jones 2022"
__license__ = "All rights reserved"


class QuestGiver:
    """Quest giver assigns to quests to characters."""
    def __init__(self, directory):
        """Initialize the quest class."""
        self.characters = []
        self.quests = []
        self.directory = directory

        self.roles = []


    def read_all_quests(self):
        pass

    def read_all_characters(self):
        pass

    def assign_all_quests(self):
        # Assign mentors by birthdate
        # Determine quests to assign based on priority
        # Assign the quests
        pass

    def compute_data(self):
        self.read_all_quests()
        self.read_all_characters()
        self.assign_all_quests()
