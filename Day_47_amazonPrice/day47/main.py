import smtplib
from bs4 import BeautifulSoup
import requests
import os


def get_price_alert(product_url, headers={}):
    response = requests.get(product_url, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    price_whole = soup.find(class_='a-price-whole').get_text()
    price_fraction = soup.find(class_='a-price-fraction').get_text()
    current_price = float(f"{price_whole}{price_fraction}")
    product_title = soup.find(class_='a-size-large a-spacing-none', id='title').get_text()

    return (product_title, current_price)


def send_mail(sender_addr, sender_pwd, recip_addr, subject, message):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=sender_addr, password=sender_pwd)
    connection.sendmail(
        from_addr=sender_addr, to_addrs=recip_addr, msg=f"Subject:{subject}\n\n{message}")
    connection.close()


gmail_email = os.environ['GMAIL_EMAIL']
gmail_app_pwd = os.environ['GMAIL_APP_PWD']

product_url = ("https://www.amazon.ca/Struct-Molding-Creme-5-3-Ounce/dp/B00E5JXYLO?pd_rd_w=NnfAi&content-id=amzn1.sym"
               ".d66add78-05b0-4a3d-9404-5c9bc639cee0&pf_rd_p=d66add78-05b0-4a3d-9404-5c9bc639cee0&pf_rd_r"
               "=77CMKJK383JQ4Y52XQHN&pd_rd_wg=1bOYg&pd_rd_r=5fccc1bd-c6b7-4312-8449-40c3b955da0b&pd_rd_i=B00E5JXYLO"
               "&psc=1&ref_=pd_bap_d_grid_rp_0_1_ec_pd_hp_d_atf_rp_1_t")

headers = {
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    #     "Accept-Encoding": "gzip, deflate, br, zstd",
    #     "Accept-Language": "en-US,en;q=0.9",
    #     "Priority": "u=0, i",
    #     "Sec-Fetch-Dest": "document",
    #     "Sec-Fetch-Mode": "navigate",
    #     "Sec-Fetch-Site": "cross-site",
    #     "Sec-Fetch-User": "?1",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

prod_name, prod_price = get_price_alert(product_url, headers=headers)

BUY_PRICE = 30
try:
    if prod_price < BUY_PRICE:
        send_mail(sender_addr=gmail_email,
                  sender_pwd=gmail_app_pwd,
                  recip_addr=gmail_email,
                  subject='Amazon Price Alert!',
                  message=f'{prod_name} is now ${prod_price}\n{product_url}')
except Exception:
    print("something wrong happened...")
