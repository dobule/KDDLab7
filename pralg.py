# Name: Ryan Gelston and John Torres
# Assignment: Lab 7
# Description: Impliments the pagerank algorithm.


import numpy as np
import scipy as sp
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize

def page_rank(graph, damp, maxError=0.0001):
   """ Runs page rank on the passed graph 
   
      graph -- The graph in the form of a matrix. Assumes that graph is a 
         numpy matrix
      damp -- Dampening coefficient
      maxError -- maximum allowable difference between prevRank and curRank
   """

   numVert = graph.shape[0]
   curRank = np.ones(numVert)
   curRank = curRank / np.linalg.norm(curRank, 1)

   # + 1 assures the while loop enters
   curError = maxError + 1

   graph = normalize(graph, norm='l1', axis=0)

   while curError > maxError:
      prevRank = curRank
      curRank = graph * prevRank.T
      curRank = ((1 - damp) / numVert) + (damp * curRank)
      curError = np.linalg.norm(curRank - prevRank, 2)

   # Normalize the rank vector
   curRank = [r / sum(curRank) for r in curRank]

   return curRank

