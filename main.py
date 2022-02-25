from roll import Roll
import pprint

if __name__ == "__main__":
    cup = Roll()
    pp = pprint.PrettyPrinter(indent=4)
    roll_info = cup.roll_dice(input())
    pp.pprint(roll_info)
    print(f"Your total roll was: {roll_info['dice_info']['roll_result']}")
