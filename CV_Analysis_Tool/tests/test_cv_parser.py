import unittest
from src.cv_parser import CVParser

class TestCVParser(unittest.TestCase):
    def setUp(self):
        # Setup nécessaire pour les tests; par exemple, chemin vers un fichier CV test
        self.parser = CVParser("chemin_vers_les_fichiers_de_test")

    def test_extract_text_pdf(self):
        # Test pour vérifier l'extraction de texte à partir d'un PDF
        # Vous aurez besoin d'un fichier PDF de test dans votre répertoire de test
        test_file_path = "chemin_vers_le_fichier_pdf_de_test.pdf"
        extracted_text = self.parser.extract_text(test_file_path)
        self.assertNotEqual(extracted_text, "", "Le texte extrait ne devrait pas être vide.")

    def test_extract_text_docx(self):
        # Test pour vérifier l'extraction de texte à partir d'un DOCX
        # Vous aurez besoin d'un fichier DOCX de test dans votre répertoire de test
        test_file_path = "chemin_vers_le_fichier_docx_de_test.docx"
        extracted_text = self.parser.extract_text(test_file_path)
        self.assertNotEqual(extracted_text, "", "Le texte extrait ne devrait pas être vide.")

    def test_find_email(self):
        # Test pour vérifier l'extraction d'adresse email
        test_text = "Pour plus d'informations, contactez-moi à exemple@email.com."
        email = self.parser._find_email(test_text)
        self.assertEqual(email, "exemple@email.com", "L'email extrait devrait correspondre à l'email dans le texte de test.")

    # Ajoutez d'autres tests au besoin pour couvrir les fonctionnalités de cv_parser.py

if __name__ == '__main__':
    unittest.main()
