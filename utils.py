from typing import List

KNOWN_PROGRAMMING_LANGUAGES = {
    "python", "java", "c++", "c", "c#", "go", "golang", "typescript", "javascript",
    "kotlin", "ruby", "php", "r", "swift", "rust", "scala", "perl", "sql", "bash"
}

def clean_spoken_languages(langs: List[str]) -> List[str]:
    return [lang for lang in langs if lang.lower() not in KNOWN_PROGRAMMING_LANGUAGES]

def normalize_duration(duration):
    if duration is None:
        return None
    try:
        years = float(duration)
        return int(years) if years.is_integer() else round(years, 1)
    except:
        return None

def extract_specific_socials(links: List[str]) -> dict:
    socials = {
        "linkedin": None,
        "github": None,
        "others": []
    }
    for link in links:
        link = link.lower()
        if "linkedin.com" in link:
            socials["linkedin"] = link
        elif "github.com" in link:
            socials["github"] = link
        else:
            socials["others"].append(link)
    return socials
