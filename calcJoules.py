#this program uses  a user-defined function to calculate joules produces of a given mass
#the formula is e = mc^2

def calculate_energy():
    mass = float(input("enter mass in Kg: "))
    c = 2.99 * 10**8
    energy = mass * c**2
    return energy

joules = calculate_energy()

print(f'The energy produced from given mass is {joules} joules')