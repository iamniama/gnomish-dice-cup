import re
import random


class Roll:
    def __init__(self):
        self.dice_rex = re.compile(r'''
            (?P<base_roll>(?P<num_dice>[0-9]*)d(?P<sides>[0-9]{,3}))  # get the base roll, dice, and sides
        ''', re.X)
        self.mod_rex = re.compile(r'[+-][0-9]+')

    def parse_command(self, command_str):
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
        return output

    def num_gen(self, sides):
        return random.choice([random.randint(1,sides) for x in range(25)])

    def roll_dice(self, command_str):
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


