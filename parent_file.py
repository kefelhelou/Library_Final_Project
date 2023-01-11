# ● Client
# ○ Properties:
# ■ id
# ■ full_name
# ■ age
# ■ id_no
# ■ phone_number

# ● Librarian ○ Properties:
# ■ id
# ■ full_name
# ■ age
# ■ id_no
# ■ emplyment_type(Full/part)

class ParentModel:

        def __init__(self, id: int, full_name: str, age: int, id_no: int):
            self.__id = id
            self.__full_name = full_name
            self.__age = age
            self.__id_no = id_no

        def set_id(self, id):
            self.__id = id

        def get_id(self):
            return self.__id
