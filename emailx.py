from bs4 import BeautifulSoup
import re

# Function to extract emails from a website
def extract_email(website):
    try:
        response = requests.get(website, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text))
        return emails if emails else "No email found"
    except:
        return "Failed to fetch"

# Load websites from CSV
with open("businesses.csv", "r", encoding="utf-8") as file:
    next(file)  # Skip header
    business_websites = [line.strip().split(",")[-1] for line in file]

email_data = []
for site in business_websites[:5]:  # Limit for testing
    emails = extract_email(site)
    email_data.append([site, emails])

# Save extracted emails to CSV
with open("business_emails.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Website", "Emails"])
    writer.writerows(email_data)

print("✅ Emails saved to business_emails.csv")
