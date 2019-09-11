import spacy
from spacy.lang.fr.examples import sentences






def trouver_anciennete(path):
    nlp = spacy.load('fr_core_news_md')
    with open(path, 'r+', encoding="utf-8",errors='ignore') as f:
        data = f.read().replace('\n', '')
    doc = nlp(data)
    #print(doc.text)
    for ix, token in enumerate(doc):
        if token.text == "anciennet":
            for child in token.children:
                if child.text == "ans" or child.text == "annes" :
                    print('Ancienneté en années :  %s ' % doc[ix + 1:][1])
                if child.text == "mois" :
                    print('Ancienneté en mois :  %s ' % doc[ix + 1:][1])



def trouver_salaire(path):
    nlp = spacy.load('fr_core_news_md')
    with open(path, 'r+', encoding="utf-8",errors='ignore') as f:
        data = f.read().replace('\n', '')
    doc = nlp(data)
    #print(doc.text)
    for ix, token in enumerate(doc):
        if token.text == "salaire":
            for child in token.children:
                if child.text == "euros":
                    print("Le salaire est de : %s euros" % [token.text for token in child.lefts][1])


trouver_anciennete('arret4.txt')

trouver_salaire('arret4.txt')