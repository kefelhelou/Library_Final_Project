# ● Borrowing Order:
# ○ Properties:
# ■ id
# ■ date
# ■ client_id
# ■ book_id
# ■ status (Active - Expired - Canceled)

class OrderModel:

    def __init__(self, id: int, date: str, client_id: int, book_id: int, status: str):
        self.__id = id
        self.__date = date
        self.__client_id = client_id
        self.__book_id = book_id
        self.__status = status


    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id