# Excercise 1
name = "Rayhan"
age = 17
gpa = 3.34
is_student = True

print(f"{name} {type(name)}")
print(f"{age} {type(age)}")
print(f"{gpa} {type(gpa)}")
print(f"{is_student} {type(is_student)}")

# Excercise 2
birth_year = "2008"

usr_age = 2026 - int(birth_year)

print(f"you are {usr_age} years old.")

# Excercise 3
celsius = 25
farenheit = (celsius * 9/5) + 32
print(f"{celsius}C is {farenheit}F")

# Excercise 4
price = "$19.99"

clean_price = float(price.replace("$",""))
print(f"Price after tax is: {round((clean_price * 1.07),2)}")

#Excercise 5:
birth_year = "2008"
age = 2026 - int(birth_year) #supposed to be an int
print("You are ", age ," years old") #this aint c++ vro

# Excercise 2.1
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])
print(fruits.append("orange"))
print(fruits.insert("orange",1))
print(fruits.remove("banana"))
popped = fruits.pop()
print(fruits)