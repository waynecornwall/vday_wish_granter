

print()
wish_receiver = input("Enter your first name: ")
wish_giver = input("Enter your partner's name: ")
message = f"\nHappy Valentines Day {wish_receiver.title()}. {wish_giver.title()} loves you and your every wish is their command."
print(message)


def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def vday_wish_granter():
    is_giver_alive = True
    while is_giver_alive:
        print()
        while True:
            kisses = input("How many kisses would you like?: ")
            if kisses.isdigit():
                break
            elif isfloat(kisses):
                print(f"Sorry {wish_receiver.title()}, {kisses} is an invalid response. Must be a whole digit. Try again.\n")
                continue
            elif kisses.isalnum():
                print(f"Sorry {wish_receiver.title()}, {kisses} is an invalid response. Must be a digit. Try again.\n")
                continue
            else:
                print(f"Sorry {wish_receiver.title()}, {kisses} is an invalid response. Try again.\n")
                continue

        while True:
            hugs = input("How many hugs would you like?: ")
            if hugs.isdigit():
                break
            elif isfloat(hugs):
                print(f"Sorry {wish_receiver.title()}, {hugs} is an invalid response. Must be a whole digit. Try again.\n")
                continue
            elif hugs.isalnum():
                print(f"Sorry {wish_receiver.title()}, {hugs} is an invalid response. Must be a digit. Try again.\n")
                continue
            else:
                print(f"Sorry {wish_receiver.title()}, {hugs} is an invalid response. Try again.\n")
                continue

        while True:
            orgasms = input("How many orgasms would you like?: ")
            if orgasms.isdigit():
                break
            elif isfloat(orgasms):
                print(f"Sorry {wish_receiver.title()}, {orgasms} is an invalid response. Must be a whole digit. Try again.\n")
                continue
            elif orgasms.isalnum():
                print(f"Sorry {wish_receiver.title()}, {orgasms} is an invalid response. Must be a digit. Try again.\n")
                continue
            else:
                print(f"Sorry {wish_receiver.title()}, {orgasms} is an invalid response. Try again.\n")
                continue

        if kisses == "0" and hugs == "0" and orgasms == "0":
            alive_loop = True
            while alive_loop:
                alive_or_dead = input(f"\nIs {wish_giver.title()} alive or dead?: ")
                if alive_or_dead.lower() == "alive":
                    print(f"{wish_giver.title()} is {alive_or_dead.lower()}!", end=" ")

                    lovin_loop = True
                    while lovin_loop:
                        more_lovin = input("So would you like some lovin'? ")
                        if more_lovin.lower() == "yes":
                            lovin_loop = False
                            alive_loop = False
                            continue
                        elif more_lovin.lower() == "no":
                            print(f"\n{wish_giver.title()} is {alive_or_dead.lower()} and you don't want their lovin'? That's weird. Aight. See ya!")
                            alive_loop = False
                            is_giver_alive = False
                            break
                        else:
                            print(f"Sorry {wish_receiver.title()}, {more_lovin} is an invalid response")
                            continue

                elif alive_or_dead.lower() == "dead":
                    print(f"Apparently {wish_giver.title()} is {alive_or_dead.lower()}. Sucks to be you {wish_receiver.title()}")
                    is_giver_alive = False
                    break
                else:
                    print(f"Sorry {wish_receiver.title()}, {alive_or_dead} is not a valid response.")
        else:
            print(f"\nYou've just received {kisses} kisses, {hugs} hugs and had {orgasms} orgasms from {wish_giver.title()}")
            more_loop = True
            while more_loop:
                more = input("Would you like more? (yes or no): ")
                if more.lower() == "yes":
                    print(f"\nGOOD CHOICE {wish_receiver.upper()}!")
                    more_loop = False
                    continue
                elif more.lower() == "no":
                    print("\nI guess you've had enough. There's more where that came from. See you again soon.")
                    is_giver_alive = False
                    break
                else:
                    print(f"Sorry {wish_receiver.title()}, {more} is not a valid response. Try again.")
                    continue


run_program = True
while run_program:
    vday_wish_granter()
    play_again = True
    while play_again:
        choice = input("\nWould you like to play again? (yes or no): ")
        if choice.lower() == "yes":
            print("Ok. Here we go!")
            play_again = False
        elif choice.lower() == "no":
            print(f"\nThanks for playing {wish_receiver.title()}. HAPPY VALENTINE'S DAY!")
            run_program, play_again = False, False
        else:
            print(f"Sorry {wish_receiver.title()}, {choice} is not a valid response. Try again.")
            continue

