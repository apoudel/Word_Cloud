# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:30:50 2016

@author: jamiehand, with help from Pete Johnson's CS150 examples
"""

import string
from stop_words import get_stop_words

def read_words(filename):
    """
    Read lines from a file, strip newlines and punctuation from the lines,
    split the lines into words, make each word lowercase, and return a
    list of those words.
    Ideas on translate (for removing puctuation) from:
    http://stackoverflow.com/a/266162/4979097
    and http://stackoverflow.com/a/12453622/4979097
    """

    translate_table = str.maketrans("","", string.punctuation)  # NOTE: this removes apostrophes, too
    words = []
    f = open(filename, "r")

    # strip newlines at the end, remove punctuation from the line, then split
    # into individual words -- then make each word lowercase and add it into
    # the words list
    for line in f:
        #print(line)
        words += (word.lower() for word in line.strip(string.whitespace).translate(translate_table).split())

    f.close()
    return words


def count_words(word_list):
    """
    Traverse word_list to find out how many times each word appears.
    Return a dictionary with word as the key and that word's frequency as
    the value.
    """
    word_with_frequency_dict = dict()
    for word in word_list:
        if word in word_with_frequency_dict:
            word_with_frequency_dict[word] += 1
        else:
            word_with_frequency_dict[word] = 1

    return word_with_frequency_dict

def remove_stop_words(word_dict):
    """
    Take out stop words
    """
    stop_words = get_stop_words('en')
    # make keys into new list, so we can change the dict's size (i.e.
    # delete keys) while iterating over the dict's keys
    for word in list(word_dict.keys()):
        if word in stop_words:
            del word_dict[word]


def get_most_frequent(word_dict, num_words):
    """
    Sort keys (words) by value and then extract the top num_words,
    or duplicate the dictionary and then find the largest key/value pair in
    the dictionary (get max value) and remove that key/value pair 10 times.
    Ideas here: http://stackoverflow.com/a/280156/4979097
    """
    most_freq = []
    while(len(most_freq) < num_words and len(word_dict.keys()) > 0):
#        max_word = max(word_with_frequency_dict,
#                       key=lambda x: word_with_frequency_dict[x[0]])
        max_word = max(word_dict, key=word_dict.get)  # dict.get() returns value for given key
        most_freq.append((max_word, word_dict[max_word]))
        # NOTE only removing from word_dict b/c we know we won't need it
        # again! TODO way to do this w/o deleting from word_dict?
        del word_dict[max_word]
    return most_freq

def write_words_to_file(word_tuples, year):
    """
    Take in a list of word tuples, and output them into a csv file,
    each on its own line
    """
    filename = "SOTU-csv/" + str(year)+".csv"
    f = open(filename, "w")
    f.write("word,freq,year\n")
    for tup in word_tuples:
        f.write(tup[0]+","+str(tup[1])+","+str(year)+"\n")

def txt_to_csv(input_filename, year):
    word_list = read_words(input_filename)
    word_dict = count_words(word_list)
    remove_stop_words(word_dict)
    word_tuples = get_most_frequent(word_dict,100000)
    write_words_to_file(word_tuples, year)
    print(word_tuples)


if __name__ == "__main__":
    txt_to_csv("2002.txt", 2002)
    # word_list = read_words("2002.txt")
    # word_dict = count_words(word_list)
    # remove_stop_words(word_dict)
    # word_tuples = get_most_frequent(word_dict,25)
    # write_words_to_file(word_tuples, 2002)


# TODO write file aggregator that outputs something like:
# word:___ freq:{[year:___, count:___], [year:___, count:___]}
