import requests
import csv

# ScraperAPI Key
SCRAPERAPI_KEY = "217dcd69b4b0e964916750e6adbfef36"

# Google Search Query
QUERY = "IT services in Texas contact email"
GOOGLE_SEARCH_URL = f"https://www.google.com/search?q={QUERY.replace(' ', '+')}"

# ScraperAPI Request
SCRAPERAPI_URL = f"http://api.scraperapi.com/?api_key={SCRAPERAPI_KEY}&url={GOOGLE_SEARCH_URL}"

# Make the request
response = requests.get(SCRAPERAPI_URL)

# Debugging Response
print("Response Status Code:", response.status_code)
print("Response Text:", response.text[:500])  # Print first 500 characters

# Save raw HTML to a file for manual inspection
with open("google_results.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("✅ Google search results saved as google_results.html. Open it to check the content.")
