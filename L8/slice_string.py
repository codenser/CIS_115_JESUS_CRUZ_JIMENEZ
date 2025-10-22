#this program uses a user-defined function to slice a string and returns the sliced string from posoition 0

def slice_my_string():
    my_string= input("enter string: ")
    sliced_string= my_string[0:5]
    return sliced_string 

print(slice_my_string())