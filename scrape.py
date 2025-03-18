import requests

payload = { 'api_key': '217dcd69b4b0e964916750e6adbfef36', 'url': 'https://www.google.com/maps', 'output_format': 'csv', 'autoparse': 'true', 'follow_redirect': 'false', 'country_code': 'us', 'device_type': 'desktop', 'session_number': '10', 'max_cost': '2000' }
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)
