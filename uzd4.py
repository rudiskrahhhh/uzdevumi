direction = str(input("uz kuru virzienu tu gribi doties? "))

if direction == "w":
    print("tu ej uz prieksu")
elif direction == "a":
    print("tu ej pa labi")
elif direction == "s":
    print("tu ej pa kreisi")
elif direction == "d":
    print("tu ej uz atpakalu")
else:
    print("kluda!")