import sys
import random


def micro_random(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)


if __name__ == "__main__":
    lower_bound = int(sys.argv[1])
    upper_bound = int(sys.argv[2])
    random_number = micro_random(lower_bound, upper_bound)
    print(random_number)
