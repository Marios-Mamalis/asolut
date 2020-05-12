"""MIT License
Copyright (c) 2019 Marios Mamalis
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from re import sub, search, split
from inflect import engine
import numpy as np
from itertools import chain
from plotly import offline
import plotly.graph_objects as go
from pandas import DataFrame
from os import path
import eel
from tkinter import Tk
from tkinter.filedialog import askopenfile
from encodings.aliases import aliases
import codecs
import logging

def preprocessing(texts, pos=None, chrsplt='\s|\\\\|/', keepstopwords=False, mode='normal', chng=True):

    eng = engine()
    wnl = WordNetLemmatizer()

    # parts of speech to include
    if pos is None:
        pos = ['JJ', 'JJR', 'JJS',
               'NN', 'NNS', 'NNP', 'NNPS',
               'RB', 'RBR', 'RBS', 'VB',
               'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

    # regex filter
    if mode == "none":
        # keep everything
        def _substi(word):
            return word
    elif mode == "normal":
        # remove symbols at the end and the start
        def _substi(word):
            return sub(r"^[^\w]+|[^\w]+$", "", word)
    elif mode == "extended":
        # remove symbols at the end and the start with exceptions for common meaningful characters
        def _substi(word):
            return sub(r"^[^\w°؋฿₿¢₡₵$₫֏€ƒ₲₾₴₭₺₼₥₦₱£﷼៛ރ₽₨௹₹৲૱₪₸₮₩¥₳₠₢₯₣₤₶ℳ₧₰₷©™®]+|"
                          r"[^\w°؋฿₿¢₡₵$₫֏€ƒ₲₾₴₭₺₼₥₦₱£﷼៛ރ₽₨௹₹৲૱₪₸₮₩¥₳₠₢₯₣₤₶ℳ₧₰₷©™®]+$", "", word)
    elif mode == "full":
        # remove all symbols
        def _substi(word):
            return sub(r"\W", "", word)
    elif "custom" in mode:
        # custom regex
        def _substi(word):
            return sub(str(mode[7:]), "", word)
    else:
        logging.warning('mode' + str(mode) + ' is not valid. Default normal mode selected.')

        def _substi(word):
            return sub(r"^[^\w]+|[^\w]+$", "", word)


    # unite parts of speech
    def _changee(word, poss):
        if poss in ["NN", "NNP", "NNPS", "NNS"]:
            if eng.singular_noun(str(word)):
                word = (eng.singular_noun(str(word)))
            else:
                word = (wnl.lemmatize(word, 'n'))
        elif poss in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]:
            word = (wnl.lemmatize(word, 'v'))
        elif poss in ["JJ", "JJR", "JJS"]:
            word = (wnl.lemmatize(word, 'a'))
        elif poss in ["RB", "RBR", "RBS"]:
            word = (wnl.lemmatize(word, 'r'))
        return word

    # split text
    textlist = split(chrsplt, texts)
    # drop empties
    textlist = list(filter(None, textlist))
    # character handling
    textlist = [_substi(i) for i in textlist]
    # drop empties
    textlist = list(filter(None, textlist))
    # words to lowercase
    textlist = [i.lower() for i in textlist]
    # drop stopwords
    if keepstopwords:
        pass
    else:
        textlist = [i for i in textlist if i not in stopwords.words('english')]
    # separate those that contain characters not filtered
    regexc = [i for i in textlist if search(r"\W", i)]
    textlist = [i for i in textlist if not search(r"\W", i)]
    # create tags
    textlist = pos_tag(textlist)
    # keep words with correct part of speech tags
    textlist = [(i, j) for i, j in textlist if j in pos]
    # lemmatize and edit words
    if chng==True:
        textlist = [_changee(i, j) for i, j in textlist]
    else:
        textlist = [i for i, j in textlist]
    # unite exceptions and edited words
    textlist = textlist + regexc
    return textlist


def freqs(textlist, sortedby='sum', returntype='plot', figtitle='plot', numb=None):
    ver = 0
    figtitle1 = figtitle
    while path.exists(figtitle + ".html"):
        ver += 1
        figtitle = figtitle1 + " (" + str(ver) + ")"

    # simple word frequencies
    words, counts = np.unique(np.array(textlist), return_counts=True)
    L = len(words.tolist())
    try:
        if numb <= 0:
            numb = None
    except:
        pass
    if numb is None:
        if L < 15:
            numb = L
        else:
            numb = 15
    try:
        if numb > L:
            numb = L
    except:
        pass
    tags = np.array([j for i, j in pos_tag(words.tolist())])
    # synonym frequencies
    syncounts = np.empty(shape=[1, len(counts)], dtype=int)[0]
    listofsynonyms = np.empty(shape=[1, len(counts)], dtype=np.ndarray)[0]
    empty = np.array([0 for uu in range(len(words))])
    num = 0
    for i in words:
        # find synonyms for i
        if tags[num] in ["NN", "NNP", "NNPS", "NNS"]:
            listofsynonyms[num] = np.array(list(set([k.lower() for k in list(set(
                chain.from_iterable([j.lemma_names() for j in wn.synsets(i, 'n')])))
                                                     if (k.lower() in words) and (k.lower() != i)])))
        elif tags[num] in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]:
            listofsynonyms[num] = np.array(list(set([k.lower() for k in list(set(
                chain.from_iterable([j.lemma_names() for j in wn.synsets(i, 'v')])))
                                                     if (k.lower() in words) and (k.lower() != i)])))
        elif tags[num] in ["JJ", "JJR", "JJS"]:
            listofsynonyms[num] = np.array(list(set([k.lower() for k in list(set(
                chain.from_iterable([j.lemma_names() for j in wn.synsets(i, 'a')])))
                                                     if (k.lower() in words) and (k.lower() != i)])))
        elif tags[num] in ["RB", "RBR", "RBS"]:
            listofsynonyms[num] = np.array(list(set([k.lower() for k in list(set(
                chain.from_iterable([j.lemma_names() for j in wn.synsets(i, 'r')])))
                                                     if (k.lower() in words) and (k.lower() != i)])))
        else:
            listofsynonyms[num] = np.array([])
        # find their existence in the unique words np.array
        syncounts[num] = np.sum((np.where(np.isin(words, listofsynonyms[num]), counts, empty)))
        num += 1
    # sorting
    if sortedby == "frequencies":
        ordr = np.argsort(counts)
    elif sortedby == "synonym frequencies":
        ordr = np.argsort(syncounts)
    elif sortedby == "sum":
        total = np.add(counts, syncounts)
        ordr = np.argsort(total)
    else:
        logging.warning("Not valid sortedby input: " + str(sortedby) + " is not a valid input. Sorting by sum.")
        total = np.add(counts, syncounts)
        ordr = np.argsort(total)
    words = words[ordr]
    counts = counts[ordr]
    syncounts = syncounts[ordr]
    listofsynonyms = listofsynonyms[ordr]
    # plotting with plotly
    if returntype == "plot" or returntype == "both":
        endind = len(words)
        maxcount = syncounts[(endind-numb):endind].tolist()[-1]+counts[(endind-numb):endind].tolist()[-1]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=words[(endind-numb):endind].tolist(),
            x=counts[(endind-numb):endind].tolist(),
            hovertext=[k+' '+j for j, k in zip([str(i) for i in counts[(endind-numb):endind].tolist()],
                                               words[(endind-numb):endind].tolist())],
            hoverinfo="text",
            name="Words' Frequencies",
            orientation='h',
            marker=dict(
                color='rgba(58, 71, 80, 0.6)',
                line=dict(color='rgba(58, 71, 80, 1.0)', width=15/numb)
            )
        ))
        fig.add_trace(go.Bar(
            y=words[(endind-numb):endind].tolist(),
            x=syncounts[(endind-numb):endind].tolist(),
            hovertext=[k+' '+j for j, k in zip([str(i) for i in syncounts[(endind-numb):endind].tolist()],
                                               [', '.join(listofsynonyms[i].tolist())
                                                for i in range((endind-numb), endind)])],
            hoverinfo="text",
            name="Words' Synonyms' Frequencies",
            orientation='h',
            marker=dict(
                color='rgba(225, 145, 65, 0.6)',
                line=dict(color='rgba(225, 145, 65, 1.0)', width=15/numb)
            )
        ))

        fig.update_layout(barmode='stack',
                          xaxis_title="Counts",
                          yaxis_title="Words",
                          title_text=("Paper's doi:<br>" +
                                      "<a href='doi'>" +
                                      "A solution for the synonym problem in word frequency algorithms</a>"),
                          title_font=dict(
                              size=10),
                          xaxis=dict(
                              tickmode='linear',
                              tick0=0,
                              dtick=maxcount//8
                          ))

        offline.plot(fig, filename=figtitle + '.html')
        if returntype == 'both':
            df = DataFrame([words, counts, syncounts, listofsynonyms]).T
            df.rename(columns={
                0: 'Words',
                1: 'Counts',
                2: 'Synonym Counts',
                3: 'List of synonyms'
            }, inplace=True)
            return df
        elif returntype == 'plot':
            pass
    elif returntype == "data":
        df = DataFrame([words, counts, syncounts, listofsynonyms]).T
        df.rename(columns = {
            0: 'Words',
            1: 'Counts',
            2: 'Synonym Counts',
            3: 'List of synonyms'
        }, inplace=True)
        return df
    else:
        logging.error("Not valid return type")


def gui():
    enccs = sorted(list(set([k for k, v in aliases.items()] + [v for k, v in aliases.items()])))
    eel.init(path.dirname(path.realpath(__file__)) + '/web')
    trmodes = ["none", "normal", "extended", "full"]
    sormodes = ["frequencies", "synonym frequencies", "sum"]

    @eel.expose
    def open_file():
        global ask
        root = Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        asknew = askopenfile(filetypes=[("Text files", "*.txt")])
        if asknew is not None:
            ask = asknew
        return ask.name

    @eel.expose
    def init_tug():
        try:
            x = eel.get_to_python()()
            with codecs.open(ask.name, encoding=x[0]) as filename:
                if filename is not None:
                    content = filename.read()
            if not x[3]:
                x[3] = None
            freqs(textlist=preprocessing(texts=content, pos=x[3], keepstopwords=x[2], mode=trmodes[int(x[1]) - 1]),
                          sortedby=sormodes[int(x[4])-1], returntype='plot', figtitle='plot', numb=int(x[5]))
            eel.endit()
        except:
            logging.error("Something went wrong")
            eel.endit()
            raise

    @eel.expose
    def encs():
        return enccs

    eel.start('main.html', size=(600, 850), port=8118)
