import math

#Allow work many times
desire = input("Do math?")
while desire.lower() not in ["no", "n", "stop" "don't" "dont" "nah"]:
    #Make a variable for each value
    Side1 = int(input("First side"))
    Side2 = int(input("Second side"))

    #Calculate the hypotenuse
    Hypotenuse = math.sqrt(Side1**2 + Side2**2)
    print(Hypotenuse)
    desire = input("Do math?")
