#!/usr/bin/env python -*- coding: utf-8 -*-

from nltk import sent_tokenize

from texeval import TexEval2015
from util import xmldoc2txt, wikicorpus


teval = TexEval2015()

terms = [term for termid, term in teval.terms('food')]

for xmldoc in wikicorpus('wiki.xml'):
    doc = xmldoc2txt(xmldoc)
    if any(i for i in term if term in doc):
        for line in doc.split('\n'):
            if term.lower() in line.lower() and line.lower() != term.lower(): 
                print term, line