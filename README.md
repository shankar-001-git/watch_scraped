# Flipkart Watches Scraper

A Python project to scrape watch product data from Flipkart. It collects product URLs and then scrapes detailed info for each watch, storing everything in MongoDB.

## Features

* Collects product URLs from Flipkart’s watch category (PLP).
* Scrapes detailed product info (PDP) like name, price, brand, description, images.
* Saves data to MongoDB and avoids duplicates using `product_url` as a unique key.
* Easy to configure MongoDB settings and Scrapy parameters.

## Setup

1. Clone the repo:

```bash
git clone <repository_url>
cd FLIPKART_w

```bash
pip install Scrapy pymongo curl_cffi parsel
```

4. Make sure MongoDB is installed and running.

## Usage

### 1. Collect Product URLs (PLP)

python product_url.py


### 2. Scrape Product Details (PDP)

Create and run your Scrapy spider:

bash
scrapy crawl flipkart_pdp_scraper

The spider reads pending URLs from MongoDB, scrapes the product data, and updates the status to `scraped`.

## MongoDB Integration

* `db_config.py` holds MongoDB URI, database, and collection names.
* `pipelines.py` inserts or updates scraped items in MongoDB using `product_url` as a unique key.

## Notes

* Flipkart’s site structure and anti-bot measures may change—update selectors, headers, or cookies as needed.
* Ensure `ROBOTSTXT_OBEY = False` if you want to bypass robots.txt (do this responsibly).
* Use `extract_digits` from `custom_function.py` to clean prices or numeric fields.

