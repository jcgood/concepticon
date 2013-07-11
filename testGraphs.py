#!/sw/bin/python2.4


### TODO ####: PRINT OUT FORM FEATURES FOR COMPONENTS

# Changes for 2.6?
#from rdflib.Graph import Graph
#from rdflib.Namespace import Namespace
#from rdflib.Graph import QuotedGraph

from rdflib import Graph
from rdflib import Namespace
#from rdflib import QuotedGraph

from rdflib import URIRef, Literal, BNode, Namespace
from rdflib import RDF

import re

import pprint


store = Graph()

store.load("/Volumes/Obang/MyDocuments/Digital/LEGO/MLODE/Lego-Unified.rdf")
store.load("/Volumes/Obang/MyDocuments/Digital/LEGO/MLODE/Saramaccan_Good_2009_1.rdf")
store.load("/Volumes/Obang/MyDocuments/Digital/LEGO/MLODE/Archi_Khalilov_2006_1.rdf")
store.load("/Volumes/Obang/MyDocuments/Digital/LEGO/MLODE/Abar.Missong_Hamm.Diller.Diller.Tiati_1.rdf")

#stuff = store.predicate_objects("http://purl.org/linguistics/concept/763")
#stuff = store.triples((URIRef('http://purl.org/linguistics/lego/concept/763'),URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'),URIRef('http://purl.org/linguistics/gold/SemanticUnit')))
#stuff = store.triples((None,None,URIRef('http://purl.org/linguistics/gold/SemanticUnit')))
stuff = store.triples((URIRef('http://purl.org/linguistics/lego/concept/763'),None,None))

for s,p,o in stuff:

	#print s,p,o

	if p.count("http://purl.org/linguistics/lego/hasCounterpart") > 0:
	
		#print o
		
		morestuff = store.triples((o,URIRef('http://purl.org/linguistics/gold/hasForm'),None))
		
		for s,p,o in morestuff:
		
			moremorestuff = store.triples((o,URIRef('http://purl.org/linguistics/gold/stringRep'),None))

			for s,p,o in moremorestuff:
				
				print s,p,o.encode('UTF-8')