from io import BytesIO
from pathlib import Path
import re
import textwrap

from pypdf import PdfReader
from docx import Document

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}

SECTION_HEADINGS = {
    "objective",
    "education",
    "technical skills",
    "projects",
    "certifications",
    "languages known",
    "languages",
    "experience",
    "skills",
    "summary",
    "profile",
}

COMPACT_PHRASE_REPAIRS = {
    "toseekchallengingopportunitieswhereicaneffectivelyutilizemyskillsandknowledgeforthegrowthoftheorganizationwhilecontinuouslyimprovingmyprofessionalabilities": "To seek challenging opportunities where I can effectively utilize my skills and knowledge for the growth of the organization while continuously improving my professional abilities.",
}


def _normalize_lines(text):
    lines = []
    for raw_line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        line = " ".join(raw_line.split()).strip()
        if line:
            lines.append(line)
    return lines


def _repair_compact_sentence(line):
    compact = re.sub(r"[^a-z0-9]", "", line.lower())
    for key, value in COMPACT_PHRASE_REPAIRS.items():
        if key in compact:
            return value
    return line


def extract_resume_text(uploaded_file):
    filename = uploaded_file.filename or ""
    suffix = Path(filename).suffix.lower()

    if suffix not in ALLOWED_EXTENSIONS:
        raise ValueError("Please upload a PDF, DOCX, or TXT resume file.")

    raw_data = uploaded_file.read()
    if not raw_data:
        raise ValueError("The uploaded resume file is empty.")

    if suffix == ".pdf":
        reader = PdfReader(BytesIO(raw_data))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
    elif suffix == ".docx":
        document = Document(BytesIO(raw_data))
        text = "\n".join(paragraph.text for paragraph in document.paragraphs)
    else:
        text = raw_data.decode("utf-8", errors="ignore")

    cleaned_text = "\n".join(_normalize_lines(text)).strip()
    if not cleaned_text:
        raise ValueError("No readable text was found in the uploaded resume.")

    return cleaned_text


def format_resume_preview(resume_text):
    normalized_lines = _normalize_lines(resume_text)
    if not normalized_lines:
        return ""

    formatted_lines = []
    current_heading = ""

    for line in normalized_lines:
        cleaned_line = _repair_compact_sentence(line)
        lowered = cleaned_line.lower().rstrip(":")

        if lowered in SECTION_HEADINGS:
            if formatted_lines and formatted_lines[-1] != "":
                formatted_lines.append("")
            formatted_lines.append(cleaned_line)
            formatted_lines.append("")
            current_heading = lowered
            continue

        if current_heading == "objective":
            wrapped = textwrap.wrap(cleaned_line, width=92)
            formatted_lines.extend(wrapped or [line])
            formatted_lines.append("")
            continue

        if current_heading == "education":
            year_match = re.search(r"(20\d{2}\s*[–-]\s*20\d{2}|20\d{2})", cleaned_line)

            if year_match and "cgpa" in cleaned_line.lower():
                before_year = cleaned_line[:year_match.start()].strip().rstrip(",")
                year_text = cleaned_line[year_match.start():].strip()
                cgpa_match = re.search(
                    r"\bCGPA\s*:?\s*([0-9]+(?:\.[0-9]{1,2})?)",
                    before_year,
                    flags=re.IGNORECASE,
                )

                if cgpa_match:
                    if before_year:
                        prefix = before_year[:cgpa_match.start()].strip().rstrip(",")
                        if prefix:
                            formatted_lines.append(prefix)
                    formatted_lines.append(f"CGPA: {cgpa_match.group(1)}")
                    formatted_lines.append(year_text)
                    continue

        if cleaned_line.startswith("•"):
            formatted_lines.append(cleaned_line)
        else:
            if len(cleaned_line) > 95 and not re.search(r"[.:]$", cleaned_line):
                formatted_lines.extend(textwrap.wrap(cleaned_line, width=92))
            else:
                formatted_lines.append(cleaned_line)

    cleaned_lines = []
    for line in formatted_lines:
        if line == "" and cleaned_lines and cleaned_lines[-1] == "":
            continue
        cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()
