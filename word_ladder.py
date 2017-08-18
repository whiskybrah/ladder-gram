from collections import defaultdict
from itertools import product

'''def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]'''

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