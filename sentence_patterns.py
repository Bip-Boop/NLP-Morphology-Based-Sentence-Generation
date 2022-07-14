from copy import deepcopy

import tools
from random import choice, randint, uniform

from nltk.corpus import wordnet as wn


# (Охапка дров и плов готов)
class TextConstructor:

    def __init__(self, available_words, abstract_sentences):
        self.available_words = available_words

        self.abstract_sentences = list(abstract_sentences)

        self.mt = tools.MorphologicalTools()
        self.sct = tools.StaticContextTools()
        #self.dct = tools.DynamicContextTools()

        self.available_words_POSes = list()
        for aw in self.available_words:
            self.available_words_POSes.append(wn.synsets(aw)[0].pos())

        self.connected_words = set()
        for w in available_words:
            for sim in self.sct.get_similar(w):
                self.connected_words.add(sim)
        self.connected_words = list(self.connected_words)

        self.senteces = list()
        self.lenght = None

    def generate_text(self, lenght=None, input_involvement_probability = 0.5):
        text = ""
        self.lenght = lenght
        if self.lenght is None:
            self.lenght = randint(2, len(self.available_words))

        for i in range(self.lenght):
            self.senteces.append(deepcopy(choice(self.abstract_sentences)))

        for s in self.senteces:
            s.text_constructor = self

            for i in range(len(s.POSes)):
                if s.POSes[i] == "n" and s.specific_words[i] is None and uniform(0.0, 1.0) < input_involvement_probability:
                    s.specific_words[i] = choice(self.available_words)

            s.complete()
            text += s.get_sentence() + " "

        return text[:-1]


class SentenceScheme:

    def __init__(self, POSes, specific_words, text_constructor: TextConstructor, punctuation="."):
        assert (len(POSes) == len(specific_words))

        self.POSes = POSes
        self.specific_words = specific_words
        self.text_constructor = text_constructor
        self.punctuation = punctuation

        if self.specific_words is None:
            self.specific_words = [None] * len(POSes)


    def complete(self):

        for i in range(len(self.POSes)):
            variants = list()
            if self.specific_words[i] is None:
                j = 0
                while not variants and j < 256:
                    variants = self.text_constructor.mt.find_all_variants_of_pos(choice(
                        self.text_constructor.connected_words), self.POSes[i])
                    j += 1

                self.specific_words[i] = variants[0]





    def get_unprepared_sentence_tokens(self):
        sentence = ""
        for w in self.specific_words:
            wf = w
            if wf is None:
                wf = "a"  # неопределенный артикуль наименьшим образом скажется на контексте
            sentence += wf + " "
        return sentence[:-1]


    def get_sentence(self):
        sentence = ""
        for w in self.specific_words:
            if w is None:
                raise RuntimeError("Sentence is not constructed yet")
            sentence += w + " "
        return sentence[0].upper() + sentence[1:-1] + self.punctuation


#sc = SentenceScheme(["a", "n", "p", "a", "n"], ["a", None, "in", "the", "box"], TextConstructor(["box"], ("f")) )
#sc.complete()
#print(sc.get_sentence())


