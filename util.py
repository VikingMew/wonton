#!/usr/bin/env python -*- coding: utf-8 -*-

import io

def xmldoc2txt(xmldoc):
    """
    wikixml = 'wiki.xml'

    for i in wikicorpus(wikixml):
        print xmldoc2txt(i)
        break
    """
    return xmldoc.partition('>')[2].partition('<')[0].strip()

def wikicorpus(xmlfile):
    """ 
    Iterates through the xml file document by document
    
    >>> for xmldoc in wikicorpus('test.xml'):
    >>>     print xmldoc
    """
    with io.open(xmlfile, 'r', encoding='utf8') as fin:
        doc = []
        for line in fin:
            # Skips empty lines
            if not line.strip(): continue
            # When document ends
            if line.endswith('</doc>\n'):
                doc.append(line.strip())
                yield "\n".join(doc)
                doc = []
            else:
                doc.append(line.strip())
                

def lev(s, t):
    ''' From Wikipedia article; Iterative with two matrix rows. '''
    if s == t: return 0
    elif len(s) == 0: return len(t)
    elif len(t) == 0: return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]
    return v1[len(t)]

import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
 
def cosine(text1, text2):
    return get_cosine(text_to_vector(text1), text_to_vector(text2))