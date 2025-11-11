from Zoo.Food import Food
class Animal:
    Name: str
    NickName: str = ""
    isMamel: bool
    isHungry: bool = False
    isPreditor: bool
    Age: int

    def __init__(self,_name:str,_isMamel:bool,_isPreditor:bool,_age:int):
        self.Name=_name
        self.isMamel=_isMamel
        self.isPreditor=_isPreditor
        self.Age=_age

    def feed(self,_food:Food):
        if (self.isPreditor and _food.isVegi):
            raise Exception("This Animal cannot eat vegitarion food")
            
        if (self.isHungry):
            self.isHungry = False
