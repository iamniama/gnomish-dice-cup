import re
import random
import pprint


class Roll:

    def __init__(self):
        # TODO: Update mod_rex to include an identifier, such as +2 (weapon) +1 (stat) -2 (partial cover)
        self.dice_rex = re.compile(r'''
            (?P<base_roll>(?P<num_dice>[0-9]*)d(?P<sides>[0-9]{,3}))  # get the base roll, dice, and sides
        ''', re.X)
        self.mod_rex = re.compile(r'[+-][0-9]+')

    def parse_command(self, command_str):
        # TODO: need to differentiate command formats, so that a simple command like 1d20 or just an int can just get passed on to num_gen()

        """
        Breaks the command input into its components and provides a base structure for the roll
        :param command_str: the command string input by the user
        :return: output, a dict with all relevant info about the dice before the roll
        """
        try:
            dice_info = self.dice_rex.search(command_str)
            modifiers = [int(x) for x in list(self.mod_rex.findall(command_str))]
            output = {
                'error': False,
                'command': command_str,
                'dice_info': {
                    'dice': 1 if not dice_info['num_dice'].isdigit() else int(dice_info['num_dice']),
                    'sides': int(dice_info['sides']),
                    'modifiers': modifiers,
                    'mod_sum': sum(modifiers) if len(modifiers) > 0 else 0,
                    'advantage': 'with advantage' in command_str,
                    'disadvantage': 'with disadvantage' in command_str,
                    'roll_result': 0,
                    'primary_dice': 0,
                    'secondary_dice': 0,
                    'dice_pool_primary': [],
                    'dice_pool_secondary': [],
                },
            }
        except TypeError:
            return {'error': True}
        return output

    @staticmethod
    def num_gen(sides):
        """
        Random number generation for dice rolling
        :param sides: the number of sides (the upper bound for random int)
        :return: a random choice selected from a list of 25 random integers within range(1,sides)
        """
        return random.choice([random.randint(1,sides) for x in range(25)])

    def roll_dice(self, command_str):
        """
        The main method of the Roll class, roll_dice takes the user's commmand, passes it to the command parser, and returns dice roll data
        :param command_str: the user input
        :return: dict with output of parse_command along with the actual results of the roll
        """
        cmd_data = self.parse_command(command_str)
        cmd_data['dice_info']['dice_pool_primary'] = [self.num_gen(cmd_data['dice_info']['sides']) for x in range(cmd_data['dice_info']['dice'])]
        cmd_data['dice_info']['dice_pool_secondary'] = [self.num_gen(cmd_data['dice_info']['sides']) for x in
                                         range(cmd_data['dice_info']['dice'])]
        cmd_data['dice_info']['primary_dice'] = sum(cmd_data['dice_info']['dice_pool_primary'])
        cmd_data['dice_info']['secondary_dice'] = sum(cmd_data['dice_info']['dice_pool_secondary'])
        if cmd_data['dice_info']['advantage']:
            cmd_data['dice_info']['roll_result'] = max(cmd_data['dice_info']['primary_dice'], cmd_data['dice_info']['secondary_dice']) + cmd_data['dice_info']['mod_sum']
        elif cmd_data['dice_info']['disadvantage']:
            cmd_data['dice_info']['roll_result'] = min(cmd_data['dice_info']['primary_dice'], cmd_data['dice_info']['secondary_dice']) + cmd_data['dice_info']['mod_sum']
        else:
            cmd_data['dice_info']['roll_result'] = cmd_data['dice_info']['primary_dice']
        return cmd_data


if __name__ == "__main__":
    cup = Roll()
    pp = pprint.PrettyPrinter(indent=4)
    roll_info = cup.roll_dice(input())
    pp.pprint(roll_info)
    if not roll_info['error']:
        pp.pprint(roll_info)
        print(f"Your total roll was: {roll_info['dice_info']['roll_result']}")