class KeywordScanner:
    def __init__(self, keywords):
        self.keywords = [keyword.lower() for keyword in keywords]  # Pré-traitez les mots-clés en minuscules pour la comparaison

    def calculate_score(self, text):
        text = text.lower()  # Convertit le texte en minuscules une seule fois
        score = sum(text.count(keyword) for keyword in self.keywords)
        return score
