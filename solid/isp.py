# ISP: interface segregation principle
"""
This interface has to many operations that are not related
"""
class Machine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError

class MultiFunctionalPrinter(Machine):
    def print(self, document):
        print(document)
    def fax(self, document):
        print(document)
    def scan(self, document):
        scan(document)

class OldFashionPrinter(Machine):
    def print(self, document):
        print(document)  # ok
    def fax(self, document):
        pass  # bad solution
    def scan(self, document):
        """Not supported!""" # bad
        raise NotImplementedError("Print cannot scan!")  # vary bad!

# ISP approach
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        print(document)

class MultiFunctionalDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionalMachine(MultiFunctionalDevice):
    def __init__(self, priter, scanner):
        self.scanner = scanner
        self.printer = Printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
