from contacts.entity import Entity
from contacts.service import Service
class Controller:
    def __init__(self):
        self.service = Service()

    def register(self, name, phone, email, addr):
        entity = Entity()
        entity.name =name
        entity.phone = phone
        entity.email= email
        entity.addr = addr

        self.service.add_contact(entity)

    def list(self):
        return self.service.get_contacts()

    def remove(self, name):
        self.service.del_contact(name)

