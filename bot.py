import requests
import csv

# Your Google Places API Key
GOOGLE_API_KEY = "AIzaSyClkznw890rj_6LfH5ZAGEW0eSWY_mG8xI"
LOCATION = "Texas, USA"
SEARCH_QUERY = "IT services"  # Change this for different business types

# Google Places API URL
places_url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={SEARCH_QUERY}+in+{LOCATION}&key={GOOGLE_API_KEY}"

# Fetch business listings
response = requests.get(places_url)
data = response.json()

business_list = []
for business in data.get("results", []):
    name = business.get("name", "N/A")
    address = business.get("formatted_address", "N/A")
    website = business.get("website", "N/A")  # Only some businesses have websites
    business_list.append([name, address, website])

# Save businesses to CSV
with open("businesses.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Business Name", "Address", "Website"])
    writer.writerows(business_list)

print("✅ Business data saved to businesses.csv")
