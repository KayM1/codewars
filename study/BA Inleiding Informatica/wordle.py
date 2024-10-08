import random

def wordle(word):
    word = word.lower()
    
    while True:
        rslt = ""
        guess = input(f"Enter your guess. (World length ({len(word)})): ").lower()

        if len(guess) != len(word):
            print(f"Your guess must be {len(word)} letters long!")
            continue
        
        for i in range(len(word)):
            if guess[i] == word[i]:
                rslt += "^"
            elif guess[i] in word:
                rslt += "x"
            else:
                rslt += "_"
        
        print("    " + guess)
        print("    " + rslt)
        if rslt == "^"*len(word):
            return False

# Step 1: Generate a dictionary
words_dict = {
    1: "apple",
    2: "banana",
    3: "cherry",
    4: "date",
    5: "elderberry"
}

# Step 2: Randomly select one element (key-value pair)
random_key = random.choice(list(words_dict.keys()))  # Randomly select a key

# Step 3: Convert the selected element to a string
selected_word = words_dict[random_key]  # Get the value associated with the random key
selected_word_as_string = str(selected_word)  # Convert to string

wordle(selected_word_as_string)