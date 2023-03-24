#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_two(n):
    return n == 2 or n == '2'


# In[2]:


def is_vowel(char):
    if type(char) == str: 
        return char.lower() in list('aeiou')
    else:
        return False


# In[3]:


def is_consonsant(string):
    if type(string) == str:
        return not is_vowel(string)
    else:
        return False


# In[4]:


def capital_cons_start(string):
    if is_consonsant(string[0]):
        string= string.capitalize()
    return string


# In[5]:


def calculate_tip(bill_total, tip_perc=.2):
    return bill_total * tip_perc + bill_total


# In[6]:


def apply_discount(og_price, discount_perc):
    return og_price - og_price * discount_perc


# In[7]:


def handle_commas(number):
    number = number.replace(',','')
    number = int(number)
    return number


# In[8]:


def get_letter_grade(grade):
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    else:
        letter_grade = 'F'
    return letter_grade


# In[9]:


def remove_vowels(string):
    new_string = ''

    for char in string:
        if not is_vowel(char):
            new_string += char

    return new_string


# In[10]:


def normalize_name(string):
    new_string =''

    for char in string:
        if char.isdigit() or char.isalpha() or char == ' ':
            new_string += char

    new_string = new_string.strip().lower().replace(' ','_')
    return new_string


# In[11]:


def cumulative_sum(ls_numbs):
    total = 0

    some_sums = []

    for numb in ls_numbs:
        total += numb
        some_sums.append(total)

    return some_sums


# In[ ]:




