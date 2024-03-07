"""
Author: Christine Wei
Date: February 20, 2023,
Description: This program determines the escape velocity of any planet
"""

# Global constants for the values of pi and gravitational constant 
PI = 3.14159265

G = 6.67428*(10**-11)


# Mainline logic
def main():
    """Takes user input for integer circumference and integer acceleration due to gravity, \
    displays radius, mass, and escape velocity of planet"""
    
    circum = float(input("Circumference (m) of the planet? "))
    acc_due_grav = float(input("Acceleration due to gravity (m/s^2)? "))
    escape_velocity(circum, acc_due_grav)


# Displaying results in the right units
def display_results(plan_radius, plan_mass, plan_vescape):
    """Takes the radius(m), mass(kg), and escape velocity(m/s) of the planet, \
    displays radius(km), mass(10^21 kg), escape velocity(km/s) of planet in correct units"""
    
    radius_km = plan_radius/1000
    mass_kg = plan_mass/10**21
    vescape_km = plan_vescape/1000
    
    print("Planet radius = ", round(radius_km, 1), "km",
          "\nPlanet mass = ", round(mass_kg, 1), "x 10^21 kg",
          "\nEscape velocity = ", round(vescape_km, 1), "km/s")


# Calculating the escape velocity
def escape_velocity(plan_circ, plan_acc_due_grav):
    """Takes the circumference, and acceleration due to gravity of the planet, \
    calculates radius, mass, and escape velocity, and displays results"""
    
    radius = plan_circ/(2*PI)
    mass = (plan_acc_due_grav*radius**2)/G
    vescape = ((2*G*mass)/radius)**0.5
    
    print("\nCalculating the escape velocity...")
    display_results(radius, mass, vescape)


main()
