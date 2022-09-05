import re  # For preprocessing
import pandas as pd  # For data handling
from time import time  # To time our operations
from collections import defaultdict  # For word frequency

import spacy  # For preprocessing

import logging  # Setting up the loggings to monitor gensim
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)
df = pd.read_csv('../input/simpsons_dataset.csv')
df.shape
df.head()
df = df.dropna().reset_index(drop=True)
df.isnull().sum()