
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
#self means refer to the class its in// initializing family based on last name
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"id": self._generateId(),
            "first_name": "John",
            "last_name": "jackson",
            "age": 33,
            "lucky_numbers": [7, 13, 22]},

            {"id": self._generateId(),
            "first_name": "Jane",
            "last_name": "jackson",
            "age": 35,
            "lucky_numbers": [10, 14, 3]},

            {"id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": "jackson",
            "age": 5,
            "lucky_numbers": [1]}
        ]


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member = {},
        self._members.append(member)



    def delete_member(self, id):
        # fill this method and update the return
        for member in range(len(self._member)):
            if self._member[member]['id'] == id:
                self._members.pop(member)
                return True
        return False 



    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == int(id):
                return member
        return None



    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
