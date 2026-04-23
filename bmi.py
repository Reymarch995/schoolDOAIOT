import math

def calculate_bmi(height, weight) -> float:
    try:
        print("Height = " + str(height))
        print("Weight = " + str(weight))

        bmi = weight / (math.pow(height, 2))

        print("BMI = " + str(bmi))
        return bmi
    except Exception as e:
        print("uhoh! ran into error: " + e)
def bmiRange(bmi: float) -> null:
    if(bmi < 18.5):
        print("ur underweight")
    elif(18.5 < bmi < 25.0):
        print("ur normal weight")
    elif(bmi > 25.0):
        print("ur overweight")
    else:
        return 1

bmi = calculate_bmi(height=1.73,weight=37)
bmiRange(bmi)