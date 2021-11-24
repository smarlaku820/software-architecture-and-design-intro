# No Client should be forced to depend on the methods that it does not use.


from abc import ABC, abstractmethod

# IMultiFunction Interface
class IMultiFunction(ABC):
    @abstractmethod
    def print(self):
        pass
    @abstractmethod
    def get_print_spool_details(self):
        pass
    @abstractmethod
    def scan(self):
        pass
    @abstractmethod
    def scan_photo(self):
        pass
    @abstractmethod
    def fax(self):
        pass
    @abstractmethod
    def internet_fax(self):
        pass

# Xerox device
class XeroxWorkCenter(IMultiFunction):
    # Implements all the abstract methods from IMultiFunction Interface
    def print(self):
        # real printing code
        pass
    def get_print_spool_details(self):
        # real code that gets spool details
        pass
    def scan(self):
        # real code for scanning
        pass
    def scan_photo(self):
        # real code for scanning photos
        pass
    def fax(self):
        # real code for doing faxes
        pass
    def internet_fax(self):
        # real code for doing internet faxes.
        pass

# HP Printer/Scanner
class HPPrinterScanner(IMultiFunction):
    # Doesn't Implements all the abstract methods from IMultiFunction Interface.
    # Leaves Code Pockets which are unimplemented.
    def print(self):
        # real printing code
        pass
    def get_print_spool_details(self):
        # real code that gets spool details
        pass
    def scan(self):
        # real code for scanning
        pass
    def scan_photo(self):
        # real code for scanning photos
        pass
    def fax(self):
        # UnImplemented
        pass
    def internet_fax(self):
        # UnImplemented
        pass

# Cannon Printer
class CannonPrinter(IMultiFunction):
    # Doesn't Implements all the abstract methods from IMultiFunction Interface.
    # Leaves Code Pockets which are unimplemented.
    def print(self):
        # real printing code
        pass
    def get_print_spool_details(self):
        # real code that gets spool details
        pass
    def scan(self):
        # UnImplemented
        pass
    def scan_photo(self):
        # UnImplemented
        pass
    def fax(self):
        # UnImplemented
        pass
    def internet_fax(self):
        # UnImplemented
        pass

x1=XeroxWorkCenter()
h1=HPPrinterScanner()
c1=CannonPrinter()