import numpy as np
import pandas as pd


df = pd.read_csv("../lexical_simplification/word_complexity_lexicon/lexicon.tsv", sep='\t', names=["word", "complexity"])

df['word_lower'] = df["word"].str.lower()

print(df.sample(3))


def score_sentence(sentence):
    print("Splitting the sentence: " + sentence)
    print("Split form:")
    print(sentence.split())

    word_complexity_scores = [df[df['word_lower'] == word.lower()]["complexity"].iloc[0] if any(word.lower() == df["word_lower"]) else np.nan for word in sentence.split()]
    print(word_complexity_scores)
    return word_complexity_scores

print(score_sentence("I am a hungry caterpillar"))
