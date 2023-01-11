# ● Librarian ○ Properties:
# ■ id
# ■ full_name
# ■ age
# ■ id_no
# ■ emplyment_type(Full/part)
from model.parent_file import ParentModel


class LibrarianModel(ParentModel):


        def __init__(self, id: int, full_name: str, age: int, id_no: int, employment_type: str):
            super(LibrarianModel, self).__init__(id, full_name, age, id_no)
            self.__employment_type = employment_type