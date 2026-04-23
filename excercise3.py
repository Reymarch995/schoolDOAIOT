#excercise 3

def display_main_menu() -> str:
    uinput = input("Enter some numbers separated by commas (e.g. 5,67,32): ")
    return uinput

def get_user_input(uinput: str) -> float:
    x = uinput.split(",")
    print(x)



uinput = display_main_menu()
get_user_input(uinput)
