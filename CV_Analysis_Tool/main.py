from src.cv_parser import CVParser
from src.keyword_scanner import KeywordScanner
from src.report_generator import ReportGenerator

def main():
    cv_folder = "path/to/cvs"  # Chemin du dossier contenant les CV
    keywords = ['Natixis', 'Emlyon', 'investissements', 'Equipe', 'M&A', 'Crédit Agricole', 'BNP', 'DCF', 'Multiples', 'statistics', 'Grande Ecole', 'Neoma', 'Capital', 'KPMG']
    output_file = "path/to/output/report.csv"

    parser = CVParser(cv_folder)
    scanner = KeywordScanner(keywords)
    generator = ReportGenerator(output_file)

    for cv_file in parser.get_cv_files():
        text = parser.extract_text(cv_file)
        info = parser.extract_info(text)
        score = scanner.calculate_score(text)
        generator.add_row(cv_file, info, score)

    generator.export()

if __name__ == "__main__":
    main()
