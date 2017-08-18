import re
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

'''def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()'''

def wordretrieve(dictionary):
    for i in open(dictionary, 'r'):
        # tba?

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
    for x, a in startsearch(wordnetwork, startword):
        if x == targetword:
            print( '  '.join(a))