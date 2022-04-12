#  Practice Questions
#  1. What are the two values of the Boolean data type? How do you write them?
#       True False


#  2. What are the three Boolean operators?
#        'and' 'or' 'not'


#  3. Write out the truth tables of each Boolean operator (that is, every possible
#  combination of Boolean values for the operator and what they evaluate to).

#           and operator:
#        True and True -> True
#        True and False -> False
#        False and True -> False
#        False and False -> False

#           or operator:
#       True or True  ->  True
#       True or False  -> True
#       False or True  -> True
#       False or False  -> False

#           not operator:
#       not True  ->  False
#       not False ->  True


#  4. What do the following expressions evaluate to?

#  (5 > 4) and (3 == 5)  ->  False
#  not (5 > 4)  ->  False
#  (5 > 4) or (3 == 5)  ->  True
#  not ((5 > 4) or (3 == 5))  ->  False
#  (True and True) and (True == False)  ->  False
#  (not False) or (not True)  ->  True


#  5. What are the six comparison operators?
#  > >= < <= != ==

#  6. What is the difference between the equal to operator and the assignment operator?
# == vs =

#  7. Explain what a condition is and where you would use one.
#  condition is just a more specific name in the context of flow control statements.


#  8. Identify the three blocks in this code: r: vai imprimir spam só

#  spam = 0
#  if spam == 10:
#      print('eggs')
#      if spam > 5:
#          print('bacon')
#      else:
#          print('ham')
#      print('spam')
#  print('spam')


#  9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam,
#  and prints Greetings! if anything else is stored in spam.

#  spam = 2
#  if spam == 1:
#      print('Hello')
#  elif spam == 2:
#      print('Howdy')
#  else:
#      print('Greetings!')


#  10. What keys can you press if your program is stuck in an infinite loop?
#  Ctrl+c

#  11. What is the difference between break and continue?
#  Break statement para e sai do while loop, continue para e reinicia o while loop.


#  12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
#  range(10) e range(0, 10) são a msm coisa, sendo que um deles seta o inicio da contagem em zero,
#  e range(0, 10, 1) vai do zero ao 10 com o passo de 1 por vez.


#  13. Write a short program that prints the numbers 1 to 10 using a for loop.
#  Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

#  for i in range(1, 11):
#      print(i)
# -------------------------
#  x = 0
#  while True:
#      x = x + 1
#      print(x)
#      if x == 10:
#          break

#  14. If you had a function named bacon() inside a module named spam,
#  how would you call it after importing spam?
# from spam import bacon


#  Extra credit: Look up the round() and abs() functions on the internet, and find out what they do.
#  Experiment with them in the interactive shell

