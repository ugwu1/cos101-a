def physic_and_maths_operation_option():
    print("\nmaths and physic operation option: ")
    print("a. distance")
    print("b. potential energy")
    print("c. surface tension")
    print("d. final velocity")
    print("e. triangle")
    print("f. end")

physic_and_maths_operation_option()
option = input("enter an option a to f  ")
if option == "a":

    speeds = int(input("enter the speed of the distance  "))
    time = int(input("enter the time taken "))
    distance = speeds * time
    print(distance)

elif option == "b":
    mass = int(input("enter the mass of the PE "))
    gravity = int(input("enter the gravity of the PE "))
    height = int(input("enter the height of the PE "))
    potential_energy = mass * gravity * height
    print(potential_energy)

elif option == "c":
    force = int(input("enter the force "))
    length = int(input("enter the length "))
    surface_tension = force * length
    print(surface_tension)

elif option == "d":
    initial_velocity = int(input("enter the initial velocity "))
    accelation = int(input("enter the accelation "))
    time = int(input("enter the time taken "))
    final_velocity = initial_velocity * accelation * time
    print(final_velocity)

elif option == "e":
    base = int(input("enter the base "))
    height = int(input("enter the height "))
    area = base * height
    print(area)

elif option =="f":
    close = "thank you for using henry's code "
    matric = "matric no bhu|24|04|05|0126"
    end = close + matric
    print(end)

else :
    print("the option type is invalid pls choose an option a to f")


