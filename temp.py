def calc_average_temperature(list: list) -> float:
    sum = 0
    for x in list:
        sum += x
    average = sum / len(list)
    print(average)

listFruits = [5,3,2,6]

calc_average_temperature(listFruits)