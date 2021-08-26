from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from nltk import trigrams
from collections import defaultdict
from random import choices
from random import choice


def corp_stats(file_name):
    f = open(file_name, "r", encoding="utf-8")
    text = f.read()
    tk = WhitespaceTokenizer()
    corpus = tk.tokenize(text)
    # unique = sorted(set(corpus))
    # print("Corpus statistics")
    # print(F"All tokens: {len(corpus)}")
    # print(F"Unique tokens: {len(set(unique))}")
    return corpus


def print_index(ind, corpus):
    try:
        index = int(ind)
    except Exception:
        print("Typ Error. Please input an integer.")
        return
    if isinstance(index, str):
        print("Typ Error. Please input an integer.")
    elif index > len(corpus):
        print("Index Error. Please input an integer that is in the range of the corpus.")
    else:
        print(F"Head: {corpus[index][0]} Tail: {corpus[index][1]}")


def find_bigrams(corpus):
    bigram = list(bigrams(corpus))
    # print(F"Number of bigrams: {len(bigram)}")
    return bigram


def find_trigrams(corpus):
    trgrm = list(trigrams(corpus))
    # print(F"Number of trigrams: {len(trgrm)}")
    return trgrm


def create_markov_bgrms(bigrms):
    bigrams_dict = defaultdict(dict)
    for i in bigrms:
        bigrams_dict[i[0]].setdefault(i[1], 0)
        bigrams_dict[i[0]][i[1]] += 1
    return bigrams_dict


def create_markov_trigrams(trigrms):
    trigrams_dict = defaultdict(dict)
    for i in trigrms:
        head = ' '.join((i[0], i[1]))
        trigrams_dict[head].setdefault(i[2], 0)
        trigrams_dict[head][i[2]] += 1
    return trigrams_dict


def print_markov(bigrams_dict, word):
    print(f"Head: {word}")
    if bigrams_dict[word]:
        for key, value in bigrams_dict[word].items():
            print(f"Tail: {key}    Count: {value}")
    else:
        print("The requested word is not in the model. Please input another word.")


def generate_random(trigrams_dict):
    start = []
    for word in trigrams_dict.keys():
        words = word.split()
        if word[0].isupper() and not words[0].endswith(('!', '.', '?')):
            start.append(word)
    for i in range(10):
        wrd = choice(start)
        word_list = [wrd]
        counter = 2
        while True:
            key_list = list()
            value_list = list()
            for key, value in trigrams_dict[wrd].items():
                key_list.append(key)
                value_list.append(value)
            old_wrd = wrd
            old_wrd = old_wrd.split()
            new_wrd = choices(key_list, value_list)
            new_wrd = ''.join(new_wrd)
            if counter >= 5 and wrd.endswith(('!', '.', '?')):
                break
            word_list.append(new_wrd)
            counter += 1
            wrd = ' '.join((old_wrd[1], new_wrd))
        print(' '.join(word_list))


def main():
    file_name = input()
    corp = corp_stats(file_name)
    trigrm = find_trigrams(corp)
    trigrams_dict = create_markov_trigrams(trigrm)
    generate_random(trigrams_dict)


if __name__ == "__main__":
    main()
