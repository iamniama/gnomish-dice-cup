from roll import Roll
import pprint

if __name__ == "__main__":
    cup = Roll()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(cup.roll_dice(input()))
