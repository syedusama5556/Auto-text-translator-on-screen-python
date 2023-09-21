import re

# Sample text containing Japanese characters
sample_text = """
View Play Navigate Favourites Help

はミ
に
やっぱり気になる
ゆずさん?(笑)
"""

# Combined regex pattern for matching both Kanji and Hiragana/Katakana
combined_pattern = r'([一-龯ぁ-んァ-ン])'

# Compile the combined regular expression
combined_regex = re.compile(combined_pattern, re.UNICODE)

# Split the sample text into lines
lines = sample_text.strip().split('\n')

# Iterate through each line and find matches
for line in lines:
    matches = combined_regex.findall(line)
    if matches:
        print(f"Matches in line '{line}':")
