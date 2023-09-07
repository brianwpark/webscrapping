import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

for i in range(1, 6):
    print("page:", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=9&backgroundColor=".format(i)
    
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        # remove all AD
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("  <AD is removed>")
            continue


        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명

        # remove apple products
        if "Apple" in name:
            # print("  <Apple product is removed>")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
        
        # Item with more than 100 review & rating with more than 4.5 will be listed
        rate = item.find("em", attrs={"class":"rating"}) # rating
        if rate:
            rate = rate.get_text()
        else:
            # print("  <Item without rating is removed>")
            continue
        
        rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수

        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            # print("  <Item without rating is removed>")
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            # print(name, price, rate, rate_cnt)
            print(f"Product : {name}")
            print(f"Price : {price}")
            print(f"Rating : {rate} ({rate_cnt} Ratings)")
            print("Link for Product : {}".format("https://www.coupang.com" + link))
            print("-"*100) # line for devision