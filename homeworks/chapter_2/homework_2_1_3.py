# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_VLbNgSIBM8IfR04vGtNcSZAVFLap5eO
"""

def debug_control(*elements):
    element = 0
    for i in elements:
        element += 1
    return element
debug_control("Hello!", 1000, 7)