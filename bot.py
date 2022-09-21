import spacy
import textblob
from spacytextblob.spacytextblob import SpacyTextBlob


def print_sentiment(doc):
        sentiment = doc._.polarity

        if sentiment > 0.7:
            print("[BOT] I'm happy to hear that")
        elif sentiment < 0.3:
            print("[BOT] I'm sorry to hear that")
        else:
            print("[BOT] I'm neutral about that")



if __name__ == "__main__":

    # if en core web sm doesn't exit
    # download it
    try:
        nlp = spacy.load("en_core_web_sm")
    except:
        from spacy.cli import download
        download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")

    nlp.add_pipe('spacytextblob')


    print("ctrl-c to exit")

    print("[BOT] Hi nice to meet you, what would you like to talk about?")
    sentence: str = input()
    while True:

        if sentence.lower() in ["exit", "quit", "q", "bye", "goodbye"]:
            print("[BOT] Bye!")
            break

        if not sentence:
            print("[BOT] What would you like to talk about?")
            sentence = input()
            continue

        doc = nlp(sentence)

        noun_phrases = [chunk.text for chunk in doc.noun_chunks]
        print(noun_phrases)
        if not noun_phrases:
            print_sentiment(doc)
            sentence = input()
            continue

        for noun_phrase in noun_phrases:

            if noun_phrase in ["i", "you", "we", "they", "he", "she", "it"]:
                continue

            print(f"[BOT] What do you think about {noun_phrase}?")
            sentence = input()
            doc = nlp(sentence)
            break

        print_sentiment(doc)
        sentence = input()



