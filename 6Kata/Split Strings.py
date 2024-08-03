# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def split_into_pairs(s):
    # If the length of the string is odd, append an underscore
    if len(s) % 2 != 0:
        s += '_'

    # Initialize an empty list to store the pairs
    pairs = []

    # Iterate over the string, taking two characters at a time
    for i in range(0, len(s), 2):
        pairs.append(s[i:i + 2])

    return pairs


# import re
#
# def solution(s):
#     return re.findall(".{2}", s + "_")