# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

import re

def solution(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)