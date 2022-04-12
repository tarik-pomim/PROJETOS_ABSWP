"""
Practice Questions
1. What are escape characters?
r.:  An escape character lets you use characters that are otherwise impossible to
put into a string.

2. What do the \n and \t escape characters represent?
r.:  \n newline  ;  \t Tab

3. How can you put a \ backslash character in a string?
r.:  \\

4. The string value "Howl's Moving Castle" is a valid string.
Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
r.: Because of using double quotes "" instead of single quotes''

5. If you don’t want to put \n in your string,
how can you write a string with newlines in it?
r.:  Using triple quotes '''x''', single or triple

6. What do the following expressions evaluate to?

'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]

r.:
e
Hello
Hello
lo, world!


7. What do the following expressions evaluate to?

'Hello'.upper()
'Hello'.upper().isupper()  # At least ONE letter is uppercase
'Hello'.upper().lower()

r.:
HELLO
false
hello

isalpha()  # letters
isalnum()  # letters and numbers
isdecimal()  # numeric characters
isspace()  # spaces, tabs, and newlines
istitle()  # words that begin with an uppercase letter followed by only lowercase letters


8. What do the following expressions evaluate to?

'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())

r.:
['remember,', 'remember,', 'the', 'fifth', 'of', 'november.']
'There-can-be-only-one.'


9. What string methods can you use to right-justify, left-justify, and center a string?
r.:  rjust(), ljust(), center()

10. How can you trim whitespace characters from the beginning or end of a string?
r.:  lstrip()

spam.strip()  # remove todos whites
spam.lstrip()  # remove whites da esq
spam.rstrip()  # remove whites da dir

pode-se passar uma tring como argumento pra especificar
qual char no final deve ser removido.


"""