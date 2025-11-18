#this is my final project for CIS 115

#create a catalog of products with prices with list's in a dictionary
def create_catalog():
    catalog = {}
    1=["Usb Drive(128 GB)", 12.00],
    2=["Mac Book Pro(15 inch)", 2900.00],
    3=["Arduino 1010(with blue tooth)", 48.00],
    4=["Ring Camera(wireless)", 156.00],
    5=["Smart TV(TCL 70 inch)", 359.00]
    
    #I will print in a correct product catalog format
for key, value in catalog.items():
     print(f"{key}      |    {value[0]}    |   ${value[1]:.2f}) ")
    