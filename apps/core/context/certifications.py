from dataclasses import dataclass


@dataclass(frozen=True)
class Certification:
    issuer: str
    title: str
    description: str
    url: str
    action: str


CERTIFICATIONS = [

    Certification(

        issuer="IBM",

        title="9 Verified Badges",

        description=(
            "Data Science, Python, Data Analysis, "
            "Visualization and related technologies."
        ),

        url="https://www.credly.com/users/dimitri-bachkatov",

        action="View Credly Profile",

    ),

    Certification(

        issuer="English",

        title="C1 English Certificate",

        description="Verified English proficiency (C1).",

        url=(
            "https://internationalenglishtest.com/"
            "verify-certificate/"
            "758B8DE2A1-758B8DE304-758B8DBA6C"
        ),

        action="Verify Certificate",

    ),

]