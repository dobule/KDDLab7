# Name: Ryan Gelston and John Torres
# Assignment: Lab 7
# Description: Utility functions for the pagerank algorithm and pagerank
#  command line programs

from scipy.sparse import csr_matrix

##########################################################
# Read Graph From File
##########################################################

def read_graph_file(filePath):
   """ Reads a graph from the passed path and translates it into a 
      scipy csr_matrix
   """

###########################################################
# Printing Functions
###########################################################

def print_page(pageName, pageScore):
   """ Prints the pagerank of a single vertex """
   print("obj: %s with pagerank: %f" % (pageName, pageScore))


def print_pageranks(pageranks):
   """ Prints the pageranks for a list of verticies 
   
      pageranks -- [(vertexName, pagerankScore), ...]
   """

   #TODO: Sort the pageranks in decending order

   for name, score in pageranks:
      print_page(name, score)
