import collections
from collections import Counter
import json
import math
import threading

my_list = []
user_timer = ()
# previous_input = ""

time_second = int(input(">> Please input the amount of time in seconds between emitting numbers and their frequency\n"))


def Console_Timer():
    global user_timer
    user_timer = threading.Timer(time_second, Console_Timer)
    user_timer.start()

    # Counts the frequency of number in a list
    ctr = collections.Counter(my_list)
    frequency = Counter(ctr)
    # frequency.most_common()
    if len(my_list) != 0:
        print(">>", repr(frequency).strip('Counter()').replace("{", "").replace('}', ""))


def check_perfect_square(m):
    # Function to check the whether the number is perfect square or not?
    n = int(math.sqrt(m))
    return n * n == m


def check_fibo(m):
    return check_perfect_square(5 * m * m + 4) or check_perfect_square(5 * m * m - 4)


def processing_input():
    # Core function of the application. Processes the user input as per the requirements.

    is_halted = False
    while True:
        user_input = input(">> Please enter the next number\n")

        if user_input == 'halt':
            user_timer.cancel()
            print(">> timer halted")
            is_halted = True
            break

        if user_input == 'quit':
            ctr = collections.Counter(my_list)
            frequency = Counter(ctr)
            # frequency.most_common()
            print(">>", repr(frequency).strip('Counter()').replace("{", "").replace('}', ""))
            exit_input = input(">> Thanks for playing, press any key to exit.")
            user_input = ""
            user_timer.cancel()
            exit()
            break

        if user_input.isnumeric():
            user_input = int(user_input)

            # check for Fibonacci number
            check_fibo(user_input)
            if check_fibo(user_input):
                print(">> FIB")
            my_list.append(user_input)

    if is_halted:
        user_input = input("")

        if user_input == 'resume':
            user_timer.join()
            print(">> timer resumed")
            is_halted = False
            Console_Timer()
            processing_input()


def main():
    Console_Timer()

    first_number = int(input(">> Please enter the first number\n"))
    my_list.append(first_number)
    processing_input()


main()
