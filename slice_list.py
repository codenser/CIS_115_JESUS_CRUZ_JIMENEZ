#this program will slice a list containing the months of the year and will print from position 4 to 6

def slice_list():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    months_slicing = months[4:7]
    return months_slicing
print(slice_list())

slice_list()