#!/usr/bin/env python3
"""
Uses Claude API to analyze and fix fuzzy images and uneven card sizes.
"""

import anthropic
import re

client = anthropic.Anthropic()

# Read current SCSS
with open("assets/main.scss", "r") as f:
    scss = f.read()

# Read current essentials.md
with open("essentials.md", "r") as f:
    html = f.read()

prompt = """You are fixing a Jekyll/SCSS product card layout. Here are the two problems:

1. IMAGES ARE FUZZY: The images are low-resolution Amazon CDN thumbnails (156x153px) being displayed at a larger size, causing blur. Fix this by using CSS to display them at a maximum of their native size, centered in the square container with a neutral background filling the rest. Do NOT upscale them beyond 100% of their natural size — use `object-fit: contain` with `max-width: 156px; max-height: 156px` clamped inside the container so they never stretch.

2. CARDS ARE UNEVEN: Cards in the same grid row have different heights because title text wraps to different lengths. Fix this by making the entire `.product-card` a fixed height (e.g. 280px) using CSS grid internally — image area gets a fixed pixel height (180px), info area fills the rest. Titles must be clamped to exactly 2 lines with `-webkit-line-clamp`. The grid itself should use `align-items: stretch`.

Here is the current SCSS product card block (between the markers):
--- SCSS START ---
""" + re.search(r'// Product grid.*?(?=\n// [A-Z])', scss, re.DOTALL).group(0) + """
--- SCSS END ---

Return ONLY the replacement SCSS block for `.product-grid` and `.product-card` — no explanation, no markdown fences, just the raw SCSS starting with `// Product grid`."""

print("Sending to Claude API...")

with client.messages.stream(
    model="claude-opus-4-6",
    max_tokens=4000,
    thinking={"type": "adaptive"},
    messages=[{"role": "user", "content": prompt}]
) as stream:
    new_scss = stream.get_final_message()

result = ""
for block in new_scss.content:
    if block.type == "text":
        result += block.text

print("Claude response received.")
print("--- Generated SCSS ---")
print(result[:500], "...")

# Replace the product grid + card block in main.scss
old_block = re.search(r'// Product grid.*?(?=\n// [A-Z]|\Z)', scss, re.DOTALL).group(0)
new_scss_content = scss.replace(old_block, result.strip() + "\n\n")

with open("assets/main.scss", "w") as f:
    f.write(new_scss_content)

print("✅ assets/main.scss updated.")
