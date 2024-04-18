<h1 align="center">asolut</h1>

<hr />
  
<p align="center">A solution for the synonym problem in word frequency algorithms </p>

<hr />

<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/asolut?color=dark-green) -->
[![Downloads](https://static.pepy.tech/personalized-badge/asolut?period=total&left_color=grey&right_color=yellow&left_text=Downloads)](https://pepy.tech/project/asolut) ![PyPI - License](https://img.shields.io/pypi/l/asolut?color=red) ![PyPI](https://img.shields.io/pypi/v/asolut?label=version)

This algorithm’s goal is to augment the regular word frequency algorithms by introducing and incorporating the synonyms of the words in the process of counting frequencies. The algorithm consists of three functions that serve to preprocess the text, count the synonym-incorporating frequencies and finally to offer a Graphical User Interface for the users who want to avoid coding.

## The functions
### Function Preprocessing
This ﬁrst function called preprocessing is used to, as the name implies, preprocess the text upon which the word frequencies will be calculated through a sequence of transformations.
#### Input
The function's inputs and their default values are the following:
```python
preprocessing(texts, pos=None, chrsplt="\s|\\\\|/", keepstopwords=False, mode="normal", chng=True)
```
##### ```texts``` parameter:
Type: ```str```

The text that will be preprocessed.
It can be any valid string.

##### ```pos``` parameter:
Type: ```List of str```

The parts of speech that should be included. Any word whose PoS not within this list will be discarded.
Should be a list of valid PoS tags (see [Penn Treebank PoS Tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)).
The true default values of PoS that are assigned later in the function if the default value of ```None``` is chosen are [’JJ’, ’JJR’, ’JJS’, ’NN’, ’NNS’, ’NNP’, ’NNPS’, ’RB’, ’RBR’, ’RBS’, ’VB’, ’VBD’, ’VBG’, ’VBN’, ’VBP’, ’VBZ’] (adjectives, adverbs, verbs and nouns).

##### ```chrsplt``` parameter:
Type: ```str```

Contains a Regular Expression pattern that deﬁnes the character/s where the text should be split at.
Should be a valid Regex (Regular Expression) pattern.

##### ```keepstopwords``` parameter:
Type: ```bool```

Speciﬁes whether stop words should be kept (True) or discarded (False).

##### ```mode``` parameter:
Type: ```str```

Deﬁnes how special characters inside words should be treated.
Should be ”none”, ”normal”, ”extended”, ”full”, or any valid Regex (Regular Expression) pattern preceded by the characters ”custom ” (eg. ”custom a|b”).
The regex patterns of each are as follows and every match they get in each token will result in the removal of the matched part.

mode|RegEx pattern
-------|------------
"none"|no RegEx pattern (keeps words unchanged)
"normal"|^[^\w]+|[^\w]+$
"extended"|^[^\w°؋฿₿¢₡₵$₫֏€ƒ₲₾₴₭₺₼₥₦₱£﷼៛ރ₽₨௹₹৲૱₪₸₮₩¥₳₠₢₯₣₤₶ℳ₧₰₷©™®]+\|[^\w°؋฿₿¢₡₵$₫֏€ƒ₲₾₴₭₺₼₥₦₱£﷼៛ރ₽₨௹₹৲૱₪₸₮₩¥₳₠₢₯₣₤₶ℳ₧₰₷©™®]+$
"full"|\W
"custom x"|x

##### ```chng``` parameter:
Type: ```bool```

Speciﬁes whether words should be lemmatized (True) or not (False).

#### Output
The output of the algorithm is a list that contains the processed tokens. It should be noted that this list is not sorted and also that it may contain several occurrences of the same token.

### Function freqs
#### Input
The function's inputs and their default values are the following:
```python
freqs(textlist, sortedby="sum", returntype="plot", figtitle="plot", numb=None)
```
##### ```textlist``` parameter:
Type: ```List of str```

A list of tokens.
Should be a list of tokens, preferably words

##### ```sortedby``` parameter:
Type: ```str```

In case that the output is a dataset, speciﬁes the variable it should be ordered by.
Must be a string that is either ”frequencies”, ”synonym frequencies” or ”sum”; in case that the string is not one of those, then ”sum” is selected automatically.


##### ```returntype``` parameter:
Type: ```str```

Speciﬁes what will be the output of the function (dataset or graph)
Must be a string with valid values those of ”data”, ”plot” or ”both”.

##### ```ﬁgtitle``` parameter:
Type: ```str```

In case that the output is a graph, speciﬁes its title.
Can be any valid string

##### ```numb``` parameter:
Type: ```int```

In case that the output is a graph, speciﬁes the number n of n most frequent visualised elements
The default value of None was selected in order to make the assigning ﬂexible. Since the number of the visualised elements is related to the total number of unique elements, the numb parameter is made to have a default value of 15 if the count of unique elements are more than or equal to 15, but in the case of less than 15 unique elements the value should become the number of unique elements. In the case that numb is larger than the count of unique elements, then it is made equal to it.
Must be an positive integer. If a non positive value is inputted then it reverts to None like in default.

#### Output
The possible outputs of the freqs function are two, one is a graph while the other is a dataframe. If the graph option is selected, the plotly package is used to create a horizontal stacked bar chart like the one in the ﬁgure below that is immediately displayed in a browser.

<p align="center">
  <img src="https://user-images.githubusercontent.com/46795338/94809872-e8a90e00-03fb-11eb-8756-61a1059009f7.png">
</p>

The option of the dataframe is returned in Python and consists of four columns by the names of ’Words’, ’Counts’, ’Synonym Counts’ and ’List of synonyms’, whose contents are the Numpy arrays words, counts, syncounts and listofsynonyms respectively. The dataframe looks like the table below:

Index|Words|Counts|Synonym Counts|List of synonyms
---|-|------|---------------|-----------------
0|headphone|1|3|[earphone, earpiece]
1|flower|1 |0|[]
2|earphone|2|2|[earpiece, headphone]
3|earpiece|1|3|[earphone, headphone]

### Function gui
The last function offers a Graphical User Interface that is used as a way to make the tool accessible to non developers by adding a menu-like interface that oﬀers ease of use. It outputs a graph upon submission if everything is correctly inputted.


<hr />
For more information on the original versions, visit the paper: DOI: <a href="https://www.researchgate.net/publication/344713286_A_solution_for_the_synonym_problem_in_word_frequency_algorithms">10.13140/RG.2.2.14789.27369</a>
