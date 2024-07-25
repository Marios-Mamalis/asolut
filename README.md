<h1 align="center">asolut</h1>

<hr />
<p align="center">A solution for the synonym problem in word frequency algorithms </p>
<hr />

![Downloads](https://img.shields.io/pepy/dt/asolut?label=Downloads) ![PyPI - License](https://img.shields.io/pypi/l/asolut?color=red) ![PyPI](https://img.shields.io/pypi/v/asolut?label=version)

This library contains the official implementation of the synonym-augmented frequency algorithm presented
in "[A solution for the synonym problem in word frequency algorithms](https://doi.org/10.13140/RG.2.2.14789.27369)",
along with a GUI wrapper and text preprocessing utilities.

## Installation
The package requires Python 3.7.3 and can be installed through PyPi with the following command:
```commandline
pip install asolut
```
Additionaly, the NLTK `stopwords`, `averaged_perceptron_tagger` and `wordnet` resources are needed.

## Reference
### asolut.preprocessing
```python
asolut.preprocessing(texts, pos=None, chrsplt="\s|\\\\|/",
                     keepstopwords=False, mode="normal", chng=True)
```
Performs basic text preprocessing on a given string. Preprocessing includes tokenization, Part of Speech filtering,
stopword removal, special character handling and lemmatization.

#### Parameters:
- `texts: str`  
The text to be preprocessed. Can be any valid string.
- `pos: [str, ...]`, default=`None`  
The parts of speech that should be included in the output. Any word corresponding to a PoS not contained in the list will be 
discarded. List items must be valid [Penn Treebank PoS tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).
The actual default value of the parameter, assigned later in the function, is the following list:
`["JJ", "JJR", "JJS", "NN", "NNS", "NNP", "NNPS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]`
(adjectives, adverbs, verbs and nouns).
- `chrsplt: str`, default=`"\s|\\\\|/"`  
Regular Expression pattern that defines the character/s on which the text should be split at. 
Must be a valid RegEx pattern.
- `keepstopwords: bool`, default=`False`  
Specifies whether stop words should be kept (`True`) or discarded (`False`).
- `mode: {"none", "normal", "extended", "full", "custom (custom pattern)"}`, default=`"normal"`  
Defines which special characters contained in words should be removed.
Can be `"none"`, `"normal"`, `"extended"`, `"full"`, or any valid RegEx pattern preceded by the
characters `"custom "` (e.g. "custom a|b").
The predefined RegEx patterns are as follows:
  - `"none"`: no RegEx pattern (keeps words unchanged)
  - `"normal"`: `^\W+|\W+$`
  - `"extended"`: `^[^\w°؋฿₿¢₡₵$₫֏€ƒ₲₾₴₭₺₼₥₦₱£﷼៛ރ₽₨௹₹৲૱₪₸₮₩¥₳₠₢₯₣₤₶ℳ₧₰₷©™®]+|[^\w°؋฿₿¢₡₵$₫֏€ƒ₲₾₴₭₺₼₥₦₱£﷼៛ރ₽₨௹₹৲૱₪₸₮₩¥₳₠₢₯₣₤₶ℳ₧₰₷©™®]+$`
  - `"full"`: `\W`
- `chng: bool`, default=`True`  
Specifies whether words should be  lemmatized (`True`) or not (`False`).

#### Returns:
- `textlist: [str, ...]`    
The pre-processed text as a list of tokens.

### asolut.freqs
```python
asolut.freqs(textlist, sortedby="sum", returntype="plot", figtitle="plot", numb=None)
```
Calculates the frequencies of words by taking into account their synonyms.
#### Parameters:
- `textlist: [str, ...]`  
A list of tokens. Preferably, word-level tokens.
- `sortedby: {"frequencies", "synonym frequencies", "sum"}`, default=`"sum"`  
Specifies the type of frequency the output should be ordered by (descending).
  - `"frequencies"`: Standard word frequencies.
  - `"synonym frequencies"`: Solely word synonym frequencies.
  - `"sum"`: The sum of both synonym and word frequencies.
- `returntype: {"plot", "data", "both"}`, default=`"plot"`  
Specifies the output of the function.
  - `"plot"`: Creates and saves an interactive html horizontal stacked bar chart. Returns `None`.
  - `"data"`: Returns the resulting information as a `pandas.DataFrame` object.
  - `"both"`: Creates and saves the interactive html barplot and returns the information as a `pandas.DataFrame` object.

If a plot is chosen to be generated, it is of the following format:
<p align="center">
  <img src="https://user-images.githubusercontent.com/46795338/94809872-e8a90e00-03fb-11eb-8756-61a1059009f7.png" width=70%>
</p>

- `figtitle: str`, default=`"plot"`  
If a plot was chosen to be created, this parameter specifies the filename under which it will be saved.
- `numb: int`, default=`None`  
Specifies the number of bars depicted in the barplot. The value of `numb` is given by this function:

$$
numb = 
\begin{cases} 
min(15, n\\_unique, numb\\_input) & \text{, if } numb\\_input \gt 0 \\
min(15, n\\_unique) & \text{, if } numb\\_input \le 0
\end{cases} 
$$

where `n_unique` is the number of unique words after pre-processing
and `numb_input` is the user input for the `numb` parameter. The input must be a positive integer.

#### Returns: 
- `data: pandas.DataFrame or None`  
The DataFrame containing the calculated counts. It is of the following format:

| Words     | Counts | Synonym Counts | List of synonyms      |
|-----------|--------|----------------|-----------------------|
| headphone | 1      | 3              | [earphone, earpiece]  |
| flower    | 1      | 0              | []                    |
| earphone  | 2      | 2              | [earpiece, headphone] |
| earpiece  | 1      | 3              | [earphone, headphone] |

### asolut.gui
```python
asolut.gui()
```
Displays a graphical user interface that serves as a wrapper for the aforementioned functions,
in order to make the tool accessible to non developers. Can only generate the horizontal stacked bar chart.
