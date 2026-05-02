---
layout: page
title: Learning
permalink: /essentials/learning/
---

# Learning

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
