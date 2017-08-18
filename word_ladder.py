from collections import defaultdict
from itertools import product
import unittest
import os.path
from collections import deque

def startsearch(network, start): # uses breadth-first search
    nodevisited = set()  # create a set that keeps track of which arcs have been visited already
    q = deque([[start]])  # create a queue which contains all the paths from starting arc, created with a list
                          # that contains the start arc (named start)
    while q: # this begins the growing of paths, one at a time
        node = q.popleft()  # pop a path from the queue to continue exploring
                            # and retrieve the last arc visited from that path
        arc = node[-1]
        yield arc, node
        for nearby in network[arc] - nodevisited: # retrieve neighbours from network,
                                                  # remove the arcs that have already been visited
            nodevisited.add(nearby) # then for each of the remaining unvisted neighbours the arc is set to
                                    # visited and a path consisting of the path so far plus the arc is added
            q.append(node + [nearby])   # adding the new arc schedules it for further exploration,
                                        # but only when all other arcs on the adjaceny list have been explored

def wordretrieve(dictionary):
    for i in open(dictionary, 'r'):
        yield i[:-1]

def createGraph(wordList):
    network = defaultdict(set)
    containers = defaultdict(list) # create a list of containers which store words with characters in common together
    for word in wordList:
        for x in range(len(word)):
            container = '{}~{}'.format(word[:x], word[x + 1:]) # given a tilde wildcard, a single container
            # is defined by words that are similar within single characters
            # e.g. lea~ container would have -> leak, lean, leap, lead and more
            containers[container].append(word)
            # add arcs and edges for words in the same container
    for container, nearby in containers.items():
        for firstword, secondword in product(nearby, repeat=2): # because repeat=2, only two characters will be in each loop iteration
          # product () is the cartesian product which is equivalent to a nested for loop
            if firstword != secondword:
                network[secondword].add(firstword)
                network[firstword].add(secondword)
    return network

dictfile = input("Enter dictionary:")
if os.path.isfile(dictfile):
    dictionary = createGraph(wordretrieve(dictfile))
else:
    print("Incorrect file name")
    exit(0)

if __name__ == '__main__':
    startword = input("Enter start word:")
    targetword = input("Enter target word:")
    for arc, path in startsearch(dictionary, startword):
        if arc == targetword:
            print( ' -> '.join(path))

