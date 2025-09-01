import datetime
delay = datetime.timedelta(days=0)
new_date = datetime.datetime.today() - delay
formatted_date = new_date.strftime('%Y_%m_%d')
host='localhost'

mongo_uri = "mongodb://localhost:27017/"
database = "flipkart_watch"
link_table = "product_url"
pdp_table = "pdp"
