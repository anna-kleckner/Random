import random 

def get_number_of_colors():
    number_of_colors = 0

    while True:
        try:
            number_of_colors = int(input("How many colors do you want?: "))
            if number_of_colors > 4 or number_of_colors < 2:
                print("ERROR: must be a number between 2-4")
                continue
            else:
                break
        except:
            print("ERROR: must be a number between 2-4")
    return number_of_colors


def main():
    color_list = ["magenta", "pink", "glow orange", "neon orange", "yellow", 
                 "green", "teal", "glow blue", "neon blue", "royal blue", 
                 "light purple", "purple", "sparkles", "white", "black"]

    number_of_colors = get_number_of_colors()

    for n in range(number_of_colors):
        print(f"Color {n + 1}: {random.choice(color_list)}")

main()

