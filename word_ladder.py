from collections import defaultdict
from itertools import product
import unittest
from collections import deque

def startsearch(network, start):
    q = deque([[start]])
    while q:
        node = q.popleft()
        arc = node[-1]
        yield arc, node

def wordretrieve(dictionary):
    for i in open(dictionary, 'r'):
        yield i[:-1]

def createGraph(wordList):
    network = defaultdict(set)
    containers = defaultdict(list)
    for word in wordList:
        for x in range(len(word)):
            container = '{}~{}'.format(word[:x], word[x + 1:])
            containers[container].append(word)
    for container, nearby in containers.items():
        for firstword, secondword in product(nearby, repeat=2):
            if firstword != secondword:
                network[secondword].add(firstword)
                network[firstword].add(secondword)
    return network

dictionary = createGraph(wordretrieve('dictionary.txt'))

if __name__ == '__main__':
    startword = input("Enter start word:")
    targetword = input("Enter target word:")
    for arc, path in startsearch(wordnetwork, startword):
        if arc == targetword:
            print( ' -> '.join(path))


class myTest(unittest.TestCase):
  def test_graph(self):
      print("setup")


unittest.main()