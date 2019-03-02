# Name: Ryan Gelston and John Torres
# Assignment: Lab 7
# Description: Utility functions for the pagerank algorithm and pagerank
#  command line programs

import numpy as np
from scipy.sparse import csr_matrix


##########################################################
# Read Graph From File
##########################################################


def read_graph_file(filePath, weight_f):
   """ Reads a graph from the passed path and translates it into a 
      scipy csr_matrix

      filePath -- Path to a directed graph in the form of a csv file
      weight_f -- Determines the weight of an edge given two numbers
   """

   with open(filePath, 'r') as f:
      rawGraph = f.read()

   rawGraph = rawGraph.split('\n')
   rawGraph = [edge.split(',') for edge in rawGraph if edge != '']
   rawGraph = [(edge[0][1:-1], float(edge[1]), edge[2][1:-1], float(edge[3]))
               for edge in rawGraph]

   vertexList = []

   for edge in rawGraph:
      if edge[0] not in vertexList:
         vertexList.append(edge[0])
      if edge[2] not in vertexList:
         vertexList.append(edge[2])

   print(vertexList)

   fromVertex = np.array([vertexList.index(edge[0])
                          for edge in rawGraph])
   toVertex = np.array([vertexList.index(edge[2])
                        for edge in rawGraph])
 
   edgeWeight = np.array([weight_f(edge[1], edge[3]) 
                          for edge in rawGraph])

   print(fromVertex)
   print(toVertex)
   print(edgeWeight)


   return csr_matrix((edgeWeight, (fromVertex, toVertex)),
                     shape=(len(vertexList), len(vertexList)))


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
