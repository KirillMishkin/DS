#!/usr/bin/env python
# coding: utf-8

# ### Import

# In[4]:


import pandas as pd


# ### Задание 1

# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# 
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные: 
# 
# [1, 1, 1, 2, 2, 3, 3], 
# 
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# 
# [450, 300, 350, 500, 450, 370, 290].
# 

# In[6]:


authors = pd.DataFrame({'author_id':[1,2,3],
                        'author_name':['Тургенев', 'Чехов', 'Островский']})
authors


# In[7]:


book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                    'book_title':['Отцы и дети', 
                                  'Рудин', 
                                  'Дворянское гнездо', 
                                  'Толстый и тонкий', 
                                  'Дама с собачкой', 
                                  'Гроза', 
                                  'Таланты и поклонники'],
                    'price':[450, 300, 350, 500, 450, 370, 290]})
book


# In[14]:


authors.dtypes


# In[17]:


book.dtypes


# ### Задание 2

# Задание 2
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.
# 

# In[20]:


authors_price = authors.merge(book, how = 'outer')
authors_price


# ### Задание 3

# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

# In[72]:


top5 = authors_price.sort_values(by=['price'], ascending=False).head(5).reset_index()


# In[73]:


top5


# ### Задание 4

# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора,минимальная, максимальная и средняя цена на книги этого автора.
# 

# In[198]:


authors_stats = pd.DataFrame({'author_name':[],
                             'min_price':[],
                             'mean_price':[],
                             'max_price':[]})


# In[199]:


# Вариант 1. Прямо в лоб. 
authors_stats['author_name'] = authors_price['author_name']
authors_stats['min_price'] = authors_price['price']
authors_stats['max_price'] = authors_price['price']
authors_stats['mean_price'] = authors_price['price']
authors_stats.groupby('author_name').agg({'min_price':'min',
                                         'mean_price':'mean',
                                         'max_price':max})


# In[202]:


# Вариант 2
authors_stats = pd.DataFrame(authors_price).groupby('author_name')['price'].agg(['min','mean',max])


# In[194]:


authors_stats


# ### Задание 5

# Создайте новый столбец в датафрейме authors_price под названием cover, в нем будут располагаться данные о том, какая обложка у данной книги - твердая или мягкая. В этот столбец поместите данные из следующего списка:
# ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'].
# 
# Просмотрите документацию по функции pd.pivot_table с помощью вопросительного знака.Для каждого автора посчитайте суммарную стоимость книг в твердой и мягкой обложке. Используйте для этого функцию pd.pivot_table. При этом столбцы должны называться "твердая" и "мягкая", а индексами должны быть фамилии авторов. Пропущенные значения стоимостей заполните нулями, при необходимости загрузите библиотеку Numpy.
# 
# Назовите полученный датасет book_info и сохраните его в формат pickle под названием "book_info.pkl". Затем загрузите из этого файла датафрейм и назовите его book_info2. Удостоверьтесь, что датафреймы book_info и book_info2 идентичны.
# 

# In[200]:


authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
authors_price


# In[207]:


authors_price.pivot_table('price', index='author_name',columns = 'cover',aggfunc = 'sum').fillna(0)


# In[ ]:




