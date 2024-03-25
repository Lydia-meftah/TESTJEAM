import pandas as pd

class ReportGenerator:
    def __init__(self, output_file):
        self.output_file = output_file
        self.df = pd.DataFrame(columns=['File Name', 'Name', 'Surname', 'School', 'Email', 'Phone', 'Score'])

    def add_row(self, file_name, info, score):
        new_row = {
            'File Name': file_name,
            'Name': info.get('name', 'N/A'),
            'Surname': info.get('surname', 'N/A'),
            'School': info.get('school', 'N/A'),
            'Email': info.get('email', 'N/A'),
            'Phone': info.get('phone', 'N/A'),
            'Score': score
        }
        self.df = self.df.append(new_row, ignore_index=True)

    def export(self):
        try:
            self.df.to_csv(self.output_file, index=False)
            print(f"Report generated successfully: {self.output_file}")
        except IOError as e:
            print(f"Failed to write report to {self.output_file}: {e}")
