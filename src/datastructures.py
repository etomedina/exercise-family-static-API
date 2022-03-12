
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name, members):
        
        self.last_name = last_name
    # example list of members
        self._members = members

    # def serialize(self):
    #     return{
    #         #"id" : self.id,
    #         "last_name" : self.last_name,
    #         "first_name" : self.first_name,
    #         "age" : self.age,
    #         "lucky_numbers": self.lucky_numbers
    #         }


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        # Capturar info en el endpoint (arhivo app.py)
        # Validar si datos en post corresponden a un miembro (con o sin id)
        # no corresponde, retornamos No corresponde a familiar
        # si corresponde:
        #generar id
        #agregamos a members
        pass

    def delete_member(self, id):
        # fill this method and update the return
        for person in self._members:
            if id == person['id']:
                self._members.remove(person)
                return True
        return None

    def get_member(self, id):
        # fill this method and update the return
        for person in self._members:
            if id == person['id']:
                return person
        return None
        
        




    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
