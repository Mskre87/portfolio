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

        issuer="IBM SkillsBuild",

        title="9 Verified Professional Credentials",

        description=(
            "Professional certifications covering Python, Data Science, "
            "Data Analysis, Data Visualization, Data Science Foundations "
            "and related technologies."
        ),

        url="https://www.credly.com/users/dimitri-bachkatov",

        action="View Credly Profile",

    ),

    Certification(

        issuer="International English Test",

        title="English Proficiency (C1)",

        description=(
            "Verified C1 English proficiency for professional and "
            "technical communication."
        ),

        url=(
            "https://internationalenglishtest.com/"
            "verify-certificate/"
            "758B8DE2A1-758B8DE304-758B8DBA6C"
        ),

        action="View Certificate",

    ),

]