import colorama
from colorama import Fore
from os import system

system("Title Temperature converter")


def temp_conversions():
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    def kelvin_to_fahrenheit(kelvin):
        celsius = kelvin_to_celsius(kelvin)
        return celsius_to_fahrenheit(celsius)

    def fahrenheit_to_kelvin(fahrenheit):
        celsius = fahrenheit_to_celsius(fahrenheit)
        return celsius_to_kelvin(celsius)

    def end():
        new = input("\nPress ENTER to exit or new to start over: ")
        if new == "new":
            run()

    def wrong_number():
        print(Fore.RED + "number not recognized please start over")
        run()

    print("Tempature Converter")

    def run():

        print(Fore.WHITE + "1. Celcius to Fahrenheit\n2. Fahreheit to Celcius\n" + \
              "3. Kelvin to Celcius\n4. Kelvin to Fahrenheit\n5. Celcius to Kelvin\n" + \
              "6. Fahrenheit to Kelvin\n or 'exit' to exit")

        def conversion_fck():
            print(Fore.WHITE, end="")
            number = input()
            while number != "exit":

                if number == "1":
                    celsius = (input("how many degrees celcius do you want to convert from?\n"))

                    try:
                        celsius = float(celsius)
                        print(celsius_to_fahrenheit(celsius), "degrees fahrenheit")
                        end()
                    except ValueError:
                        wrong_number()

                elif number == "2":
                    fahernheit = (input("How many degrees fahrenheit do you want to convert from?\n"))

                    try:
                        fahernheit = float(fahernheit)
                        print(fahrenheit_to_celsius(fahernheit), "degrees celcius")
                        end()
                    except ValueError:
                        wrong_number()

                elif number == "3":
                    kelvin = (input("how many degrees kelvin do you want to convert from?\n"))

                    try:
                        kelvin = float(kelvin)
                        print(kelvin_to_celsius(kelvin), "degrees celcius")
                        end()
                    except ValueError:
                        wrong_number()

                elif number == "4":
                    kelvin2 = (input("how many degrees kelvin do you want to convert from?\n"))

                    try:
                        kelvin2 = float(kelvin2)
                        print(kelvin_to_fahrenheit(kelvin2), "degrees fahrenheit")
                        end()
                    except ValueError:
                        wrong_number()

                elif number == "5":
                    celsius = (input("how many degrees celcius do you want to convert from?\n"))

                    try:
                        celsius = float(celsius)
                        print(celsius_to_kelvin(celsius), "degrees kelvin")
                        end()
                    except ValueError:
                        wrong_number()

                elif number == "6":
                    fahernheit2 = (input("how many degrees fahrenheit do you want to convert from?\n"))

                    try:
                        fahernheit2 = float(fahernheit2)
                        print(fahrenheit_to_kelvin(fahernheit2), "degrees kelvin")
                        end()
                    except ValueError:
                        wrong_number()

                else:
                    print(Fore.RED + "please type a number 1-6 or exit to exit")
                    conversion_fck()

        conversion_fck()

    run()


if __name__ == "__main__":
    print(Fore.RED, "ran in temp conv file")
