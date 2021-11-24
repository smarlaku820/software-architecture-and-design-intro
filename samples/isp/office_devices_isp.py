# No Client should be forced to depend on the methods that it does not use.


from abc import ABC, abstractmethod

# Implementing Multiple Interfaces
class IPrint(ABC):
    @abstractmethod
    def print(self):
        pass
    @abstractmethod
    def get_print_spool_details(self):
        pass

class IScan(ABC):
    @abstractmethod
    def scan(self):
        pass
    @abstractmethod
    def scan_photo(self):
        pass
 
class IFax(ABC):
    @abstractmethod
    def fax(self):
        pass
    @abstractmethod
    def internet_fax(self):
        pass


# Xerox device
class XeroxWorkCenter(IPrint, IScan, IFax):
    # Implements all the abstract methods from Iprint,IScan,IFax Interfaces
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
class HPPrinterScanner(IPrint, IScan):
    # Implements all the abstract methods from Iprint,IScan Interfaces
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

# Cannon Printer
class CannonPrinter(IPrint):
    # Implements all the abstract methods from IPrint Interface
    def print(self):
        # real printing code
        pass
    def get_print_spool_details(self):
        # real code that gets spool details
        pass

x1=XeroxWorkCenter()
h1=HPPrinterScanner()
c1=CannonPrinter()