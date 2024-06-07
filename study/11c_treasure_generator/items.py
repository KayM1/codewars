import random
import string
import re


ids = {}

class Stats:
    STATS = ['CRIT','HASTE','TOUGHNESS','MULTISTRIKE','PENETRATION','ARMOR']

    def __init__(self, order, unid):
        self.order = order
        self.unid = unid
        self.stat = random.choice(self.STATS)
        self.power =  self.generate_power()

    def generate_power(self):
        if self.order < 2:
            p = random.random()
            # Determine power based on desired probabilities
            if p < 0.55:  # 55% chance
                return random.randint(1, 2000)  # Common
            elif p < 0.75:  # 20% chance
                return random.randint(2000, 4000)  # Uncommon
            elif p < 0.90:  # 15% chance
                return random.randint(4000, 6000)  # Rare
            elif p < 0.98:  # 5% chance
                return random.randint(6000, 8000)  # Epic
            else:  # 2% chance
                return random.randint(8000, 10000)  # Legendary
        else:
            return random.randint(200,600)


class Item:
    # ANSI escape codes for colors
    COLORS = {
        'common': '\033[38;5;250m',  # White
        'uncommon': '\033[92m',  # Green
        'rare': '\033[94m',  # Blue
        'epic': '\033[95m',  # Magenta
        'legendary': '\033[38;5;214m'  # Red
    }

    RESET = '\033[0m'  # Reset color
    BOLD = '\033[1m'   # Bold text

    def __init__(self):
        self.syllable_map = {
    '0': ['Wou', 'Thui', "Snee", "Ber", "Fau"],
    '1': ['klin', 'stee', 'bee', 'kha', 'rit'],
    '2': ['blau', 'roo', 'gee', 'zwar', 'gro'],
    '3': ['win', 'wors', 'lich', 'kos', 'draa'],
    '4': ['haa', 'ber', "koe", 'dan', 'groz'],
    '5': ['hal', 'Tar', 'slo', 'nach', 'ze'],
    '6': ['spe', 'krach', 'glan', 'tij', "ki"],
    '7': ['gou', 'rij', 'moo', 'lan', 'sne'],
    '8': ['ros', 'twe', 'kha', 'kou', 'rusti'],
    '9': ['maa', 'ste', "lie", 'bulga', 'winte']
        }

        self.name = random.choice(self.ITEM_NAMES)
        self.type = self.name.lower()
        self.unid = self.generate_unique_id()
        self.power = self.generate_power()
        self.stats = Stats(1, self.unid)
        self.rarity = self.determine_rarity()
        
        if self.rarity in ['rare', 'epic', 'legendary']:
            self.add_stat('sec_stats', 2)
        
        if self.rarity in ['epic', 'legendary']:
            self.add_stat('tert_stats', 3)

        self.name = self.generate_name(self.name)
        if self.rarity == 'epic' or self.rarity == 'legendary':
            self.unique_name = self.generate_unique_name(self.unid)
        else:
            self.unique_name = None

        self.real_power = self.determine_real_power_hidden()

    def add_stat(self, stat_name, order):
        new_stat = Stats(order, self.unid)
        
        # Check against primary stats
        if new_stat.stat == self.stats.stat:
            self.stats.power += new_stat.power
            return
        
        # Check against secondary stats if they exist
        if hasattr(self, 'sec_stats') and self.sec_stats is not None:
            if new_stat.stat == self.sec_stats.stat:
                self.sec_stats.power += new_stat.power
                return
    
        # Assign the new stat to the specified attribute
        self.rarity = self.determine_rarity()
        setattr(self, stat_name, new_stat)


    # Adjectives for item names based on rarity
    FLAVOR = {
        'common': ['Rusty', 'Old', 'Dusty', 'Worn', 'Plain'],
        'uncommon': ['Shiny', 'Polished', 'Fine', 'Quality', 'Sturdy'],
        'rare': ['Gleaming', 'Exquisite', 'Intricate', 'Ornate', 'Prized'],
        'epic': ['Mystical', 'Enchanted', 'Heroic', 'Mythical', 'Epochal'],
        'legendary': ['Divine', 'Exalted', 'Ethereal', 'Celestial', 'Astral']
    }

    ITEM_NAMES = ['Sword', 'Shield', 'Gem', 'Bow', 'Armor', 'Belt', 'Cloak']

    
    def generate_power(self):
        # Generate a random number between 0 and 1
        p = random.random()
        
        # Determine power based on desired probabilities
        if p < 0.70:  # 55% chance
            return random.randint(1, 1000)  # Common
        elif p < 0.80:  # 20% chance
            return random.randint(1000, 2000)  # Uncommon
        elif p < 0.95:  # 15% chance
            return random.randint(2000, 4000)  # Rare
        elif p < 0.995:  # 5% chance
            return random.randint(4000, 6000)  # Epic
        else:  # 2% chance
            return random.randint(6000, 9000)  # Legendary

    def determine_rarity(self):
        stat_power = self.determine_real_power_hidden()
        if stat_power < 3000:
            return 'common'
        elif stat_power < 5000:
            return 'uncommon'
        elif stat_power < 7000:
            return 'rare'
        elif stat_power < 10000:
            return 'epic'
        else:
            return 'legendary'
    
    def determine_real_power_hidden(self):
        real_power_hidden = self.power + self.stats.power

        if hasattr(self, 'sec_stats') and self.sec_stats is not None:
            real_power_hidden += self.sec_stats.power
        if hasattr(self, 'tert_stats') and self.tert_stats is not None:
            real_power_hidden += self.tert_stats.power
        return real_power_hidden
    
    def generate_unique_id(self):
        all_letters = string.ascii_lowercase + string.ascii_uppercase
        while True:
            unid = (
                random.choice(all_letters) +
                random.choice(all_letters) +
                str(random.randint(1, 1000000)).zfill(6) +
                random.choice(all_letters) +
                random.choice(all_letters)
            )
            if unid not in ids:
                ids[unid] = unid
                return unid
    
    def generate_unique_name(self, unid):
        # Extract the integer part of the ID
        integer_part = ''.join(filter(str.isdigit, unid[2:5]))
        # Convert each digit to the corresponding syllable
        name_parts = [random.choice(self.syllable_map[digit]) for digit in integer_part]
        # Combine the syllables to form the unique name
        unique_name = ''.join(name_parts).capitalize()
        return unique_name

    
    def generate_name(self, name):
        flavor = random.choice(self.FLAVOR[self.rarity])
        return f"{flavor} {name}"

    def __repr__(self):
        color = self.COLORS.get(self.rarity, self.RESET)
        output = f"{color}{self.BOLD}[{self.unique_name} - {self.name}]{self.RESET}" if self.unique_name else f"{color}{self.BOLD}[{self.name}]{self.RESET}"
        output += f"\n{color}({self.rarity} {self.type})"
        output += f"\n    POWER: {self.power}"
        output += f"\n {self.stats.stat}: {self.stats.power}"
        
        if hasattr(self, 'sec_stats') and self.sec_stats is not None:
            output += f"\n    {self.sec_stats.stat}: {self.sec_stats.power}"
        
        if hasattr(self, 'tert_stats') and self.tert_stats is not None:
            output += f"\n    {self.tert_stats.stat}: {self.tert_stats.power}"
        
        output += f" {self.RESET}\n"
        output += f" ({self.real_power})\n"

        # Strip ANSI escape codes from output for length calculation
        stripped_output = re.sub(r'\x1b\[[0-9;]*m', '', output)
        # Get the length of the stripped output
        output_length = len(stripped_output)
        # Get the length of the original output including ANSI escape codes
        original_length = len(output)

        # Calculate the difference in length
        length_difference = original_length - output_length

        # Adjust the length of the output to account for ANSI escape codes
        adjusted_output = output[:output_length + length_difference]

        return adjusted_output
