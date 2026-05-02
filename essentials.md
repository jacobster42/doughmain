---
layout: page
title: Essentials
permalink: /essentials/
---

# Essential Baking Tools & Equipment

After years of testing and countless loaves, these are the tools that consistently deliver professional results in a home kitchen. Each recommendation is chosen for reliability, accuracy, and value.

<div class="section-cards">
  {% for section in site.data.products.sections %}
  {% assign s = section[1] %}
  <a class="section-card" href="#{{ s.id }}" onclick="var el=document.getElementById('{{ s.id }}');if(el){el.open=true;}">
    <div class="section-card-title">{{ s.title }}</div>
    <div class="section-card-desc">{{ s.description }}</div>
  </a>
  {% endfor %}
</div>

<details id="must-haves" class="product-section">
<summary><h2>The Must-Haves</h2></summary>

{% assign must_haves = "kitchen_scales,stand_mixers,bench_scrapers,mixing_bowls" | split: "," %}
{% for category_key in must_haves %}
  {% assign category = site.data.products.categories[category_key] %}
<h3>{{ category.title }}</h3>
<p>{{ category.description }}</p>
<div class="product-grid">
{% for product in category.products %}
<a class="product-card" href="{{ site.data.products.base_amazon_url }}{{ product.asin }}?tag={{ site.data.products.affiliate_tag }}">
  <div class="product-image-wrap">
    {% if product.image %}<img src="{{ product.image }}" alt="{{ product.name }}">
    {% else %}<div class="product-image-placeholder">&#9744;</div>{% endif %}
    {% if product.personal_favorite %}<span class="personal-favorite-badge">My Pick</span>{% endif %}
  </div>
  <div class="product-info">
    <h4>{{ product.name }}</h4>
    {% if product.price != "" %}<div class="product-price">{{ product.price }}</div>{% endif %}
  </div>
</a>
{% endfor %}
</div>
{% endfor %}
</details>

<details id="precision" class="product-section">
<summary><h2>Precision Instruments</h2></summary>

{% assign precision = "thermometers,oven_thermometers" | split: "," %}
{% for category_key in precision %}
  {% assign category = site.data.products.categories[category_key] %}
<h3>{{ category.title }}</h3>
<p>{{ category.description }}</p>
<div class="product-grid">
{% for product in category.products %}
<a class="product-card" href="{{ site.data.products.base_amazon_url }}{{ product.asin }}?tag={{ site.data.products.affiliate_tag }}">
  <div class="product-image-wrap">
    {% if product.image %}<img src="{{ product.image }}" alt="{{ product.name }}">
    {% else %}<div class="product-image-placeholder">&#9744;</div>{% endif %}
    {% if product.personal_favorite %}<span class="personal-favorite-badge">My Pick</span>{% endif %}
  </div>
  <div class="product-info">
    <h4>{{ product.name }}</h4>
    {% if product.price != "" %}<div class="product-price">{{ product.price }}</div>{% endif %}
  </div>
</a>
{% endfor %}
</div>
{% endfor %}
</details>

<details id="baking" class="product-section">
<summary><h2>Baking Vessels</h2></summary>

{% assign baking = "loaf_pans,dutch_ovens,proofing_baskets,baking_mats" | split: "," %}
{% for category_key in baking %}
  {% assign category = site.data.products.categories[category_key] %}
<h3>{{ category.title }}</h3>
<p>{{ category.description }}</p>
<div class="product-grid">
{% for product in category.products %}
<a class="product-card" href="{{ site.data.products.base_amazon_url }}{{ product.asin }}?tag={{ site.data.products.affiliate_tag }}">
  <div class="product-image-wrap">
    {% if product.image %}<img src="{{ product.image }}" alt="{{ product.name }}">
    {% else %}<div class="product-image-placeholder">&#9744;</div>{% endif %}
    {% if product.personal_favorite %}<span class="personal-favorite-badge">My Pick</span>{% endif %}
  </div>
  <div class="product-info">
    <h4>{{ product.name }}</h4>
    {% if product.price != "" %}<div class="product-price">{{ product.price }}</div>{% endif %}
  </div>
</a>
{% endfor %}
</div>
{% endfor %}
</details>

<details id="tools" class="product-section">
<summary><h2>Hand Tools</h2></summary>

{% assign hand_tools = "bread_lames,dough_whisks,rolling_pins" | split: "," %}
{% for category_key in hand_tools %}
  {% assign category = site.data.products.categories[category_key] %}
<h3>{{ category.title }}</h3>
<p>{{ category.description }}</p>
<div class="product-grid">
{% for product in category.products %}
<a class="product-card" href="{{ site.data.products.base_amazon_url }}{{ product.asin }}?tag={{ site.data.products.affiliate_tag }}">
  <div class="product-image-wrap">
    {% if product.image %}<img src="{{ product.image }}" alt="{{ product.name }}">
    {% else %}<div class="product-image-placeholder">&#9744;</div>{% endif %}
    {% if product.personal_favorite %}<span class="personal-favorite-badge">My Pick</span>{% endif %}
  </div>
  <div class="product-info">
    <h4>{{ product.name }}</h4>
    {% if product.price != "" %}<div class="product-price">{{ product.price }}</div>{% endif %}
  </div>
</a>
{% endfor %}
</div>
{% endfor %}
</details>

<details id="specialty" class="product-section">
<summary><h2>Pretzel Specialty</h2></summary>

{% assign specialty = "pretzel_essentials,pizza_steel" | split: "," %}
{% for category_key in specialty %}
  {% assign category = site.data.products.categories[category_key] %}
<h3>{{ category.title }}</h3>
<p>{{ category.description }}</p>
<div class="product-grid">
{% for product in category.products %}
<a class="product-card" href="{{ site.data.products.base_amazon_url }}{{ product.asin }}?tag={{ site.data.products.affiliate_tag }}">
  <div class="product-image-wrap">
    {% if product.image %}<img src="{{ product.image }}" alt="{{ product.name }}">
    {% else %}<div class="product-image-placeholder">&#9744;</div>{% endif %}
    {% if product.personal_favorite %}<span class="personal-favorite-badge">My Pick</span>{% endif %}
  </div>
  <div class="product-info">
    <h4>{{ product.name }}</h4>
    {% if product.price != "" %}<div class="product-price">{{ product.price }}</div>{% endif %}
  </div>
</a>
{% endfor %}
</div>
{% endfor %}
</details>

<details id="reading" class="product-section">
<summary><h2>Essential Reading</h2></summary>

{% assign category = site.data.products.categories.essential_reading %}
<p>{{ category.description }}</p>
<div class="product-grid">
{% for product in category.products %}
<a class="product-card" href="{{ site.data.products.base_amazon_url }}{{ product.asin }}?tag={{ site.data.products.affiliate_tag }}">
  <div class="product-image-wrap">
    {% if product.image %}<img src="{{ product.image }}" alt="{{ product.name }}">
    {% else %}<div class="product-image-placeholder">&#9744;</div>{% endif %}
    {% if product.personal_favorite %}<span class="personal-favorite-badge">My Pick</span>{% endif %}
  </div>
  <div class="product-info">
    <h4>{{ product.name }}</h4>
    {% if product.price != "" %}<div class="product-price">{{ product.price }}</div>{% endif %}
  </div>
</a>
{% endfor %}
</div>
</details>
