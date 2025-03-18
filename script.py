import requests
from bs4 import BeautifulSoup
import re

# Your ScraperAPI Key (Replace with new key if necessary)
SCRAPERAPI_KEY = "AIzaSyClkznw890rj_6LfH5ZAGEW0eSWY_mG8xI"

# Google Search Query
QUERY = "IT services in Texas contact email"
GOOGLE_SEARCH_URL = f"https://www.google.com/search?q={QUERY.replace(' ', '+')}"

# Use ScraperAPI to bypass Google bot detection
SCRAPERAPI_URL = f"http://api.scraperapi.com/?api_key={SCRAPERAPI_KEY}&url={GOOGLE_SEARCH_URL}"

def scrape_google():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    response = requests.get(SCRAPERAPI_URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract business websites from Google search results
    business_links = []
    for link in soup.find_all("a", href=True):
        url = link["href"]
        if "http" in url and "google" not in url:
            business_links.append(url.split("&")[0])  # Remove Google tracking params

    return business_links

def extract_emails_from_website(url):
    """Scrapes emails from a business website"""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text))
        return emails if emails else "No email found"
    except:
        return "Failed to fetch"

# Scrape Google for business websites
business_websites = scrape_google()
print("Found Websites:", business_websites)

# Extract emails from each business website
for site in business_websites[:5]:  # Limit to 5 websites to avoid rate limits
    print(f"\nScraping emails from: {site}")
    emails = extract_emails_from_website(site)
    print("Emails found:", emails)
