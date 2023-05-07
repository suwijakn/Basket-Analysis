from collections import defaultdict
from itertools import combinations

def generate_transactions(data):
  transactions = dict()
  for index, trans_item in data.iterrows():
    id = str(trans_item["Member_number"]) + '_' + str(trans_item['Date'])
    if id not in transactions:
      transactions[id] = []
    transactions[id].append(trans_item["itemDescription"])
  return transactions

def has_support(perm, one_itemsets):
  return frozenset({perm[0]}) in one_itemsets and \
          frozenset({perm[1]}) in one_itemsets

# Creating a list of itemsets with only one element
def calculate_itemsets_one(transactions, min_sup=0.01):

  N = len(transactions)

  temp = defaultdict(int)
  one_itemsets = dict()

  for key, items in transactions.items():
      for item in items:
        inx = frozenset({item})
        temp[inx] += 1

  # remove all items that is not supported.
  for key, itemset in temp.items():
      if itemset > min_sup * N:
          one_itemsets[key] = itemset

  return one_itemsets

def calculate_itemsets_two(transactions, one_itemsets):
  two_itemsets = defaultdict(int)

  for key, items in transactions.items():

      items = list(set(items))  # remove duplications

      if (len(items) > 2):
          for perm in combinations(items, 2):
              if has_support(perm, one_itemsets):
                  two_itemsets[frozenset(perm)] += 1
      elif len(items) == 2:
          if has_support(items, one_itemsets):
              two_itemsets[frozenset(items)] += 1
  return two_itemsets

def calculate_association_rules(one_itemsets, two_itemsets, N):
  rules = []
  for source, source_freq in one_itemsets.items():
      for key, group_freq in two_itemsets.items():
          if source.issubset(key):
              target = key.difference(source)
              support = group_freq / N
              confidence = group_freq / source_freq
              rules.append((next(iter(source)), next(iter(target)),
                            confidence, support))
  return rules

# You can now calculate the frequency sets
def calculate_support_confidence(transactions, min_sup=0.01):
  N = len(transactions)
  one_itemsets = calculate_itemsets_one(transactions, min_sup)
  two_itemsets = calculate_itemsets_two(transactions, one_itemsets)
  rules = calculate_association_rules(one_itemsets, two_itemsets, N)
  return sorted(rules)

