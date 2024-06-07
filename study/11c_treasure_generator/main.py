from items import Item
from collections import Counter


COLORS = {
        'common': '\033[38;5;250m',  # White
        'uncommon': '\033[92m',  # Green
        'rare': '\033[94m',  # Blue
        'epic': '\033[95m',  # Magenta
        'legendary': '\033[38;5;214m'  # Red
    }

items = []

# Generate 1000 random items
items = [Item() for i in range(50)]

# Count occurrences of each rarity
rarity_counts = Counter(item.rarity for item in items)

# Print the counts
for rarity, count in rarity_counts.items():
    print(f"{rarity.capitalize()}: {count}")
print(f"\n---")


for item in items[:5]:
    print(item)

print("Top 5 Most Powerful Items:")
sorted_items = sorted(items, key=lambda x: x.real_power, reverse=True)
for index, item in enumerate(sorted_items[:5], start=1):
    print(f"{index}. {item}")
