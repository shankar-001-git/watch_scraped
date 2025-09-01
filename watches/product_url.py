from curl_cffi import requests
from parsel import Selector
from pymongo import MongoClient

cookies = {
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
    'Network-Type': '4g',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aprovogue-premium-gifting-watch-man-boys-trending-quality-day-date-functioning-analog-men%25253Ap%25253Aitma75134bb65010%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
    'vd': 'VI47A9CD667EB74D67963A0236D072776B-1751974102787-7.1755781305.1755779636.153290545',
    'S': 'd1t17Pz8/Ayo/Yj8/Pz8/JD9FetBeZUP8Vp/ji/a8ceP7vN+9W0Kyg88Seb+xbw1aOpqry5YA2hYmjzF400Zk6czXaw==',
    'SN': 'VI47A9CD667EB74D67963A0236D072776B.TOK3497BC6F45F54B46B8891410EC984584.1755781310007.LO',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://www.flipkart.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
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
    # 'Cookie': 'T=TI175197410009300150749015058904626350761183500924374943512863979236; rt=null; K-ACTION=null; ud=0.kg-XnFW5gcfK9f7SstW1IHWtFGQ4PsE9BiR7cXzDh7ZdChKOEQNhdwtbKMDdDNfCA53XxogF7xk46d2sIeAZmMdnhO8kVTHRuk55chpJBOrBkMA1Cvs2tdnNvGyEg_W2GYK0KT8Szohpj0Ei-bMS3g; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3NTczOTk5MDksImlhdCI6MTc1NTY3MTkwOSwiaXNzIjoia2V2bGFyIiwianRpIjoiNzZjZGQyOTctZDY1Ny00ZDZiLTk4YTQtNWQyODg0MDg5NWYwIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzUxOTc0MTAwMDkzMDAxNTA3NDkwMTUwNTg5MDQ2MjYzNTA3NjExODM1MDA5MjQzNzQ5NDM1MTI4NjM5NzkyMzYiLCJrZXZJZCI6IlZJNDdBOUNENjY3RUI3NEQ2Nzk2M0EwMjM2RDA3Mjc3NkIiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.hvqbnS8sjLE0zxYMtb8jBuuVEbDJfc30o3CnvV4c-5U; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20321%7CMCMID%7C19483144267122342160392425720158975437%7CMCAAMLH-1756276709%7C12%7CMCAAMB-1756276709%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1755679109s%7CNONE%7CMCAID%7CNONE; vh=551; vw=1280; dpr=1.5; fonts-loaded=en_loaded; isH2EnabledBandwidth=true; h2NetworkBandwidth=9; qH=959e134ef548e173; _gcl_au=1.1.235898740.1755775912; Network-Type=4g; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aprovogue-premium-gifting-watch-man-boys-trending-quality-day-date-functioning-analog-men%25253Ap%25253Aitma75134bb65010%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; vd=VI47A9CD667EB74D67963A0236D072776B-1751974102787-7.1755781305.1755779636.153290545; S=d1t17Pz8/Ayo/Yj8/Pz8/JD9FetBeZUP8Vp/ji/a8ceP7vN+9W0Kyg88Seb+xbw1aOpqry5YA2hYmjzF400Zk6czXaw==; SN=VI47A9CD667EB74D67963A0236D072776B.TOK3497BC6F45F54B46B8891410EC984584.1755781310007.LO',
}

params = {
    'q': 'watches for men',
    'sid': 'r18,f13',
    'as': 'on',
    'as-show': 'on',
    'otracker': 'AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na',
    'otracker1': 'AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na',
    'as-pos': '1',
    'as-type': 'RECENT',
    'suggestionId': 'watches for men|Wrist Watches',
    'requestId': 'bcbfcbdf-1b86-444c-9c70-464a5e5fd20e',
    'as-searchtext': 'watches for men',
    'p[]': [
        'facets.price_range.from=Min',
        'facets.price_range.to=2000',
    ],
}

try:
    # MongoDB connection (Change URI if needed)
    client = MongoClient("mongodb://localhost:27017/")
    db = client["flipkart_watch"]
    collection = db["product_list"]

    print("Connected to MongoDB ✅")

    response = requests.get('https://www.flipkart.com/search',
                            params=params, cookies=cookies, headers=headers)

    if response.status_code == 200:
        selector = Selector(response.text)
        base_url = "https://www.flipkart.com"

        # Extract product URLs
        tot_urls = selector.xpath('//div[@class="_1sdMkc LFEi7Z"]/a/@href').getall()

        for url in tot_urls:
            product_url = base_url + url

            # Insert into MongoDB (ignore duplicates)
            collection.update_one(
                {"product_url": product_url},   # filter
                {"$setOnInsert": {"product_url": product_url, "status": "pending"}},  
                upsert=True
            )
            print(f"Watch_url: {product_url} inserted successfully")

    else:
        print("Failed with status:", response.status_code)

except Exception as err:
    print("Error:", err)

finally:
    client.close()
    print("MongoDB connection closed")
