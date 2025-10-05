#this program uses a user fefined funtion to print the months of the year with being given using a star and end argument

def months_of_year(startMonth, endMonth):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    start = int(input("enter starting month (1-12): "))
    end = int(input("enter ending month (1-12): "))

    for month in months[start-1:end]:
        print(month)

months_of_year(1,12)