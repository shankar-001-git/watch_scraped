from itemadapter import ItemAdapter
from pymongo import MongoClient
from flipkart_watches import db_config as db
from flipkart_watches.items import FlipkartWatchesItem


class FlipkartWatchesPipeline:
    def __init__(self):
        # MongoDB connection
        self.client = MongoClient(db.mongo_uri)  # example: "mongodb://localhost:27017/"
        self.db = self.client[db.database]       # database name
        self.link_collection = self.db[db.link_table]  # PLP collection
        self.pdp_collection = self.db[db.pdp_table]    # PDP collection

    def process_item(self, item, spider):
        if isinstance(item, FlipkartWatchesItem):
            collection = self.pdp_collection
        else:
            collection = self.link_collection

        try:
            # Insert or update (avoids duplicates by URL)
            collection.update_one(
                {"product_url": item.get("product_url")},
                {"$set": dict(item)},
                upsert=True
            )
            print(f"Inserted/Updated: {item.get('product_url')}")
        except Exception as e:
            print("Error inserting into MongoDB:", e)

        return item

    def close_spider(self, spider):
        self.client.close()
