#this program uses a user-defined function to calculate kenetic energy

def kinetic_energy(mass, velocity):
    ke = 0.5 * mass * velocity**2
    return ke
mass = int(input("Enter mass in kg: "))
velocity = int(input("Enter velocity in m/s: "))
print(f'The kinetic energy of the given object is {kinetic_energy(mass, velocity)} joules')