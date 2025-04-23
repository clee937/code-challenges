
 #CodeWars Challenge: [A needle in the Haystack]
 #Link: [https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python]
 #Difficulty: [8 Kyu]

# Instructions

# Can you find the needle in the haystack? Write a function findNeedle() that takes an array full of junk but containing one "needle". After your function finds the needle it should return a message (as a string) that says: "found the needle at position " plus the index it found the needle.
 

def find_needle(haystack):
    for index in range(len(haystack)):
        if (haystack[index] == "needle"):
            return f'found the needle at position {index}'
            # return 'found the needle at position ' + str(index) 
            
            
# def find_needle(haystack):
#     if 'needle' in haystack:
#         return 'found the needle at position %d' % haystack.index('needle')

# def find_needle(haystack): 
# 	return 'found the needle at position %d' % haystack.index('needle')
    
# def find_needle(haystack):
#     index = haystack.index("needle")
#     return f'found the needle at position {index}'

# def find_needle(haystack):
#     return f'found the needle at position {haystack.index("needle")}'

# def find_needle(haystack):
#     index = haystack.index('needle')
#     return 'found the needle at position {}'.format(index)

# def find_needle(haystack):
#     for word in haystack:
#         if word == 'needle':
#             return "found the needle at position " + str(haystack.index('needle'))


find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])   
# found the needle at position 5    
