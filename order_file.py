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
