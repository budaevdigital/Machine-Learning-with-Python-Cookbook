
# coding: utf-8

# # Глава 1. 
# ## Векторы, матрицы, массивы
# > <b>1.1 Создание вектора

# In[8]:


# Загрузить библиотеку
import numpy as np

# Создать вектор как строку
vector_row = np.array([1, 2, 3])

# Создать вектор как столбец
vector_column = np.array([[1],
                          [2],
                          [3]])


# In[9]:


vector_row


# In[10]:


vector_column


# > <b>1.2 Создание матрицы

# In[5]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 2],
                   [1, 2],
                   [1, 2]]) 

matrix


# In[6]:


matrix_object = np.mat([[1, 2],
                        [1, 2],
                        [1, 2]])
matrix_object 


# > <b>1.3 Создание разряженной матрицы

# In[11]:


# Загрузить библиотеки
import numpy as np
from scipy import sparse

# Создать матрицу
matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])

# Создать сжатую разреженную матрицу-строку (CSR-матрицу)
matrix_sparse = sparse.csr_matrix(matrix)


# In[12]:


matrix


# In[13]:


matrix_sparse


# In[14]:


# Взглянуть на разряженную матрицу
print(matrix_sparse)


# In[15]:


# Создать более крупную матрицу
matrix_large = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Создать сжатую разреженную матрицу-строку (CSR-матрицу)
matrix_large_sparse = sparse.csr_matrix(matrix_large)

# Взглянуть на исходную разряженную матрицу
print(matrix_sparse)


# In[16]:


# Взглянуть на более крупную разряженную матрицу 
print(matrix_large_sparse)


# > <b>1.4 Выбор элементов

# In[17]:


# Загрузить библиотеку
import numpy as np

# Создать вектор-строку
vector = np.array([1, 2, 3, 4, 5, 6])

# Создать матрицу
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


# In[18]:


# Выбрать третий элемент вектора
vector[2]


# In[19]:


# Выбрать вторую строку, второй столбец
matrix[1,1]


# In[20]:


# Выбрать все элементы вектора
vector[:]


# In[21]:


# Выбрать все вплоть до и включая третий элемент
vector[:3]


# In[23]:


# Выбрать все после третьего элемента
vector[3:]


# In[24]:


# Выбрать последний элемент
vector[-1]


# In[25]:


# Выбрать первые две строки и все столбцы матрицы
matrix[:2,:]


# In[26]:


# Выбрать все строки и второй столбец
matrix[:,1:2]


# > <b>1.5 Описание матрицы

# In[27]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])


# In[28]:


# Взглянуть на количество строк и столбцов
matrix.shape


# In[29]:


# Взглянуть на количество элементов (строки * столбцы)
matrix.size


# In[30]:


# Взглянуть на количество размерностей
matrix.ndim


# > <b>1.6 Применение операций к элементам

# In[33]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Создать функцию, которая добавляет к чему-то 100 
add_100 = lambda i: i + 100

# Создать векторизованную функцию
vectorized_add_100 = np.vectorize(add_100)

# Применить функцию ко всем элементам в матрице
vectorized_add_100(matrix)


# In[32]:


# Добавить 100 ко всем элементам
matrix + 100


# > <b>1.7 Нахождение максимального и минимального значений

# In[34]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


# In[35]:


# Вернуть максимальный элемент
np.max(matrix)


# In[36]:


# Вернуть минимальный элемент
np.min(matrix)


# In[37]:


# Найти максимальный элемент в каждом столбце
np.max(matrix, axis=0)


# In[38]:


# Найти максимальный элемент в каждой строке
np.max(matrix, axis=1)


# > <b>1.8 Вычисление среднего значения, дисперсии и стандартного отклонения

# In[40]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


# In[41]:


# Вернуть среднее значение
np.mean(matrix)


# In[42]:


# Вернуть дисперсию
np.var(matrix)


# In[43]:


# Вернуть стандартное отклонение
np.std(matrix)


# In[44]:


# Найти среднее значение в каждом столбце
np.mean(matrix, axis=0)


# > <b>1.9 Реформирование массивов

# In[48]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу 4x3
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])
matrix


# In[47]:


# Реформировать матрицу в матрицу 2x6
matrix.reshape(2, 6)


# In[49]:


matrix.size


# In[50]:


matrix.reshape(1, -1)


# In[51]:


matrix.reshape(12)


# > <b>1.10 Транспонирование вектора в матрицу

# In[52]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Транспонировать матрицу
matrix.T


# In[53]:


# Транспонировать вектор
np.array([1, 2, 3, 4, 5, 6]).T


# In[54]:


# Транспонировать вектор-строку
np.array([[1, 2, 3, 4, 5, 6]]).T


# > <b>1.11 Сглаживание матрицы

# In[55]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Сгладить матрицу
matrix.flatten()


# In[56]:


matrix.reshape(1, -1)


# > <b>1.12 Нахождение ранга матрицы

# In[1]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 1, 1],
                   [1, 1, 10],
                   [1, 1, 15]])

# Вернуть ранг матрицы
np.linalg.matrix_rank(matrix)


# > <b>1.13 Вычисление определителя матрицы

# In[2]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 2, 3],
                   [2, 4, 6],
                   [3, 8, 9]])

# Вернуть определитель матрицы
np.linalg.det(matrix)


# > <b>1.14 Получение диагонали матрицы

# In[3]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 2, 3],
                   [2, 4, 6],
                   [3, 8, 9]])

# Вернуть диагональные элементы
matrix.diagonal()


# In[4]:


# Вернуть диагональ на одну выше главной диагонали
matrix.diagonal(offset=1)


# In[5]:


# Вернуть диагональ на одну ниже главной диагонали
matrix.diagonal(offset=-1)


# > <b>1.15 Вычисление следа матрицы

# In[6]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 2, 3],
                   [2, 4, 6],
                   [3, 8, 9]])

# Вырнуть след
matrix.trace()


# In[7]:


# Вернуть диагональ и сумму элементов
sum(matrix.diagonal())


# > <b>1.16 Нахождение собственных значений и собственных векторов

# In[8]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, -1, 3],
                   [1,  1, 6],
                   [3,  8, 9]])

# Вычислить собственные значения и собственные векторы
eigenvalues, eigenvectors = np.linalg.eig(matrix)


# In[9]:


# Взглянуть на собственные значения
eigenvalues


# In[10]:


# Взглянуть на собственные векторы
eigenvectors


# > <b>1.17 Вычисление скалярных произведений

# In[11]:


# Загрузить библиотеку
import numpy as np

# Создать два вектора
vector_a = np.array([1,2,3])
vector_b = np.array([4,5,6])

# Вычислить скалярное произведение
np.dot(vector_a, vector_b)


# In[12]:


# Вычислить скалярное произведение
vector_a @ vector_b


# > <b>1.18 Сложение и вычитание матриц

# In[13]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix_a = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 2]])

# Создать матрицу
matrix_b = np.array([[1, 3, 1],
                     [1, 3, 1],
                     [1, 3, 8]])


# In[14]:


# Сложить две матрицы
np.add(matrix_a, matrix_b)


# In[15]:


# Вычесть из одной матрицы другую
np.subtract(matrix_a, matrix_b)


# In[16]:


# Сложить две матрицы
matrix_a + matrix_b


# > <b>1.19 Умножение матриц

# In[17]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix_a = np.array([[1, 1],
                     [1, 2]])

# Создать матрицу
matrix_b = np.array([[1, 3],
                     [1, 2]])

# Умножить две матрицы
np.dot(matrix_a, matrix_b)


# In[18]:


# Умножить две матрицы
matrix_a @ matrix_b


# In[19]:


# Умножить две матрицы поэлементно
matrix_a * matrix_b


# > <b>1.20 Обращение матрицы

# In[20]:


# Загрузить библиотеку
import numpy as np

# Создать матрицу
matrix = np.array([[1, 4],
                   [2, 5]])

# Вычислить обратную матрицу
np.linalg.inv(matrix)


# In[21]:


# Умножить матрицу на обратную ей матрицу
matrix @ np.linalg.inv(matrix)


# > <b>1.21 Генерирование случайных значений

# In[22]:


# Загрузить библиотеку
import numpy as np

# Задать начальное значение для генератора псевдослучайных чисел
np.random.seed(0)

# Сгенерировать три случайных вещественных числа между 0.0 и 1.0
np.random.random(3)


# In[23]:


# Сгенерировать три случайныз целых числа между 1 и 10
np.random.randint(0, 11, 3)


# In[24]:


# Извлечь три числа из нормального распределения со средним, равным 0.0
# и стандартным отклонением, равным 1.0
np.random.normal(0.0, 1.0, 3)


# In[25]:


# Извлечь три числа из логистического распределения со средним, равным 0.0 и
# масштабом, равным 1.0
np.random.logistic(0.0, 1.0, 3)


# In[26]:


# Извлечь три числа, которые больше или равны 1.0 и меньше 2.0
np.random.uniform(1.0, 2.0, 3)

