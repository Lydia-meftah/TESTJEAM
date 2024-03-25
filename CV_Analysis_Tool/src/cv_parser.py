import os
import re
from pdfminer.high_level import extract_text as extract_text_pdf
from docx import Document

class CVParser:
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phone_regex = re.compile(r'\b\d{10}\b')

    def __init__(self, cv_folder):
        self.cv_folder = cv_folder

    def get_cv_files(self):
        for root, _, files in os.walk(self.cv_folder):
            for file in files:
                yield os.path.join(root, file)

    def extract_text(self, file_path):
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == '.pdf':
            return self._extract_text_from_pdf(file_path)
        elif file_extension == '.docx':
            return self._extract_text_from_docx(file_path)
        else:
            print(f"Unsupported file format: {file_extension}")
            return ""

    def _extract_text_from_pdf(self, file_path):
        return extract_text_pdf(file_path)

    def _extract_text_from_docx(self, file_path):
        doc = Document(file_path)
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)

    def extract_info(self, text):
        email = self.email_regex.search(text)
        phone = self.phone_regex.search(text)
        return {
            'email': email.group(0) if email else None,
            'phone': phone.group(0) if phone else None,
        }

    def _find_email(self, text):
        """Trouve l'adresse email dans le texte."""
        match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        return match.group(0) if match else None

    def _find_phone(self, text):
        """Trouve le numéro de téléphone dans le texte."""
        # Ce regex est un exemple simple et peut nécessiter des ajustements
        match = re.search(r'\b\d{10}\b', text)
        return match.group(0) if match else None
