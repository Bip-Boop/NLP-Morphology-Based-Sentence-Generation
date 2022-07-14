# NLP-Morphology-Based-Sentence-Generation
Text building from morphological structure and semantic space, defined by input words (optionally)

## Example (Recipe generation)
```from sentence_patterns import TextConstructor, SentenceScheme```

Create schemes:
```
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
```
Template is created by assigning part of speech to each word in the sentence: v for verb, n for noun (for more detail see tools.py)

Abstract scheme is defined by a list:

```["n", "v", "n"]```

You can also provide concrete words in the following array:

```[None, "cook", None]```

Punctuation is optional.

Next, create text constructor, providing more words for context:

```tc = TextConstructor(["apples", "water", "sugar"], schemes)]```

You can use different constructors for different contexts.

Now it is possible to generate text:

```print(tc.generate_text(input_involvement_probability=0.9, length=8).replace("_", " "))```

Input involvement probability describes how often the exact words from context will appear in the result.

Length sets number of sentences in the final text.
