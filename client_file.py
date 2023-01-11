# ● Client
# ○ Properties:
# ■ id
# ■ full_name
# ■ age
# ■ id_no
# ■ phone_number
from model.parent_file import ParentModel


class ClientModel(ParentModel):

        def __init__(self, id: int, full_name: str, age: int, id_no: int, phone_number: int):
            super(ClientModel, self).__init__(id, full_name, age, id_no)
            self.__phone_number = phone_number
