class Student():
#create a class
    
    def __inti__(self,first,last,programme):
#input data
        self.first = None
        self.last = None
        self.progamme = None
        
    def set_first(self,first):
        self.first=first
    def set_last(self,last):
        self.last=last
    def set_programme(self,programme):
        self.programme=programme

    def print_information(self):
        print("Name is "+self.first+" "+self.last+" Programme is "+self.programme)


#example
    
test = Student()
test.set_first("Zhou")
test.set_last("Shen")
test.set_programme("medicine")
test.print_information()