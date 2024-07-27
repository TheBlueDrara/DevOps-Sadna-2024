import random
import numpy as np
import requests

def main():
    start = input("Enter 'start' to begin: ")

    if start.lower() == 'start':
        num = random.randint(1, 5)

        if num == 3:
            print("BOOM!!")
        else:
            print("You're safe.")
    else:
        print("Invalid input. Please enter 'start' to begin.")

if __name__ == "__main__":
    main()
