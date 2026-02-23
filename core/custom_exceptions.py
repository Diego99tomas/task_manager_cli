class RangeError(Exception):
    def __init__(self,possition:int,len_list:int):
        note="It must be greater than zero and less than "
        self.message=f"{note}{len_list}: value {possition}"
        super().__init__(self.message)