# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W4zxP7Y6QM-HySFdRUMEaoF7b0s5Aia7
"""

# №1.1
a = input()
b = a.split()
b[::-1]

# №1.2
a = input().split()
mx = int(a[0])
mn = int(a[0])
for i in a:
  i = int(i)
  if mx < i:
    mx = i
  elif mn > i:
    mn = i
print(mx, mn, end = ' ')

# №1.3
a = input()
b = list(a)
c = len(b)
if c > 6:
  print(b[3], b[5])
else:
  print(a[::-2])

# №1.4
a = input().split()
otr = 0
bol = 0
chet = 0
for i in a:
  i = int(i)
  if i < 0:
    otr += 1
  if i > 8:
    bol += 1
  if i % 2 == 0:
    chet += 1
print(otr, bol, chet, end = ' ')

# №2.1
a = input()
t = 0
f = 0
if "True" in a:
  t =+ 1
elif "False" in a:
  f =+ 1
print(t, f, end = ' ')

# №2.2