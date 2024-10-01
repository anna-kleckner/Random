import random 

def get_number_of_colors_1():
    number_of_colors_1 = 0

    while True:
        try: 
            number_of_colors_1 = int(input("Number of small bead colors: "))
            if number_of_colors_1 > 5 or number_of_colors_1 < 0:
                print("ERROR: must be a number between 0-5")
                continue
            else: 
                break
        except: 
            print("ERROR: must be a number between 0-5")
    return number_of_colors_1


def get_number_of_colors_2():
    number_of_colors_2 = 0

    while True:
        try: 
            number_of_colors_2 = int(input("Number of large bead colors: "))
            if number_of_colors_2 > 3 or number_of_colors_2 < 0:
                print("ERROR: must be a number between 0-3")
                continue
            else: 
                break
        except: 
            print("ERROR: must be a number between 0-3")
    return number_of_colors_2


def main(): 
    small_color_list = ["red", "orange", "light orange", "yellow", "light yellow"
             "teal", "light teal", "light green", "green", "light blue",
             "blue", "royal blue", "light purple", "purple", "magenta", 
             "light pink", "pink", "white"]

    large_color_list = ["red", "orange", "yellow", "green", "teal", "blue", "purple",
                     "pink", "grey", "white", "multicolor"]

    number_of_colors_1 = get_number_of_colors_1()
    number_of_colors_2 = get_number_of_colors_2()

    print(f"\nSmall bead colors:")
    if number_of_colors_1 != 0:
        for n in range(number_of_colors_1):
            print(f"Color {n+1}: {random.choice(small_color_list)}")
    else:
        print("none")
    
    print(f"\nLarge bead colors:")
    if number_of_colors_2 != 0:
        for n in range(number_of_colors_2):
            print(f"Color {n+1}: {random.choice(large_color_list)}")
    else:
        print("none")

main()
