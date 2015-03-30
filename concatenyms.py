#!/usr/bin/env python -*- coding: utf-8 -*-

from __future__ import unicode_literals

import io, sys, string
from collections import defaultdict
from itertools import chain
from difflib import SequenceMatcher as levdist
#reload(sys); sys.setdefaultencoding("utf-8")

from texeval import TexEval2015
from util import cosine

teval = TexEval2015()
 

def s1(t1, terms):
    return set([t2 for t2 in terms if t1 != t2 and len(t1)>3 
                and t2 in t1]) 

def s2(t1, terms):
    return set([t2 for t2 in terms if t1 != t2 and len(t1)>3 
                and t1.endswith(t2)])

def s3(t1, terms):
    return set([t2 for t2 in terms if t1 != t2 and len(t1)>3 
                and cosine(t1,t2) > 0.8])
    
def prec_rec_fscore(tp, fp, tn):
    prec = tp / float(tp+fp)
    rec = tp / float(tp+tn)
    fscore = 2 * prec*rec / (prec+rec)
    return prec, rec, fscore


for domain in teval.domains:
    terms = [term for termid, term in teval.terms(domain)]
    gold_onto = teval.ontology(domain)
    
    concato = defaultdict(set)
    for hid, hypo, hyper in teval.taxo(domain):
        concatenyms = s3(hypo, terms)
        concato[hypo].update(concatenyms)
        
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    for term in gold_onto:
        hypernyms = gold_onto[term]
        concatenyms = concato[term]
        true_positives += len(concatenyms.intersection(hypernyms))
        false_positives += len([i for i in concatenyms if i not in hypernyms])  
        false_negatives += len([i for i in hypernyms if i not in concatenyms])
        
    print prec_rec_fscore(true_positives, false_positives, false_negatives)
    

"""
# S1
(0.12485207100591716, 0.09352460007253093, 0.1069412767525975)
(0.7707509881422925, 0.3170731707317073, 0.44930875576036866)
(0.33233233233233234, 0.2091997479521109, 0.25676720804331016)
(0.5261194029850746, 0.3032258064516129, 0.38472032742155526)

# S2
(0.187291280148423, 0.08135552242414473, 0.11343652554990588)
(0.7883817427385892, 0.3089430894308943, 0.4439252336448598)
(0.6326530612244898, 0.17580340264650285, 0.27514792899408286)
(0.6373056994818653, 0.2645161290322581, 0.37386018237082064)


"""