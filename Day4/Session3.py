# OOPS - Popular and used in Java, .Net and Python
# Polymorphism
# Inheritance
# Encapsulation
# Abstraction
# Don't Repeat Yourself - DRY
# MVC - Model (Module connect to DB), View, Control
# Some other architecture
# Airtel, Jio
# Prepaid (CustomerName), Postpaid (CustomerName), Triple Pay - TV, Internet, Handset
# Generate bill def generate_Bill(MSISDN):
# class className(ParentClassName):
#   class attributes - variables, instance attributes - functions

class Customer():
    # class attributes
    # __ used for private variable
    __varCustomerName = 'DefaultName'
    __varCustomerAddress = 'India'
    __varCustomerAge = 18
    __varCustomerGender = 'M'
    #varTemporary = 'GarbageName'
    #__str__ = 'Trying'

    """
        def __init__(self, varName, varGender,varAge):
            self.__varCustomerGender = varGender
            self.__varCustomerName = varName
            self.__varCustomerAge = varAge
    """
    # Constructor - initialization
    def __init__(self, varName, varGender,varAge,varAddress, varIsCust=False):
        self.__varCustomerGender = varGender
        self.__varCustomerName = varName
        self.__varCustomerAge = varAge
        self.__varCustomerAddress = varAddress

    def __str__(self):
        return "This is Customer class"

    # this ==> self
    # instance attributes
    def getCustomerDetails(self):
        return self.__varCustomerName, self.__varCustomerAge, self.__varCustomerGender, self.__varCustomerAddress
    def updateCustomerDetails(self,varName, varGender,varAge,varAddress):
        self.__varCustomerGender = varGender
        self.__varCustomerName = varName
        self.__varCustomerAge = varAge
        self.__varCustomerAddress = varAddress
        # code to update in database

varCustomer = Customer('Gaurav', 'M', 30, 'Banglore, KA')
#print(varCustomer.__varCustomerName, varCustomer.__varCustomerGender)
print(varCustomer.getCustomerDetails())
varCustomer.updateCustomerDetails('Gaurav', 'M', 33, 'Delhi, Delhi')
print(varCustomer.getCustomerDetails())
varCustomer.__varCustomerName = 'Python'
print(varCustomer.getCustomerDetails())
print(varCustomer.__varCustomerName)
print(varCustomer.__str__())
#varCustomer2 = Customer('Gaurav', 'M', 30)
#print(varCustomer2.getCustomerDetails())
var1 = 10
print(type(var1))

print('-----------------Inheritance----------------')

class Prepaid(Customer):
    # instance properties
    __varPrepadISDN = 9999999999
    __varPrepaidValidty = 30
    __varPrepaidPlanType = 'Friends'

    def __init__(self, varName, varGender,varAge,varAddress, varISDN, varValidity, varPlanType):
        super().__init__(varName, varGender,varAge,varAddress)
        self.__varPrepadISDN = varISDN
        self.__varPrepaidValidty = varValidity
        self.__varPrepaidPlanType = varPlanType
        #self.varTemporary

    def getPrepaidDetails(self):
        return self.getCustomerDetails(), self.__varPrepaidPlanType, self.__varPrepadISDN, self.__varPrepaidValidty

    def getCustomerDetails(self, *args): # Overriden - customization function
        status = ''
        for num in args:
            if type(num) is float:
                status = "Prepaid bill is paid"
            else:
                status = "Prepaid bill is not paid"
        number = '91-' + str(self.__varPrepadISDN)
        return super(Prepaid, self).getCustomerDetails(), number, status

    #def getCustomerDetails(self, var1): Overloading is not possible
    #    return "Overloaded function"
prepaid1 = Prepaid('Gaurav', 'M', 30, 'Mumbai, MH', 9872494737, 15, 'Family')
print(prepaid1.getPrepaidDetails())
print(prepaid1.getCustomerDetails(10))
print(prepaid1.getCustomerDetails(10.6))
print(prepaid1.getCustomerDetails())
print(isinstance(prepaid1, Prepaid))
print(isinstance(prepaid1, Customer))
print(isinstance(varCustomer, Prepaid))
print(issubclass(Prepaid, Customer))