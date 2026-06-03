from apify_client_service import scrape_linkedin

data = scrape_linkedin(
    "https://www.linkedin.com/in/shivangi-shukla2208"
)

print(data)