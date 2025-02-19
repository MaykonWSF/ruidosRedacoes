import stanza

# Download the Portuguese model
# stanza.download('pt')

class Grammaticality:
    def __init__(self):
        self.nlp = stanza.Pipeline('pt', download_method=None)

    def analysis(self, essay):
        doc = self.nlp(essay)
        return doc


if __name__ == "__main__":
    gramatica = Grammaticality()
    texto = "O rato roeu a roupa do rei de Roma."
    doc = gramatica.analysis(texto)
    for sent in doc.sentences:
        for word in sent.words:
            print(f"word: {word.text}\tpos: {word.pos}\tfeats: {word.feats}")
    print("Fim da análise.")