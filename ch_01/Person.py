




class Person:
    def __init__(self,name,age,aderess):
        self.name = name
        self.age = age
        self.aderess = aderess
        


class Person_info(Person):
    def __init__(self):
        super().__init__()
    
    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}이고, 나이는 {self.age}, 주소는 {self.aderess}입니다.')
