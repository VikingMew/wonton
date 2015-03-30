#!/usr/bin/env python -*- coding: utf-8 -*-

import io, os
from collections import defaultdict
#from natsort import natsorted

class TexEval2015:
    def __init__(self):
        _trial_subcorpora = ['ontolearn_AI', 'WN_plants', 'WN_vehicles']
        _test_subcorpora = ['chemical', 'equipment', 'food', 'science', 
                                'WN_chemical', 'WN_equipment', 'WN_food', 
                                'WN_science']
        self.domains = [i for i in _test_subcorpora if not i.startswith("WN_")]
        self.corpus_directory = 'TExEval2015/'
        self.texeval_subcorpora = {'test': _test_subcorpora,
                                   'trial': _trial_subcorpora}    
    
    def terms(self, subcorpus):
        """
        Input terms.
        
        >>> teval = TexEval2015()
        >>> for termid, term in teval.terms('ontolearn_AI'):
        ...     print termid, term
        """
        termfile = os.path.join(self.corpus_directory, subcorpus+'.terms')
        for i in io.open(termfile, 'r'):
            termid, term = i.strip().split('\t')
            yield int(termid), term 
    
    def taxo(self, subcorpus):
        """
        Gold ontology.
        
        >>> teval = TexEval2015()
        >>> for relid, term, hypernym in teval.taxo('trial', 'onotlearn_AI'):
        ...     print relid, term, hypernym
        """
        taxofile = os.path.join(self.corpus_directory, subcorpus+'.taxo')
        for i in io.open(taxofile, 'r'):
            relid, term, hypernym = i.strip().split('\t')
            yield int(relid), term, hypernym
    
    def ontology(self, subcorpus):
        onto = defaultdict(list)
        for relid, term, hypernym in self.taxo(subcorpus):
            onto[term].append(hypernym)
        return onto