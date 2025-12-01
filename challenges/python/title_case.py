# CodeWars Challenge: [Title Case]
# Link: [https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python]
# Difficulty: [6 Kyu]

# Instructions
# A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

# Arguments
# First argument (required): the original string to be converted.
# Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string.

# Examples
# title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
# title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
# title_case('the quick brown fox') # should return: 'The Quick Brown Fox'

def title_case(title, minor_words=''):
    title = title.lower().split()
    minor_words = minor_words.lower().split()
    result = []

    for i, word in enumerate(title):
        if i == 0 or word not in minor_words:
            result.append(word.capitalize())
        else:
            result.append(word)

    return ' '.join(result)


def title_case(title, minor_words=''):
    words = title.lower().split()
    minor_words_list = minor_words.lower().split()

    return ' '.join(word.capitalize() if i == 0 or word not in minor_words_list else word for i, word in enumerate(words))


# def title_case(title, minor_words=''):
#     title = title.capitalize().split()
#     minor_words = minor_words.lower().split()

#     return ' '.join(word if word in minor_words else word.capitalize() for word in title)


# def title_case(title, minor_words=''):
#     title = title.capitalize().split()
#     minor_words = minor_words.lower().split()
#     result = []

#     for word in title:
#         if word in minor_words:
#             result.append(word)
#         else:
#             result.append(word.capitalize())

#     return ' '.join(result)


print(title_case('a clash of KINGS', 'a an the of'))  # -->  'A Clash of Kings'
# -->  'The Wind in the Willows'
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox'))  # -->  'The Quick Brown Fox'
print(title_case(''))  # -->  ''
