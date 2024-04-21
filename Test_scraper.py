import requests

url = "https://api.afl.com.au/statspro/playersStats/seasons/CD_S2024014?includeBenchmarks=false"

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
  'Accept': '*/*',
  'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://www.afl.com.au/',
  'x-media-mis-token': 'e6da82c16bf7dd55943d27263fd7db57',
  'Origin': 'https://www.afl.com.au',
  'Connection': 'keep-alive',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'If-None-Match': 'W/69301c9088c80c05b5d0a60773233f09',
  'TE': 'trailers',
  'Cookie': 'ak_bmsc=77B3597F16CCA474AF5CBCEFB5BC6BB1~000000000000000000000000000000~YAAQBRb0GPerbdSOAQAALdxa/heVPsBDhcPqdQBFFHPdzj0im4gGgrgwN4ZCPo+AP5syZEzErU1oORQyW9couu6F7ccHZLnkgYavJZP6UkxXGK8xI3U0d05bS4YJkv+0rt3bL06SsJ6POL1cIcrw2tvuMyK3da+yoC3a87sH73hZ+boWVDwfvuQ2F13qbZ/fplgZWXPp4CKAClJW7a7efRIYY2dLmDnXhLSmoyR9ZmlkYc5PFO9XtNtFcOwKVqWR03X4gSWaXFCGcdGfqVubbzW3+mmmzEgZ9XE+MQmSuHkvdiNv9jy3ZjZl00fRmgtU3ltUI7IUwYQnyoJDPGUGc45BkOQN8zSM4U9EW42gtBN+SjV//tIDjzqivA=='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
