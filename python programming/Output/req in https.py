import requests
r=requests.get("https://site.financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
url="https://www.sometime.com"
data={
    "p1":4,
    "p2":8
}
r2=requests.post(url=url,data=data)