#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the time_delta function below.

#################################################
from datetime import datetime as dt
fmt = '%a %d %b %Y %H:%M:%S %z'
def time_delta(t1, t2):
    return str(int(abs((dt.strptime(t1, fmt) - dt.strptime(t2, fmt)).total_seconds())))
#################################################                   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
    
    # Caner Dabakoglu
    # GitHub: https://github.com/cdabakoglu
