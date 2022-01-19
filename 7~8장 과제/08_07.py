class PhoneBook:
    def __init__(self):
        self.contacts = {}
        
    def __str__(self):
        PB = str()
        code = []
        for name in self.contacts.keys():
            temp = name +"  "+ f"{self.contacts[name]}"
            code.append(temp)
        PB = "\n".join(code)
        return PB
    
    def add(self, name, mobile= None, office=None, email=None):
        self.contacts[name] = mobile, office, email
        
obj = PhoneBook()
obj.add("kim", office="1231484", email = "kim@company.com")
obj.add("Park", mobile = "01045186218", email= "park@ceo.com")
print(obj)