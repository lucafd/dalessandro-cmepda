#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# Download a book (not covered by copyright) in plain-text format, e.g., from
# https://www.gutenberg.org/
# 
# --- Goal
# Write a Python program that prints the relative frequence of each letter
# of the alphabet (without distinguishing between lower and upper case) in the
# book.
# 
# --- Specifications
# -[] the program should have a --help option summarizing the usage
# -[] the program should accept the path to the input file from the command line
# -[] the program should print out the total elapsed time
# -[] the program should have an option to display a histogram of the frequences
# -[] [optional] the program should have an option to skip the parts of the text
#   that do not pertain to the book (e.g., preamble and license)
# -[] [optional] the program should have an option to print out the basic book
#   stats (e.g., number of characters, number of words, number of lines, etc.)
""" First assignment for the CMEPDA course, 2022-10-18 started writing
"""
import argparse
import time
import os
import re
import sys

if __name__ == '__main__':
    # write sth