import json

from db import SessionLocal

from models import Source
from models import ExtractedData
from models import Destination

from apify_client_service import scrape_linkedin
from extractor import extract_profile_data


def process_source():

    db = SessionLocal()

    try:

        pending_sources = db.query(
            Source
        ).filter(
            Source.status == "PENDING"
        ).all()

        for source in pending_sources:

            print(
                f"Processing {source.linkedin_url}"
            )

            raw_data = scrape_linkedin(
                source.linkedin_url
            )

            extracted = extract_profile_data(
                raw_data
            )

            extracted_row = ExtractedData(
                source_id=source.id,
                linkedin_id=extracted.get(
                    "linkedin_id"
                ),
                raw_response=raw_data,
                headline=extracted.get(
                    "headline"
                ),
                about=extracted.get(
                    "about"
                ),
                skills=extracted.get(
                    "skills"
                ),
                status="SUCCESS"
            )

            db.add(extracted_row)

            destination_row = Destination(
                linkedin_id=extracted.get(
                    "linkedin_id"
                ),
                headline=extracted.get(
                    "headline"
                ),
                about=extracted.get(
                    "about"
                ),
                skills=",".join(
                    extracted.get(
                        "skills",
                        []
                    )
                )
            )

            db.add(destination_row)

            source.status = "COMPLETED"

            db.commit()

            print(
                "Inserted Successfully"
            )

    except Exception as e:

        db.rollback()

        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    process_source()