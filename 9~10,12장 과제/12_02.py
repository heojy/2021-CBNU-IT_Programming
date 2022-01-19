class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)
        
class Person:
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)
        
class Contact(Address, Person):
    def __init__(self, street, city, name, email):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)
        
        print(f"이름 : {self.name} \n주소 : {self.city}, {self.street} \n이메일 주소 : {self.email} \n" )
    
ContactAddress1 = Contact('Dalbit-ro','Sejong-si', "Heo", "1234@gmail.com")
ContactAddress2 = Contact('Sejong-ro','Sejong-si', "Kim", "5678@gmail.com")