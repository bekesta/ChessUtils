#!/usr/bin/env python3

import re
import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} input.pgn output.pgn")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

puzzle_num = 0

def rename_puzzle(match):
    global puzzle_num
    puzzle_num += 1

    game = match.group(0)
    title = f"Puzzle {puzzle_num}"

    # Replace the Event tag
    game = re.sub(
        r'^\[Event\s+"[^"]*"\]',
        f'[Event "{title}"]',
        game,
        count=1,
        flags=re.MULTILINE,
    )

    return game


# Each game starts with an [Event ...] tag.
games = re.split(r'(?=^\[Event\s+")', text, flags=re.MULTILINE)

output = ""

for game in games:
    if game.startswith("[Event "):
        output += rename_puzzle(re.match(r'(?s).*', game))
    else:
        output += game

with open(output_file, "w", encoding="utf-8") as f:
    f.write(output)

print(f"Renamed {puzzle_num} puzzles.")
print(f"Wrote {output_file}")
