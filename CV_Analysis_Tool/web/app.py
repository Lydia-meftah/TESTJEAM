from flask import Flask, request, send_file
from src.cv_parser import CVParser
from src.keyword_scanner import KeywordScanner
from src.report_generator import ReportGenerator
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def upload_form():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload CV for Analysis</title>
</head>
<body>
    <h1>CV Analysis Tool</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <label for="cvUpload">Upload your CV:</label>
        <input type="file" id="cvUpload" name="cvUpload" accept=".pdf, .docx">
        <button type="submit">Analyze CV</button>
    </form>
</body>
</html>
'''
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'cvUpload' not in request.files:
        return 'No file part'
    file = request.files['cvUpload']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        # Vous pouvez adapter le chemin selon votre configuration
        temp_path = tempfile.mkdtemp()
        file_path = os.path.join(temp_path, file.filename)
        file.save(file_path)
        
        # Initialisation des modules avec les chemins appropriés
        parser = CVParser(temp_path)
        keywords = ['Natixis', 'Emlyon', 'investissements', 'Equipe', 'M&A', 'Crédit Agricole', 'BNP', 'DCF', 'Multiples', 'statistics', 'Grande Ecole', 'Neoma', 'Capital', 'KPMG']
        scanner = KeywordScanner(keywords)
        report_file = tempfile.NamedTemporaryFile(delete=False)
        generator = ReportGenerator(report_file.name)
        
        # Processus d'analyse
        text = parser.extract_text(file_path)
        info = parser.extract_info(text)
        score = scanner.calculate_score(text)
        generator.add_row(file.filename, info, score)
        generator.export()

        return send_file(report_file.name, as_attachment=True, download_name='report.csv')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'docx'}

if __name__ == '__main__':
    app.run(debug=True)
