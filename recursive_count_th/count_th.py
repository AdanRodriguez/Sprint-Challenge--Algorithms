'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    #if word has 0 or 1 length return count of 0
    if len(word) <= 1:
        return count
    #else if it has th add +1 to count
    elif word[0] == "t" and word[1] == "h":
        count += 1
    return count_th(word[1:], count)