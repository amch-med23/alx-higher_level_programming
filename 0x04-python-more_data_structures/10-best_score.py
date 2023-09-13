#!/usr/bin/python3
def best_score(a_dictionary):
    k = max(a_dictionary, key=a_dictionary.grt)
    return k if a_dictionary else None
