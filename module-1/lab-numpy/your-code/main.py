import numpy as np
print(np.version.version)
a=np.random.random((2,3,5))
a
b=np.ones((5,2,3))
b
b1=b.reshape(2,3,5)
b1
print(a.shape,b1.shape)
c=np.add(a,b1)
c
#se pueden sumar ya que tienen las mismas filas y columnas
c2=c.T
c2.shape
d=c
d.shape
suma=np.add(a+d)
#no tienen las mismas filas y columnas
print(a.shape,d.shape) #Uno tiene 2 capas y el otro5, el primero tiene 3 filas y 5 columna , mientras el otro 3 filas y dos columnas
e= np.multiply(a,c)
e
#En estructura es lo mismo ya que se multiplico elemento por elemento sin alterar la estructura
print(d)
d_max=np.max(d)
d_min=np.min(d)
d_mean=np.mean(d)
print(d.shape)
print(d_max,d_min,d_mean)
f=np.zeros(shape=(2,3,5))

len(f)

f = np.empty((2,3,5))
for i in range(len(f)):
   for j in range(len(f[i])):
       for k in range(len(f[i][j])):
           if (d[i][j][k] > d_min) and (d[i][j][k] < d_mean):
               f[i][j][k] = 75
           elif (d[i][j][k] > d_mean) and (d[i][j][k] < d_max):
               f[i][j][k] = 25
           elif d[i][j][k] == d_mean:
               f[i][j][k] = 50
           elif d[i][j][k] == d_min:
               f[i][j][k] = 0
           elif d[i][j][k] == d_max:
               f[i][j][k] = 100
print(f)

g = np.empty((2,3,5),str)
for i in range(len(g)):
   for j in range(len(g[i])):
       for k in range(len(g[i][j])):
           if (d[i][j][k] > d_min) and (d[i][j][k] < d_mean):
               g[i][j][k] = 'B'
           elif (d[i][j][k] > d_mean) and (d[i][j][k] < d_max):
               g[i][j][k] = 'D'
           elif d[i][j][k] == d_mean:
               g[i][j][k] = 'C'
           elif d[i][j][k] == d_min:
               g[i][j][k] = 'A'
           elif d[i][j][k] == d_max:
               g[i][j][k] = 'E'
print(g)
