import numpy as np
import pandas as pd
import os
from os import path

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = open(path.join(d, 'sen.txt')).read()
wordcloud = WordCloud().generate(text)