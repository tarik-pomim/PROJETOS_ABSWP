#  Practice Questions

#  1. What is []?
# R: A list

#  2. How would you assign the value 'hello' as the third value in a list
#  stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
# R: spam = [2, 4, 6, 'hello', 8, 10]

#  For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
#  3. What does spam[int(int('3' * 2) // 11)] evaluate to?
#  R: d

#  4. What does spam[-1] evaluate to?
#  R: d

#  5. What does spam[:2] evaluate to?
#  R: a, b

#  For the following three questions, let’s say
#  bacon contains the list [3.14, 'cat', 11, 'cat', True].
#  6. What does bacon.index('cat') evaluate to?
#  R: 1

#  7. What does bacon.append(99) make the list value in bacon look like?
#  R: [3.14, 'cat', 11, 'cat', True, 99]

#  8. What does bacon.remove('cat') make the list value in bacon look like?
#  R: [3.14, 11, 'cat', True, 99]

#  9. What are the operators for list concatenation and list replication?
#  R: + and *

#  10. What is the difference between the append() and insert() list methods?
#  R: append() method call adds the argument to the end of the list.
#     insert() method can insert a value at any index in the list.
#     The 1st argument to insert() is the index for the new value, and the second argument
#     is the new value to be inserted.

#  11. What are two ways to remove values from a list?
#  R: remove() method is passed the value to be removed from the list. Ie.: spam.remove('cat')
#  R: del is good when you know the index of the value yopu want removed. Ie.: del spam[2]

#  12. Name a few ways that list values are similar to string values.
#  R: Both lists and strings can be passed to len(),
#  have indexes and slices, be used in for loops,
#  be concatenated or replicated, and be used with the in and not in operators.


#  13. What is the difference between lists and tuples?
#  R: tuples, like strings, are immutable

#  14. How do you type the tuple value that has just the integer value 42 in it?
#  R: (42, )

#  15. How can you get the tuple form of a list value?
#  R: tuple(['cat', 'dog', 5])
#  How can you get the list form of a tuple value?
#  R: list(('cat', 'dog', 5))


#  16. Variables that “contain” list values don’t actually contain lists directly.
#  What do they contain instead?
#  R: their reference

#  17. What is the difference between copy.copy() and copy.deepcopy()?
#  StackOverflow:
#  R:  copy.copy() constructs a new compound object and then iserts references into it
#      to the objects found in the original.
#  R:  copy.deepcopy() constructs a new compound object and then inserts copies into it
#      of the objects found in the original.
#
#  Book:
#  R:  copy.copy(), can be used to make a duplicate copy of a mutable value like
#  a list or dictionary, not just a copy of a reference.
#  R: If the list you need to copy contains lists,
#  then use the copy.deepcopy() function instead of copy.copy().
#  The deepcopy() function will copy these inner lists as well.
