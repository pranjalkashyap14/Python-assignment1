#!/usr/bin/env python
# coding: utf-8

# 1 Write a Python Program(with class concepts) to find the area of the triangle using the below 
# formula.
# 
# #  area = (s*(s-a)*(s-b)*(s-c)) ***0.5
# 
# Function to take the length of the sides of triangle from user should be defined in the parent 
# class and function to calculate the area should be defined in subclass

# In[12]:


class area:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.area = 0

class triangle(area):
    def __init__(self, a, b, c):
        poly.__init__(self, a, b, c)

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        self.area = float((s * (s - self.a) * (s - self.b) * (s - self.c))) ** 0.5

    def get_area(self):
        return self.area     

a, b, c = input("a = "), input("b = "), input("c = ")

t = triangle(a, b, c)
t.calculate_area()
print("area : {}".format(t.get_area()))


# # 2.  Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

# In[23]:


def filter_long_words(wordlist, length):
    return (word for word in wordlist if len(word) >= length)

def main():
    words = input("Enter words, separated by spaces: ").split()
    length = int(input("Minimum length of words to keep: "))
    print("Words longer than {} are {}.".format(length,
          ', '.join(filter_long_words(words, length))))

main()


# # 3. Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# In[38]:


listOfWords = input("please enter the words using comma : ").split(",")
listOfInts = []
 
for i in range(len(listOfWords)):
    listOfInts.append(len(listOfWords[i]))
print ("List of wordlength:"+str(listOfInts))


# # 4. Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

# In[53]:


def vowelcheck(inputchar):
    if(inputchar=="a" or inputchar=="A" or
       inputchar=="e" or inputchar=="E" or
       inputchar=="i" or inputchar=="I" or
       inputchar=="o" or inputchar=="O" or
       inputchar=="u" or inputchar=="U"):
        return "True"
    else:
        return "False"
print("Enter a word")
inputchar=input()
if vowelcheck(inputchar)=="True":
    print("This is a vowel")
else:
    print("This is not a vowel")
       

