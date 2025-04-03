#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""data.py: Splits data into malignant or benign classes."""

__author__ = "Hudson Liu"
__email__ = "hudsonliu0@gmail.com"

import os
import shutil
import sys
import signal

import numpy as np
import pandas as pd
from termcolor import colored
from tqdm import tqdm

def tui_helper():
    """Silly stuff for making the TUi look pretty"""
    # Clean exit
    def signal_handler(*_):
        """Handles ctrl c input"""
        print(colored("\n\nExiting data processor :D ", "yellow"))
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
    HEADER = HEADER = (colored("======[", attrs=["bold"]) +
    	colored("An Unnecessarily-Fancy Data Processor", "blue", attrs=["bold"]) +
    	colored("]=======", attrs=["bold"]))
    print(BANNER + HEADER)

def data_proc(loc: str):
    """Data processing shenanigans"""
    d = loc + "train/"
    df = pd.read_csv(f"{loc}ISIC_2020_Training_GroundTruth.csv")
    labels = df[["image_name", "sex", "benign_malignant"]].to_numpy()
    
    NUM_IMGS = 600
    totals = [0] * 4
    classes = [
        ["male", "benign"],
        ["male", "malignant"],
        ["female", "benign"],
        ["female", "malignant"]
    ]
    ben = []
    mal = []
    for c in classes:
        f = 0
        while f < NUM_IMGS // 4:
            for e, l in enumerate(labels):
                if l[1] == c[0] and l[2] == c[1]:
                    if c[1] == "malignant":
                        mal.append(l[0])
                    if c[1] == "benign":
                        ben.append(l[0])
                    labels = np.delete(labels, e, axis=0)
                    f += 1
                    break
    for f in tqdm(mal, desc="Malignant imgs"):
        shutil.copyfile(f"{d}{f}.jpg", f"{loc}mal/{f}.jpg")

    for f in tqdm(ben, desc="Benign imgs"):
       shutil.copyfile(f"{d}{f}.jpg", f"{loc}ben/{f}.jpg")

     
# Run script
if __name__ == "__main__":
    tui_helper()
    d = input("Enter location of dataset (leave blank if cwd): ")
    loc = f"{d if d else "."}/ISIC_2020_Training_JPEG/"
    data_proc(loc)
