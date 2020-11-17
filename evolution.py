from __future__ import print_function

from string import ascii_lowercase
from random import random, choice
from typing import List


class Creature:
    def __init__(self, appearance, genes):
        self.appearance = appearance
        self.genes = genes

    def __lt__(self, other):
        return self.appearance < other.appearance

    def __str__(self):
        return str(self.appearance)

    def get_appearance(self):
        return self.appearance

    def get_genes(self):
        return self.genes


def match(member1, member2):
  str1 = member1.get_appearance()
  str2 = member2.get_appearance()
  mismatch = 0
  for c1,c2 in zip(str1,str2):
    if c1 != c2:
      mismatch += 1
  return mismatch

def random_str(str_len):
    out_str = []
    for i in range(0, str_len):
        out_str.append(choice(ascii_lowercase + " "))
    out_str = "".join(out_str)
    return out_str


def mutate(member: Creature):
    input_str = member.get_appearance()
    genes = member.get_genes()
    genes.append(input_str)

    input_str = list(input_str)
    max_index = len(input_str)
    mutated_index = choice(range(0, max_index))
    mutation_char = choice(ascii_lowercase + " ")

    output_str = input_str[:]
    output_str[mutated_index] = mutation_char
    output_str = "".join(output_str)

    mutated = Creature(output_str, genes)
    return mutated


def reproduce(member: Creature, k: int):
    output = []
    for i in range(0, k):
        output.append(mutate(member))
    return output


def select(offsprings: list[str], selection, size):
    survival_value = map(lambda x: (match(x, selection), x), offsprings)
    select = list(map(lambda xy: xy[1], sorted(survival_value)[:size]))
    return select


def next_generation(generation, offspring_size, survival_size, selection_word):
    offsprings = []
    for member in generation:
        offsprings += reproduce(member, offspring_size)
    next_generation = select(offsprings, selection_word, survival_size)
    return next_generation


def is_present(selection: Creature, generation):
    selection_word = selection.get_appearance()
    generation_words = list(map(lambda x: x.get_appearance(), generation))
    return selection_word in generation_words


def evolution(selection_word: str, max_num_generations: int = 500):
    selection_word = selection_word.lower()
    random = random_str(len(selection_word))
    selection = Creature(selection_word, [])
    root = Creature(random, [])
    generation: list[Creature] = [root]
    num_of_springs = 100
    num_of_select = 10
    generation_index = 1
    while True:
        generation = next_generation(generation, num_of_springs, num_of_select, selection)
        if is_present(selection, generation):
            break
        generation_index += 1
        if generation_index > max_num_generations:
            raise Exception("Not reached in the maximal number of generations")

    return generation[0], generation_index


def print_evolution(sentence):
    out = evolution(sentence)
    number_of_generations = out[1]
    best = out[0]
    return str(number_of_generations) + ", " + best.get_appearance()


def print_genes(sentence):
    out = evolution(sentence)
    best = out[0]
    for gene in best.get_genes():
        print(gene)
    print(best.get_appearance())
