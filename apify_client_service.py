from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)


def scrape_linkedin(linkedin_url):
    try:
        run_input = {
            "profileScraperMode": "Profile details no email ($4 per 1k)",
            "queries": [linkedin_url]
        }

        print(f"Scraping: {linkedin_url}")

        run = client.actor(
            "harvestapi/linkedin-profile-scraper"
        ).call(
            run_input=run_input
        )

        print("Actor Run Completed")

        dataset_id = run.default_dataset_id

        print(f"Dataset ID: {dataset_id}")

        items = list(
            client.dataset(
                dataset_id
            ).iterate_items()
        )

        print(f"Records Found: {len(items)}")

        return items

    except Exception as e:
        print(f"Apify Error: {e}")
        raise