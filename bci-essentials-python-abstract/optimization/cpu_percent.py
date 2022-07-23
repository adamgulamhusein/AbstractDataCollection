from datetime import timedelta
from sys import argv
from time import time

import psutil as psu

def cpu_percent_print():
    print(f"{psu.cpu_percent(interval=10, percpu=False)}% CPU used")