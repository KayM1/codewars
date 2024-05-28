from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import random
import io
import os

app = Flask(__name__)

# List of quotes
quotes = [
    "The only limit to our realization of tomorrow \n is our doubts of today.",
    "The purpose of our lives is to be happy.",
    "Life is what happens when you're busy making \n other plans.",
    "Get busy living or get busy dying.",
    "You have within you right now, everything you \n need to deal with whatever the world can throw at you."
]

sprite_dir = 'sprites'

@app.route('/banner.jpeg')
def banner():
    # Select a random quote
    quote = random.choice(quotes)

    # Create an image
    img = Image.new('RGB', (800, 100), color=(255, 255, 255))

    # Initialize ImageDraw
    d = ImageDraw.Draw(img)

    # Use a truetype font
    try:
        # You can use any TTF font file available in your system
        font = ImageFont.truetype("arial.ttf", 35)
        print("boop")
    except IOError:
        font = ImageFont.load_default(20)

    # Define text position and color
    text_color = (0, 0, 0)
    text_position = (10, 20)

    # Add text to image
    d.text(text_position, quote, font=font, fill=text_color)

    ## SPRITES

    # Get a list of sprite images
    sprite_files = [f for f in os.listdir(sprite_dir) if os.path.isfile(os.path.join(sprite_dir, f))]

    # Select a random sprite
    if sprite_files:
        sprite_path = os.path.join(sprite_dir, random.choice(sprite_files))
        sprite = Image.open(sprite_path).convert('RGBA')
        sprite = sprite.resize((100, 100))

        # Paste the sprite onto the banner image (top-left corner)
        img.paste(sprite, (715, 20), sprite if sprite.mode == 'RGBA' else None)

    # Save image to a bytes buffer
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    buffer.seek(0)

    return send_file(buffer, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)