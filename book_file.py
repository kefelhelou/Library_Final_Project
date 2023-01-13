# ● Book
# ○ Properties:
# ■ id
# ■ title
# ■ description
# ■ author
# ■ status(Available-UnAvailable)

class BookModel:

    def __init__(self, id: int, title: str, description: str, author: str, status: str):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__status = status

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id