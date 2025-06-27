import os
import pdfplumber
from chain import chain
from utils import clean_spoken_languages, normalize_duration

from typing import Union

def resume_to_text(resume_input: Union[str, bytes]) -> str:
    if os.path.isfile(resume_input) and resume_input.lower().endswith(".pdf"):
        with pdfplumber.open(resume_input) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    return resume_input  # Assume plain text

def parse_resume(resume_input: str) -> dict:
    resume_text = resume_to_text(resume_input)
    parsed = chain.run({"resume_text": resume_text})
    result = parsed.dict()

    result["languages"] = clean_spoken_languages(result.get("languages", []))

    for job in result.get("work_history", []):
        job["duration_years"] = normalize_duration(job.get("duration_years"))

    return result
