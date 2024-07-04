import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.environ.get('STOCK_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}'
r = requests.get(url)
data = r.json()

date_yest = list(data['Time Series (Daily)'].keys())[0]
date_bf_yest = list(data['Time Series (Daily)'].keys())[1]

yesterday = data['Time Series (Daily)'][date_yest]
bf_yesterday = data['Time Series (Daily)'][date_bf_yest]

yesterday_closing = float(yesterday['4. close'])
bf_yesterday_closing = float(bf_yesterday['4. close'])

percent_diff = round(((yesterday_closing - bf_yesterday_closing) / yesterday_closing), 2)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
recent_articles = []
if abs(percent_diff) >= 0.05:
    news_url = f'https://newsapi.org/v2/everything?q={STOCK}&from=2024-06-04&sortBy=publishedAt&apiKey={NEWS_API_KEY}'
    news_r = requests.get(news_url)
    news_data = news_r.json()
    recent_articles = news_data['articles'][:3]


## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

def format_msg(company_name, perc_diff, _article):
    stock_report = f'{company_name}: {"🔺" if perc_diff > 0 else "🔻"} {abs(perc_diff) * 100}%'

    return f"""
    {stock_report}
    Headline: {_article['title']}
    Brief: {_article['description']}
    """


def send_text(body):
    """
    NOTE: Must have an ACCT_SID and AUTH_TOKEN from Twilio, which must be saved as ENV variables;
    also, your personal mobile number must be saved
    """

    twilio_account_sid = os.environ.get('TWILIO_ACCT_SID')
    twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_client = Client(twilio_account_sid, twilio_auth_token)

    your_mobile_number = os.environ.get('PHONE_NUM')

    twilio_client.messages.create(
        from_='+16508259151',
        to=your_mobile_number,
        body=body
    )


if recent_articles:
    for article in recent_articles:
        message = format_msg(COMPANY_NAME, percent_diff, article)
        send_text(message)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
