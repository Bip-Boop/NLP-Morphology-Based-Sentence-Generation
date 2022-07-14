
from sentence_patterns import TextConstructor, SentenceScheme

schemes = (SentenceScheme(["n", "v", "n"], [None, None, None], None),
           SentenceScheme(["n", "v", "n"], [None, "cook", None], None),
           SentenceScheme(["n", "v", "n"], [None, "fry", None], None),
           SentenceScheme(["v", "_a_", "n"], [None, "a", None], None),
           SentenceScheme(["v", "the", "n"], [None, "the", None], None),
           SentenceScheme(["v", "to", "v", "n"], [None, "to", None, None], None),
           SentenceScheme(["v", "n", "on", "the", "n"], [None, None, "on", "the", None], None),
           SentenceScheme(["v", "n", "on", "the", "n"], [None, None, "on", "the", "stove"], None),
           SentenceScheme(["v", "n", "on", "the", "n"], [None, None, "on", "the", "table"], None),
           SentenceScheme(["v", "n"], [None, None],  None),
           SentenceScheme(["v", "n"], ["roast", None], None),
           SentenceScheme(["v", "n"], ["boil", None], None),
           SentenceScheme(["v", "n"], ["bake", None], None),
           SentenceScheme(["v", "a", "n"], [None, None, None], None),
           SentenceScheme(["v", "a", "n"], [None, None, None], None),
           SentenceScheme(["v", "a", "n"], [None, None, None], None),
           SentenceScheme(["v", "a", "n"], [None, None, None], None),
           SentenceScheme(["v", "a", "n"], [None, None, None], None, punctuation="!"),
           SentenceScheme(["v", "n", "and", "v", "a", "n"], [None, None, "and", None, None, None], None),
           SentenceScheme(["v", "n", "a"], [None, None, None], None),
           SentenceScheme(["v", "a", "n", "on", "the", "n"], [None, None, None, "on", "the", None], None),
           )

tc = TextConstructor(["apples", "water", "sugar"], schemes)
tc = TextConstructor(["apples", "water", "sugar", "orange", "vodka", "syrup"], schemes)
tc = TextConstructor(["cucumber", "dill", "octopus", "herring", "flour", "water"], schemes)
tc = TextConstructor(["cheese", "dill", "toadstools", "cream", "flour", "water", "basil"], schemes)

print(tc.generate_text(input_involvement_probability=0.9, lenght=8).replace("_", " "))
