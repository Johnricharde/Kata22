def strip_comments(strng, markers):
    result = ""

    strng_array = strng.split("\n")

    for string in strng_array:
        for mark in markers:
            if mark in string:
                string = string.split(mark)[0]
        result += string.rstrip() + "\n"

    return result.rstrip()


# Complete the solution so that it strips all text that follows any of
# a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
# The code would be called like so:

# result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"