def extract_profile_data(raw_json):

    if not raw_json:
        return {}

    profile = raw_json[0]

    first_name = (
        profile.get("firstName")
        or profile.get("first_name")
    )

    last_name = (
        profile.get("lastName")
        or profile.get("last_name")
    )

    headline = profile.get("headline")

    about = (
        profile.get("about")
        or profile.get("summary")
        or profile.get("bio")
        or profile.get("description")
    )

    skills = []

    for skill in profile.get("skills", []):

        if isinstance(skill, dict):
            skills.append(
                skill.get("name")
            )
        else:
            skills.append(skill)

    certifications = []

    for cert in profile.get(
        "certifications",
        []
    ):

        if isinstance(cert, dict):

            certifications.append(
                cert.get("name")
            )

        else:
            certifications.append(cert)

    linkedin_id = (
        profile.get("publicIdentifier")
        or profile.get("linkedinId")
    )

    return {
        "linkedin_id": linkedin_id,
        "first_name": first_name,
        "last_name": last_name,
        "headline": headline,
        "about": about,
        "skills": skills,
        "certifications": certifications
    }