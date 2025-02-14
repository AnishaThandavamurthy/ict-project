class CustomerError(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

def check_value(x):
    if x < 0:
        raise CustomerError("Number should be non negative")
    elif x > 100:
        raise CustomerError("Number is too large")
    return x

try:
    num=int(input("Enter a number(0-100):"))
    result=check_value(num)
    print("valid number entered:",result)
except CustomerError as ce:
    print("CustomerError occured",ce.message)
except ValueError:
    print("Invalid input .Please enter a valid number")    

