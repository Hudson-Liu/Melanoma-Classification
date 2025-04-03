#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""data.py: Splits data into malignant or benign classes."""

__author__ = "Hudson Liu"
__email__ = "hudsonliu0@gmail.com"

import os
import sys
import signal

from termcolor import colored

# Clean exit
EXIT_PRMPT = colored("\n\nExiting data processor... ", "yellow")
def signal_handler(*_):
    """Handles ctrl c input"""
    print(EXIT_PRMPT)
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)

# Banner
BANNER = colored("""
███████╗██╗██╗███╗   ███╗      ██╗███████╗██╗ ██████╗
██╔════╝██║██║████╗ ████║      ██║██╔════╝██║██╔════╝
███████╗██║██║██╔████╔██║█████╗██║███████╗██║██║     
╚════██║██║██║██║╚██╔╝██║╚════╝██║╚════██║██║██║     
███████║██║██║██║ ╚═╝ ██║      ██║███████║██║╚██████╗
╚══════╝╚═╝╚═╝╚═╝     ╚═╝      ╚═╝╚══════╝╚═╝ ╚═════╝
""", "blue")
HEADER = HEADER = (colored("====[", attrs=["bold"]) +
	colored("An Unnecessarily-Fancy Data Processor", "blue", attrs=["bold"]) +
	colored("]=====", attrs=["bold"]))
print(BANNER + HEADER)

dir_ = input("Enter location of dataset (leave blank if cwd): ")
if dir_:
    os.chdir(dir_)

