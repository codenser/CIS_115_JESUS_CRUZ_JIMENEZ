#this is my final project for CIS-115

#create a catalog of products with prices with list's in a dictionary
def create_catalog():
    catalog = {
    "Usb Drive(128 GB)" : 12.00,
    "Mac Book Pro(15 inch)" : 2900.00,
    "Arduino 1010(with blue tooth)" : 48.00,
    "Ring Camera(wireless)" : 156.00,
    "Smart TV(TCL 70 inch)" :359.00
    }
    #I will print in a correct product catalog format
    for key, value in catalog.items():
        print(() ,f"{key:<30}   |   ${value:.2f}")

#building the structure for the layout of the catalog
print("-" * 75)
print(" " * 25, "Product catalog")
create_catalog()
print("-" * 75)

products = {
    "prod id" : 1,
    "sku" : "usb_k981",
    "price" : 12.00,
    "qty" : {},
    "qtyOnHand" : 1000
},{
    "prod id:" :2,
    "sku" : "mbpro_490",
    "price" : 2900.00,
    "qty" : {},
    "qtyOnHand" : 45
},{
    "prod id:" :3,
    "sku" : "chip_1010",
    "price" : 48.00,
    "qty" : {},
    "qtyOnHand" : 325
},{
    "prod id:" :4,
    "sku" : "cam_78",
    "qty" : {},
    "price" : 156.00,
    "qtyOnHand" : 98,
},{
    "prod id" : 5,
    "sku" : "smt_tv_100",
    "price" : 359.00,
    "qty" : {},
    "qtyOnHand" : 75
}
