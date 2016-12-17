# cfg-generator
A tool to generate all words in the language denoted by a given context-free grammar.


## Use
`python3 context_free_grammar.py /path/to/grammarfile length`

Length: the number of rule subsitutions, defult = 2

## Grammar File Format

The character on the lefthand side of the first rule denotes the intial non-terminal. All other rules appear on their own line, where the lefthand side denotes the non-terminal and the righthand side denotes the result of the rule application.

Example Grammarfile:
```
S = A S B
S = |
```
