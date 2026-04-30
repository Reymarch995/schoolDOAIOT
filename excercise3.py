#excercise 3

def display_main_menu() -> str:
    print("## display ##")
    uinput = (input("Enter some numbers separated by commas (e.g. 5,67,32): "))
    return uinput

def get_user_input(uinput: str) -> list:
    print("## input ##")
    x = uinput.split(",")
    print(x)
    temp = []
    for item in x:
        item = item.strip()
        if item.replace(".", "", 1).replace("-", "", 1):
            number = float(item)
            temp.append(number)
    return temp

def calc_average(list: list) -> float:
    print("## average ##")
    sum = 0
    for x in list:
        sum += x
    average = sum / len(list)
    print(average)

def find_min_max(list: list) -> list:
    print("## minmax ##")
    min_temp = 999999999999999
    max_temp = -99999999999999
    temp = 0

    for i in range(len(list)):
        if (list[i] < min_temp):
            min_temp = list[i]
        elif (list[i] > max_temp):
            max_temp = list[i]

    print(f"{min_temp},{max_temp}")
    return [min_temp,max_temp]

def sort_temperature(list: list) -> list:
    print("## sort temp ##")
    temp = 0
    for i in range(2):
        for i in range(len(list)):
            if i == (len(list) - 1):
                break
            elif list[i] > list[i+1]:
                print(i)
                temp = list[i+1]
                list[i+1] = list[i]
                list[i] = temp
        print(list)
        return list

def calc_median_temperature() -> float:
    list: list = ()
    list = sort_temperature(listFruits)
    print("## median ##")
    median = 0
    median = list[(len(list) // 2)]
    print(f"median: {median}")

listFruits = [5,3,2,6,5,7,8]

find_min_max(listFruits)
sort_temperature(listFruits)
uinput = display_main_menu()
numbers = get_user_input(uinput)
calc_median_temperature()
