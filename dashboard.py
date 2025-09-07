from flask import Flask, render_template, jsonify, request
import json
import csv
import os
from datetime import datetime
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('dashboard.log', mode='w', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)
logger.info("🚀 Dashboard initialized")

def load_products():
    """Load products from JSON file"""
    try:
        if os.path.exists('romantix_products.json'):
            with open('romantix_products.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except Exception as e:
        logger.error(f"Error loading products: {e}")
        return []

def get_stats(products):
    """Calculate statistics from products"""
    if not products:
        return {
            'total_products': 0,
            'categories': 0,
            'price_range': 'N/A',
            'last_updated': 'N/A'
        }
    
    categories = set(p.get('category', 'Unknown') for p in products)
    prices = []
    
    for product in products:
        price_str = product.get('price', '')
        # Extract numeric price
        try:
            price = float(''.join(filter(str.isdigit, price_str.replace(',', ''))))
            if price > 0:
                prices.append(price)
        except:
            continue
    
    return {
        'total_products': len(products),
        'categories': len(categories),
        'price_range': f"KSh {min(prices):,.0f} - KSh {max(prices):,.0f}" if prices else 'N/A',
        'last_updated': products[0].get('scraped_at', 'N/A') if products else 'N/A'
    }

@app.route('/')
def index():
    """Main dashboard page"""
    products = load_products()
    stats = get_stats(products)
    return render_template('dashboard.html', products=products, stats=stats)

@app.route('/api/products')
def api_products():
    """API endpoint for products data"""
    products = load_products()
    return jsonify(products)

@app.route('/api/stats')
def api_stats():
    """API endpoint for statistics"""
    products = load_products()
    stats = get_stats(products)
    return jsonify(stats)

@app.route('/api/categories')
def api_categories():
    """API endpoint for categories"""
    products = load_products()
    categories = {}
    
    for product in products:
        category = product.get('category', 'Unknown')
        if category not in categories:
            categories[category] = 0
        categories[category] += 1
    
    return jsonify(categories)

@app.route('/export/csv')
def export_csv():
    """Export products as CSV"""
    products = load_products()
    
    # Create CSV response
    output = []
    for product in products:
        output.append({
            'Name': product.get('name', ''),
            'Price': product.get('price', ''),
            'Category': product.get('category', ''),
            'Availability': product.get('availability', ''),
            'Image URL': product.get('image_url', ''),
            'Scraped At': product.get('scraped_at', '')
        })
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
