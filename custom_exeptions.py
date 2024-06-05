class NotANumberError(Exception):
    def __str__(self):
        return "Error: you need to input a number"


class UnknownOperationError(Exception):
    def __str__(self):
        return "Error: unknown operation"



