import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random
from collections import Counter

# User params
csv_file = 'wikipedia_data_science.csv'  # Specify the CSV file to read data from
png_file = 'logo_text_mask.png'  # Specify the PNG file to read mask from.
# Mask image should have white background RGB(255,255,255) and black mask region RGB(0,0,0).
# The DPI of the cloud depends of the PNG file size!

use_desired_color = True  # Set to True if you want to use a specific color for words
cloud_desired_color = "rgb(0, 0, 0)"  # Define the desired color in RGB format

use_random_color = True  # Set to True if you want to use random colors for words

# Define a dictionary for random RGB color ranges
crc = {
    'r': (0, 255),  # Range of red component from 0 to 255
    'g': (0, 255),  # Range of green component from 0 to 255
    'b': (0, 255)   # Range of blue component from 0 to 255
}

cloud_width = 1800  # Width of the WordCloud image
cloud_height = 500  # Height of the WordCloud image

repeat_words = True  # Set to True to allow word repetitions in the WordCloud

background_color = 'white'  # Set background color for the WordCloud

# Load a CSV file with single words spread across consecutive rows of a single column
df = pd.read_csv(csv_file)

# Convert 'Words' column to a list
words = df['Words'].tolist()

# Convert all words to lowercase and count word frequencies
words_frequencies = dict(Counter(word.lower() for word in words))

# Load a mask image
mask = np.array(Image.open(png_file))


# Define a custom color functions
def desired_color(word, font_size, position, orientation, font_path, random_state):
    return cloud_desired_color


def random_color(word, font_size, position, orientation, font_path, random_state):
    # Generate a random RGB color
    r = random.randint(crc['r'][0], crc['r'][1])
    g = random.randint(crc['g'][0], crc['g'][1])
    b = random.randint(crc['b'][0], crc['b'][1])
    return f"rgb({r}, {g}, {b})"


if use_desired_color:
    color_func = desired_color
elif use_random_color:
    color_func = random_color
else:
    color_func = None

# Create the WordCloud object with custom parameters
wordcloud = WordCloud(
    background_color=background_color,
    repeat=repeat_words,
    width=cloud_width,
    height=cloud_height,
    mask=mask,
    color_func=color_func
)

# Generate the word cloud using word frequencies or relevance values
wordcloud.generate_from_frequencies(words_frequencies)

plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
plt.show()
