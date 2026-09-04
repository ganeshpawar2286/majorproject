import os
import requests
import json
import base64

class ExternalParsers:
    def __init__(self):
        # Default API keys loaded from environment if configured
        self.affinda_api_key = os.environ.get("AFFINDA_API_KEY", "")
        self.rchilli_user_key = os.environ.get("RCHILLI_USER_KEY", "")
        self.textkernel_account_id = os.environ.get("TEXTKERNEL_ACCOUNT_ID", "")
        self.textkernel_service_key = os.environ.get("TEXTKERNEL_SERVICE_KEY", "")

    # 1. AFFINDA RESUME PARSER API
    def parse_with_affinda(self, file_bytes, filename, api_key=None):
        key = api_key or self.affinda_api_key
        if not key:
            raise ValueError("Affinda API Key is missing. Please provide your AFFINDA_API_KEY.")

        url = "https://api.affinda.com/v3/documents"
        headers = {"Authorization": f"Bearer {key}"}
        files = {"file": (filename, file_bytes)}

        response = requests.post(url, headers=headers, files=files, timeout=15)
        if response.status_code not in [200, 201]:
            raise RuntimeError(f"Affinda API Error ({response.status_code}): {response.text}")

        res_json = response.json()
        data = res_json.get("data", {})

        # Extract structured fields
        name_raw = data.get("name", {})
        candidate_name = name_raw.get("raw", "Candidate") if isinstance(name_raw, dict) else "Candidate"
        
        emails = [e.get("raw") for e in data.get("emails", []) if e.get("raw")]
        phones = [p.get("raw") for p in data.get("phoneNumbers", []) if p.get("raw")]
        skills = [s.get("name", "").title() for s in data.get("skills", []) if s.get("name")]
        
        education_items = []
        for edu in data.get("education", []):
            deg = edu.get("accreditation", {}).get("education", "") or "Degree"
            education_items.append(deg.upper())

        return {
            "engine": "Affinda API",
            "candidate_name": candidate_name,
            "email": emails[0] if emails else None,
            "phone": phones[0] if phones else None,
            "skills": sorted(list(set(skills))),
            "education": education_items if education_items else ["Higher Education"],
            "raw_text_snippet": data.get("rawText", "")[:500]
        }

    # 2. RCHILLI RESUME PARSER API
    def parse_with_rchilli(self, file_bytes, filename, user_key=None):
        key = user_key or self.rchilli_user_key
        if not key:
            raise ValueError("RChilli User Key is missing. Please provide your RCHILLI_USER_KEY.")

        url = "https://api.rchilli.com/rchilli/v8/parseResumeJson"
        b64_content = base64.b64encode(file_bytes).decode("utf-8")
        
        payload = {
            "filedata": b64_content,
            "filename": filename,
            "userkey": key,
            "version": "8.0.0",
            "subuserkey": ""
        }

        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=15)
        if response.status_code != 200:
            raise RuntimeError(f"RChilli API Error ({response.status_code}): {response.text}")

        res_json = response.json()
        parser_data = res_json.get("ResumeParserData", {})

        name_data = parser_data.get("Name", {})
        candidate_name = name_data.get("FullName", "Candidate") if isinstance(name_data, dict) else "Candidate"
        
        email = parser_data.get("Email", [{}])[0].get("EmailAddress") if parser_data.get("Email") else None
        phone = parser_data.get("PhoneNumber", [{}])[0].get("Number") if parser_data.get("PhoneNumber") else None
        
        skills_raw = parser_data.get("SkillKeywords", "").split(",")
        skills = [s.strip().title() for s in skills_raw if s.strip()]

        return {
            "engine": "RChilli API",
            "candidate_name": candidate_name,
            "email": email,
            "phone": phone,
            "skills": sorted(list(set(skills))),
            "education": ["Graduate / Professional Credential"],
            "raw_text_snippet": parser_data.get("ResumeData", "")[:500]
        }

    # 3. TEXTKERNEL TX PLATFORM API
    def parse_with_textkernel(self, file_bytes, filename, account_id=None, service_key=None):
        acc_id = account_id or self.textkernel_account_id
        svc_key = service_key or self.textkernel_service_key
        
        if not acc_id or not svc_key:
            raise ValueError("Textkernel Account ID or Service Key is missing. Please configure TEXTKERNEL_SERVICE_KEY.")

        url = "https://api.textkernel.com/tx/v10/parser/resume"
        b64_content = base64.b64encode(file_bytes).decode("utf-8")
        
        headers = {
            "Tx-AccountId": acc_id,
            "Tx-ServiceKey": svc_key,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        payload = {
            "DocumentBytes": b64_content,
            "DocumentLastModified": "2026-08-18"
        }

        response = requests.post(url, json=payload, headers=headers, timeout=15)
        if response.status_code != 200:
            raise RuntimeError(f"Textkernel API Error ({response.status_code}): {response.text}")

        res_json = response.json()
        val = res_json.get("Value", {}).get("ResumeData", {})

        contact = val.get("ContactInformation", {})
        candidate_name = contact.get("CandidateName", {}).get("FormattedName", "Candidate")
        
        emails = contact.get("EmailAddresses", [])
        phones = contact.get("Telephones", [])
        
        skills_tax = val.get("SkillsData", [])
        skills = []
        for s_group in skills_tax:
            for s in s_group.get("TaxonomyRoot", []):
                skills.append(s.get("Name", "").title())

        return {
            "engine": "Textkernel Tx API",
            "candidate_name": candidate_name,
            "email": emails[0] if emails else None,
            "phone": phones[0] if phones else None,
            "skills": sorted(list(set(skills))),
            "education": ["University Degree / Credentials"],
            "raw_text_snippet": val.get("ResumeSummary", "")[:500]
        }

external_parsers = ExternalParsers()
