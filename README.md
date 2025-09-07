# Romantix E-commerce Scraper

A comprehensive web scraper for extracting product data from Romantix.co.ke, including product names, prices, images, and categories. Built with Python, BeautifulSoup, and Selenium for maximum reliability and anti-blocking capabilities.

## Features

- 🛡️ **Anti-blocking measures**: Random user agents, delays, and request rotation
- 🔄 **Multiple scraping methods**: BeautifulSoup + Requests and Selenium WebDriver
- 📊 **Web Dashboard**: Beautiful red/white themed dashboard for data visualization
- 📁 **Multiple export formats**: CSV and JSON export options
- 🐳 **Docker support**: Easy deployment with Docker and Docker Compose
- 📱 **Responsive design**: Mobile-friendly dashboard interface
- 🔍 **Advanced filtering**: Search, category, and price range filtering
- 📈 **Real-time statistics**: Product counts, categories, and price ranges

## Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone and setup
git clone <repository-url>
cd ecommerce-scrapper

# Run with Docker
docker-compose up --build

# Access dashboard at http://localhost:8080
```

### Option 2: Direct Python

```bash
# Install dependencies
pip install -r requirements.txt

# Run basic scraper
python scraper.py

# Run advanced scraper (with Selenium)
python advanced_scraper.py

# Run dashboard
python dashboard.py
```

## Project Structure

```
ecommerce-scrapper/
├── scraper.py              # Basic scraper with BeautifulSoup
├── advanced_scraper.py     # Advanced scraper with Selenium
├── dashboard.py            # Flask web dashboard
├── templates/
│   └── dashboard.html      # Dashboard template
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
├── setup.py              # Setup script
└── README.md             # This file
```

## Scraping Methods

### Basic Scraper (`scraper.py`)
- Uses BeautifulSoup + Requests
- Lightweight and fast
- Good for simple websites
- Anti-blocking with random user agents and delays

### Advanced Scraper (`advanced_scraper.py`)
- Uses Selenium WebDriver
- Handles JavaScript-rendered content
- More robust against anti-bot measures
- Automatic Chrome driver management

## Dashboard Features

- **Statistics Overview**: Total products, categories, price ranges
- **Product Grid**: Visual product display with images
- **Advanced Filtering**: Search, category, and price filters
- **Export Options**: Download data as CSV or JSON
- **Responsive Design**: Works on desktop and mobile
- **Real-time Updates**: Refresh data without page reload

## Configuration

### Environment Variables
- `PYTHONUNBUFFERED=1`: For Docker logging
- `PYTHONDONTWRITEBYTECODE=1`: Prevent .pyc files

### Scraper Settings
- Random delays between requests (1-3 seconds)
- Multiple user agent rotation
- Request timeout handling
- Automatic retry logic

## Data Output

### CSV Format
```csv
name,price,image_url,category,availability,scraped_at
"Lovense Lush Mini","KSh 26,000.00","https://...","Lovense","In Stock","2025-01-07T..."
```

### JSON Format
```json
[
  {
    "name": "Lovense Lush Mini",
    "price": "KSh 26,000.00",
    "image_url": "https://...",
    "category": "Lovense",
    "availability": "In Stock",
    "scraped_at": "2025-01-07T..."
  }
]
```

## Anti-Blocking Measures

1. **Random User Agents**: Rotates between different browser user agents
2. **Request Delays**: Random delays between requests (1-6 seconds)
3. **Session Management**: Maintains cookies and session state
4. **Header Rotation**: Varies request headers
5. **Selenium Stealth**: Removes automation detection markers
6. **Request Timeouts**: Handles slow responses gracefully

## Usage Examples

### Basic Scraping
```python
from scraper import RomantixScraper

scraper = RomantixScraper()
products = scraper.scrape_all_products()
scraper.save_to_csv("products.csv")
```

### Advanced Scraping
```python
from advanced_scraper import AdvancedRomantixScraper

scraper = AdvancedRomantixScraper(use_selenium=True)
products = scraper.scrape_all_products()
scraper.save_to_json("products.json")
scraper.close()
```

### Dashboard API
```python
# Get all products
GET /api/products

# Get statistics
GET /api/stats

# Get categories
GET /api/categories

# Export CSV
GET /export/csv
```

## Docker Commands

```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild and run
docker-compose up --build --force-recreate
```

## Troubleshooting

### Common Issues

1. **Chrome Driver Issues**
   - The advanced scraper automatically downloads ChromeDriver
   - Ensure Chrome browser is installed

2. **Blocked Requests**
   - Increase delays between requests
   - Use the advanced scraper with Selenium
   - Check if the website structure has changed

3. **No Products Found**
   - Website structure may have changed
   - Check network connectivity
   - Verify the target URL is accessible

4. **Docker Issues**
   - Ensure Docker is running
   - Check port 8080 is available
   - Review Docker logs for errors

### Debug Mode

```bash
# Run scraper with debug logging
python -c "
import logging
logging.basicConfig(level=logging.DEBUG)
from scraper import RomantixScraper
scraper = RomantixScraper()
scraper.scrape_all_products()
"
```

## Legal Notice

This scraper is for educational and research purposes only. Please ensure you comply with the website's terms of service and robots.txt file. Always respect rate limits and be considerate of the target website's resources.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the logs for error messages
3. Open an issue on GitHub
4. Ensure you're using the latest version

---

**Happy Scraping! 🚀**
