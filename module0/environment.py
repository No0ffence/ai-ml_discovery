import sys
import time
import random

import math


def print_temp(low, high):
    amp = (high - low) / 2
    midline = (high + low) / 2
    for i in range(1, 49):
        variation = random.uniform(-0.5, 0.5)
        temp = round(
            amp * math.sin((math.pi / 24) * (i - 9)) + midline + variation, 1)
        print(temp)
        time.sleep(1)


def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <season>")
            return
        season = sys.argv[1]
        if season == "summer":
            low_temp = random.uniform(5, 10)
            high_temp = random.uniform(25, 45)
        elif season == "winter":
            low_temp = random.uniform(-25, -10)
            high_temp = random.uniform(3, 10)
        elif season == "autumn":
            low_temp = random.uniform(-4, 0)
            high_temp = random.uniform(10, 18)
        elif season == "spring":
            low_temp = random.uniform(0, 12)
            high_temp = random.uniform(18, 23)
        else:
            print("Not valid season")
            return
        print_temp(low_temp, high_temp)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
