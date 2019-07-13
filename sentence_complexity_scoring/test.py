import numpy as np
import pandas as pd


df = pd.read_csv("../lexical_simplification/word_complexity_lexicon/lexicon.tsv", sep='\t', names=["word", "complexity"])

df['word_lower'] = df["word"].str.lower()

def score_sentence(sentence):
    print("Splitting the sentence: " + sentence)
    print("Split form:")
    print(sentence.split())

#    word_complexity_scores = [df[df['word_lower'] == word.lower()]["complexity"].iloc[0] if any(word.lower() == df["word_lower"]) else np.nan for word in sentence.split()]
    word_complexity_scores = [df[df['word_lower'] == word.lower()]["complexity"].iloc[0] if any(word.lower() == df["word_lower"]) else 5.0 for word in sentence.split()]
    return word_complexity_scores

print(score_sentence("I am a hungry caterpillar. Are you?"))


sentence = "I am a hungry caterpillar"
sentence_score = score_sentence(sentence)
print(sentence_score)
print(np.nansum(sentence_score) / len(sentence_score))

sentence = "Beyond my might for tonight I shall dine on turtle soup"
sentence_score = score_sentence(sentence)
print(sentence_score)
print(np.nansum(sentence_score) / len(sentence_score))

sentence = "Tonight I will eat soup"
sentence_score = score_sentence(sentence)
print(sentence_score)
print(np.nansum(sentence_score) / len(sentence_score))

sentence = "I eat soup"
sentence_score = score_sentence(sentence)
print(sentence_score)
print(np.nansum(sentence_score) / len(sentence_score))
