import sys
import os
import time
from memory_profiler import profile
import threading

start = time.time()

# # Add parent directory to path to access bci_essentials
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))

# from src.bci_data import *
from bci_essentials.bci_data import *
from bci_essentials.visuals import *

fp = open('Algo_memory_runX.log','w+')

@profile(stream=fp)
def main():
    # Initialize data object
    test_switch = EEG_data()

    # Select a classifier
    test_switch.classifier = switch_classifier()
    test_switch.classifier.set_switch_classifier_settings(n_splits=2, rebuild=True, random_seed=35)

    # Select a file to run, use a file that you have locally 
    test_switch.load_offline_eeg_data(filename  = "examples/data/switch_example.xdf") 

    # Run it
    test_switch.main(online=False, training=True)

    print(f"Time consumed: {time.time() - start}")

if __name__ == "__main__":
    main()

'''
Results for switch example:
1. Neural Network = 86.67, 100%
2. Pyriemannan = 61.12, 76.47%
3. Linear discriminant Analysis = 73.33, 58.82%
'''