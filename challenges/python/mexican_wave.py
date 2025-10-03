# CodeWars Challenge: [Mexican Wave]
# Link: [https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/python]
# Difficulty: [6 Kyu]

# Instructions
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return an array of strings where an uppercase letter is a person standing up. The input string will always consist of lowercase letters and spaces, but may be empty, in which case you must return an empty array. If the character in the string is whitespace then pass over it as if it was an empty seat.

# Examples
# "hello" => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# " s p a c e s " => [ " S p a c e s ", " s P a c e s ", " s p A c e s ", " s p a C e s ", " s p a c E s ", " s p a c e S "]
# "two words" => ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
# "gap" => [" Gap ", " gAp ", " gaP "]
# "a       b    " => ["A       b    ", "a       B    "]

def wave(people):
    mexican_wave = []
    for i in range(len(people)):
        if people[i] != ' ':
            wave = people[:i] + people[i].upper() + people[i+1:]
            mexican_wave.append(wave)
    return mexican_wave


# With list comprehension
def wave(people):
    return [people[:i] + people[i].upper() + people[i+1:]
            for i in range(len(people))
            if people[i] != ' ']


print(wave(""))
# --> []
print(wave("hello"))
# --> ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave(" s p a c e s "))
# --> [ " S p a c e s ", " s P a c e s ", " s p A c e s ", " s p a C e s ", " s p a c E s ", " s p a c e S "]
print(wave("two words"))
# --> ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
print(wave(" gap "))
# --> [" Gap ", " gAp ", " gaP "]
print(wave("a       b    "))
# --> ["A       b    ", "a       B    "]))
print(wave("this is a few words"))
# --> ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words", "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words", "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds", "this is a few woRds", "this is a few worDs", "this is a few wordS"]
