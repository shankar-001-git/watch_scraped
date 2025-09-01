import hashlib
import random
import os
import datetime
delay = datetime.timedelta(days=0)
new_date = datetime.datetime.today() - delay
formatted_date = new_date.strftime('%Y_%m_%d')
from scrapy.cmdline import execute
import pymysql
import scrapy
import pymysql .cursors
from flipkart_watches import db_config as db
from flipkart_watches.custom_function import *
from flipkart_watches.items import FlipkartWatchesItem
folder_path = fr'D:\Santosh\All_PAGE_SAVE\flipkart_watches\product_url_data_{formatted_date}'
os.makedirs(folder_path ,exist_ok=True)
class PdpDataSpider(scrapy.Spider):
    name = "pdp_data"
    cookies = {
        'Network-Type': '4g',
        'T': 'TI175197410009300150749015058904626350761183500924374943512863979236',
        'rt': 'null',
        'K-ACTION': 'null',
        'ud': '0.kg-XnFW5gcfK9f7SstW1IHWtFGQ4PsE9BiR7cXzDh7ZdChKOEQNhdwtbKMDdDNfCA53XxogF7xk46d2sIeAZmMdnhO8kVTHRuk55chpJBOrBkMA1Cvs2tdnNvGyEg_W2GYK0KT8Szohpj0Ei-bMS3g',
        'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3NTczOTk5MDksImlhdCI6MTc1NTY3MTkwOSwiaXNzIjoia2V2bGFyIiwianRpIjoiNzZjZGQyOTctZDY1Ny00ZDZiLTk4YTQtNWQyODg0MDg5NWYwIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzUxOTc0MTAwMDkzMDAxNTA3NDkwMTUwNTg5MDQ2MjYzNTA3NjExODM1MDA5MjQzNzQ5NDM1MTI4NjM5NzkyMzYiLCJrZXZJZCI6IlZJNDdBOUNENjY3RUI3NEQ2Nzk2M0EwMjM2RDA3Mjc3NkIiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.hvqbnS8sjLE0zxYMtb8jBuuVEbDJfc30o3CnvV4c-5U',
        'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20321%7CMCMID%7C19483144267122342160392425720158975437%7CMCAAMLH-1756276709%7C12%7CMCAAMB-1756276709%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1755679109s%7CNONE%7CMCAID%7CNONE',
        'vh': '551',
        'vw': '1280',
        'dpr': '1.5',
        'fonts-loaded': 'en_loaded',
        'isH2EnabledBandwidth': 'true',
        'h2NetworkBandwidth': '9',
        'qH': '959e134ef548e173',
        '_gcl_au': '1.1.235898740.1755775912',
        'S': 'd1t17Pz8/Ayo/Yj8/Pz8/JD9FetBeZUP8Vp/ji/a8ceP7vN+9W0Kyg88Seb+xbw1aOpqry5YA2hYmjzF400Zk6czXaw==',
        'Network-Type': '4g',
        'vd': 'VI47A9CD667EB74D67963A0236D072776B-1751974102787-7.1755783225.1755779636.153331507',
        'SN': 'VI47A9CD667EB74D67963A0236D072776B.TOK7E059C9CF75A4AB7947FC3F39FA7A28A.1755783234317.LO',
        's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Adaniel-radcliffe-drm-pe-silver-white-professional-edge-analog-watch-men%25253Ap%25253Aitm98edf6d7c2f3f%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
        'solved_captcha': '1755784417-18435-58665600-f45196b4ced412aaed5e258b6b05f6e4882d97efc1a73c1bb8f6333d05bbd19f',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'https://www.flipkart.com/daniel-radcliffe-drm-pe-silver-white-professional-edge-analog-watch-men/p/itm98edf6d7c2f3f?pid=WATGXTYAHDGNQDHZ&lid=LSTWATGXTYAHDGNQDHZFPKY8P&marketplace=FLIPKART&q=watches+for+men&store=r18%2Ff13&srno=s_1_8&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&fm=organic&iid=c0bc6e25-4073-4677-924c-bdf5671f2ae7.WATGXTYAHDGNQDHZ.SEARCH&ppt=None&ppn=None&ssid=vc0q59299s0000001755781423387&qH=959e134ef548e173',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version': '"139.0.7258.128"',
        'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Google Chrome";v="139.0.7258.128", "Chromium";v="139.0.7258.128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"19.0.0"',
        # 'Cookie': 'Network-Type=4g; T=TI175197410009300150749015058904626350761183500924374943512863979236; rt=null; K-ACTION=null; ud=0.kg-XnFW5gcfK9f7SstW1IHWtFGQ4PsE9BiR7cXzDh7ZdChKOEQNhdwtbKMDdDNfCA53XxogF7xk46d2sIeAZmMdnhO8kVTHRuk55chpJBOrBkMA1Cvs2tdnNvGyEg_W2GYK0KT8Szohpj0Ei-bMS3g; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3NTczOTk5MDksImlhdCI6MTc1NTY3MTkwOSwiaXNzIjoia2V2bGFyIiwianRpIjoiNzZjZGQyOTctZDY1Ny00ZDZiLTk4YTQtNWQyODg0MDg5NWYwIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzUxOTc0MTAwMDkzMDAxNTA3NDkwMTUwNTg5MDQ2MjYzNTA3NjExODM1MDA5MjQzNzQ5NDM1MTI4NjM5NzkyMzYiLCJrZXZJZCI6IlZJNDdBOUNENjY3RUI3NEQ2Nzk2M0EwMjM2RDA3Mjc3NkIiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.hvqbnS8sjLE0zxYMtb8jBuuVEbDJfc30o3CnvV4c-5U; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20321%7CMCMID%7C19483144267122342160392425720158975437%7CMCAAMLH-1756276709%7C12%7CMCAAMB-1756276709%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1755679109s%7CNONE%7CMCAID%7CNONE; vh=551; vw=1280; dpr=1.5; fonts-loaded=en_loaded; isH2EnabledBandwidth=true; h2NetworkBandwidth=9; qH=959e134ef548e173; _gcl_au=1.1.235898740.1755775912; S=d1t17Pz8/Ayo/Yj8/Pz8/JD9FetBeZUP8Vp/ji/a8ceP7vN+9W0Kyg88Seb+xbw1aOpqry5YA2hYmjzF400Zk6czXaw==; Network-Type=4g; vd=VI47A9CD667EB74D67963A0236D072776B-1751974102787-7.1755783225.1755779636.153331507; SN=VI47A9CD667EB74D67963A0236D072776B.TOK7E059C9CF75A4AB7947FC3F39FA7A28A.1755783234317.LO; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Adaniel-radcliffe-drm-pe-silver-white-professional-edge-analog-watch-men%25253Ap%25253Aitm98edf6d7c2f3f%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; solved_captcha=1755784417-18435-58665600-f45196b4ced412aaed5e258b6b05f6e4882d97efc1a73c1bb8f6333d05bbd19f',
    }
    BROWSER_VERSIONS = [
        "chrome99", "chrome100", "chrome101", "chrome104", "chrome107", "chrome110",
        "chrome116", "chrome119", "chrome120", "chrome123",
        "chrome99_android", "edge99", "edge101", "safari15_3", "safari15_5",
        "safari17_0", "safari17_2_ios"
    ]
    def __init__(self):
        super().__init__()
        self.con = pymysql.connect(user=db.user, host=db.host, password=db.password, database=db.database,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
        self.link_table = db.link_table
    def start_requests(self):
        self.cur.execute(f"select * from {self.link_table} where status ='pending'")
        result = self.cur.fetchall()
        for raw in result:
            product_url = raw['product_url']
            start_urls=product_url
            page_save_id = int(hashlib.md5(bytes(f"{start_urls}", "utf8")).hexdigest(), 16) % (10 ** 10)
            file_name = os.path.join(folder_path, f'{page_save_id}.html')
            if not os.path.exists(file_name):
                yield scrapy.Request(
                    url=start_urls,
                    callback=self.parse,
                    headers=self.headers,
                    cookies=self.cookies,
                    meta={"impersonate":random.choice(self.BROWSER_VERSIONS)},
                    dont_filter=True,
                    cb_kwargs={"page_save_id": page_save_id,"start_urls":start_urls}
                )
            else:
                yield scrapy.Request(url=f"file:///{file_name}", callback=self.parse, dont_filter=True,
                                     cb_kwargs={"page_save_id": page_save_id,"start_urls":start_urls})


    def parse(self, response,**kwargs):
        if response.status==200:
            product_url=kwargs['start_urls']
            page_save_id=kwargs['page_save_id']
            self.page_save(page_save_id, response)
            List_Price = response.xpath('//div[@class="C7fEHH"]//div[contains(@class, "Nx9bqj")]/text()').get()
            Price = extract_digits(List_Price)
            Price = extract_digits(List_Price)

            # Convert price to integer for comparison
            try:
                Price_int = int(Price)
            except ValueError:
                Price_int = 0
            if Price_int <= 2000:
                item=FlipkartWatchesItem()
                product_Name=response.xpath('//div[@class="C7fEHH"]/div/h1[@class="_6EBuvT"]/span[@class="VU-ZEz"]/text()').get()
                Brand=response.xpath('//div[@class="C7fEHH"]/div/h1[@class="_6EBuvT"]/span[@class="mEh187"]/text()').get()
                brand_name=''.join(Brand.split('\xa0'))
                Availability = "Out of Stock" if response.xpath('//div[@class="Z8JjpR"]/text()').get() == ["Sold Out"] else "In Stock"
                price=Price_int
                item['product_url']=product_url
                item['watch_Name']=product_Name
                item['brand']=brand_name
                item['Available']=Availability
                item['price']=price
                item['page_id']=page_save_id
                yield item
    def page_save(self, hash_key, response):
        file_name = os.path.join(folder_path, f'{hash_key}.html')
        if not os.path.exists(file_name):
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print("------------", hash_key, "------------- Page Save Done ----------")
        else:
            print("********* THIS PAGE IS ALREADY SAVE **********", hash_key)





if __name__ == '__main__':
    execute('scrapy crawl pdp_data'.split())