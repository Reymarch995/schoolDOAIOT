import math

def calculate_bmi(height, weight) -> float:
    try:
        print("Height = " + str(height))
        print("Weight = " + str(weight))

        bmi = weight / (math.pow(height, 2))

        print("BMI = " + str(bmi))
        
        if(bmi < 18.5):
            print("ur underweight")
            return -1
        elif(18.5 < bmi < 25.0):
            print("ur normal weight")
            return 0
        elif(bmi > 25.0):
            print("ur overweight")
            return 1
    except Exception as e:
        print("uhoh! ran into error: " + e)