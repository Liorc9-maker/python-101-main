# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "
we = word[1] + word[2] + word[-1]
see = word[-2] + word[2] + word[3] + word[-1]
trees = word[0] + word[-3] + word[2] + word[3] + word[-2]
print(we,see,trees)