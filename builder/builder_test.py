"""
You are asked to implement the Builder design pattern for
rendering simple chuncks of code

Sample use of the builder you are asked to create:
cb = CodeBuilder('Person').add_field('name', '""')\
                          .add_field('age', '0')
print(cb)

The expected output of the above code is:
class Person:
  def __init__(self):
    self.name = ""
    self.age = 0

"""

class Code:
    def __init__(self):
        self.name = None
        self.attributes = []
    
    def __str(self, ident):
        head = f"class {self.name}\n"
        head = head + f"  def__init__(self)\n"
        attr = ""
        for a in self.attributes:
            attr = attr + f"    self.{a.name} = {a.value}\n"
            
        return str(head + attr)
        

    def __str__(self):
        return self.__str(0)

class Attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class CodeBuilder:
    __root = Code()
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    def add_field(self, name, type):
        self.__root.attributes.append(Attribute(name, type))
        return self

    def __str__(self):
        print(self.__root)

if __name__ == "__main__":
    cb = CodeBuilder('Person').add_field('name', '""')\
                          .add_field('age', '0')
    print(cb)