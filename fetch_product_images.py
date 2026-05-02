#!/usr/bin/env python3
"""
Fetches Amazon product images by scraping the product page for the
high-res image URL embedded in the page's JSON data.
"""

import os
import re
import json
import urllib.request
import urllib.error
import yaml

PRODUCTS_FILE = "_data/products.yml"
OUTPUT_DIR = "assets/images/products"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}

def get_hires_image_url(asin):
    """Scrape the Amazon product page and extract the highest-res image URL."""
    product_url = f"https://www.amazon.com/dp/{asin}"
    req = urllib.request.Request(product_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode("utf-8", errors="ignore")

        # Amazon embeds image data as JSON in 'data-a-dynamic-image' attributes
        # Pattern: data-a-dynamic-image='{"url": [w, h], ...}'
        matches = re.findall(r'data-a-dynamic-image=["\'](\{[^"\']+\})["\']', html)
        best_url = None
        best_area = 0
        for match in matches:
            try:
                images = json.loads(match.replace("&quot;", '"'))
                for url, dims in images.items():
                    if isinstance(dims, list) and len(dims) == 2:
                        area = dims[0] * dims[1]
                        if area > best_area:
                            best_area = area
                            best_url = url
            except Exception:
                continue

        if best_url:
            return best_url

        # Fallback: look for landingImageUrl in page JSON
        m = re.search(r'"landingImageUrl"\s*:\s*"([^"]+)"', html)
        if m:
            return m.group(1).replace("\\u0026", "&")

    except Exception as e:
        print(f"  ✗ Page fetch failed ({e})")
    return None

def fetch_image(asin):
    image_url = get_hires_image_url(asin)
    if not image_url:
        return None, None

    req = urllib.request.Request(image_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            if response.status == 200:
                content_type = response.headers.get("Content-Type", "")
                if "image" in content_type:
                    data = response.read()
                    print(f"  ↳ {len(data)//1024}KB from {image_url[:60]}...")
                    return data, image_url
    except Exception as e:
        print(f"  ✗ Image download failed ({e})")
    return None, None

def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(PRODUCTS_FILE, "r") as f:
        data = yaml.safe_load(f)

    changed = False
    categories = data.get("categories", {})

    for cat_key, category in categories.items():
        for product in category.get("products", []):
            asin = product.get("asin")
            name = product.get("name", "product")

            if not asin:
                continue

            # Always re-fetch to get higher quality
            pass

            print(f"Fetching: {name} (ASIN: {asin})")
            image_data, source_url = fetch_image(asin)

            if image_data:
                filename = f"{slugify(name)}.jpg"
                filepath = os.path.join(OUTPUT_DIR, filename)
                with open(filepath, "wb") as img_file:
                    img_file.write(image_data)
                jekyll_path = f"/{OUTPUT_DIR}/{filename}"
                product["image"] = jekyll_path
                changed = True
                print(f"  ✓ Saved to {jekyll_path}")
            else:
                print(f"  ✗ No image found for {name}")

    if changed:
        with open(PRODUCTS_FILE, "w") as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        print("\n✅ products.yml updated with image paths.")
    else:
        print("\nNo changes made.")

if __name__ == "__main__":
    main()
