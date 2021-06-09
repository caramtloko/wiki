import wikipedia
import yake

def ExtractKeysFromWiki(subject):
    wikipedia.set.lang("pt")
    sumario = wikipedia.summary(subject)

    kws = yake.KeywordExtractor(lan="pt")
    keywords = kws.extract_keywords(sumario)

    return keywords