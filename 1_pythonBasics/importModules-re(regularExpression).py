


import re

string = "CAPITCAL LETTER , HI a sample .string"

new = re.sub('[A-Z]', '', string)
print(new)

new = re.sub('[a-z]', '', string)

print(new)

new = re.sub('[.,\']', '', string)   # remove all the punctuation from the string
                                     # here, . is within brakets, and matches any single character(many applications exclude newlines)

print(new)

new = re.sub('.', '', string)       # here, . is not within brakets, and matches literal dot "." another example is that [a.c] only matches "a", "." or "c"

print(new)

new = re.sub('[.,\'A-Z]', '', string) 

print(new)

new = re.sub('[.,\'A-Za-z]', '', string)  # print only spaces
print(new)

new = re.sub('[+" "]', '', string)  # remove the spaces
print(new)
                                    # + matches the preceding element one or more times. For example, ab+c matches "abc", "abbc", "abbc" and so forth, but not "ac"

new = re.sub('[.,\'A-Za-z+" "]', '', string)  # even remove the spaces
print(new)

string = string + "6 6656 - 4545"

new = re.sub('[^0-9]', '', string) # remove anything except numbers
print(new)

