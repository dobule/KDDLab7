# Name: Ryan Gelston and John Torres
# Assignment: Lab 7
# Description: Command-line tool that takes a graph file and outputs the 
#  pagerank of every vertex in the graph.
#
# Usage: python3 pageRank.py [graphFile]

import sys
import rankutil as ru
import pralg as pr

def print_usage_message():
   print("python3 pageRank.py [graphFile]")


def main():

   if len(sys.argv) != 2:
      print_usage_message()
      return

   graphPath = sys.argv[1]

   weight_f = lambda x, y: 1

   graph, vertSchema = ru.read_graph_file(graphPath, weight_f)

   rank = pr.page_rank(graph, 0.85, 0.00001)

   
   zipped = list(zip(vertSchema, rank))
   zipped.sort(key=lambda x: x[1], reverse=True)

   ru.print_pageranks(zipped)

   return 0


if __name__=="__main__":
   main()
