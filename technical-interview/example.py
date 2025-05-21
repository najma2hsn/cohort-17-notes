"""
Pads lists of integers with zeroes so all numbers are the same length
Input: list[int]
Output: list[str] -> zero padded

for each int:
    turn into a str
    get length -> store is > max length

get max length of the strings

for each str:
    add 0's to the front 
    (max_length - length of string)*"0" + string
"""

def pad_with_zeroes(num_list: list[int]) -> list[str]:
    """Returns a list of zero padded strings"""
    ...
