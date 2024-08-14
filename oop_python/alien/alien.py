'''
Given a sorted dictionary of an alien language, find the order of characters in the alphabet.

{
"words": ["baa", "abcd", "abca", "cab", "cad"] --> "bdac"
"words": ["caa", "aaa", "aab"] --> "cab"
}

Given dictionary is sorted in the lexicographical order of the alien language.
Output is a string consisting of all the characters of the alien alphabet, in order.
'''

def create_alpha_list(words):
    alpha_dict = {}
    