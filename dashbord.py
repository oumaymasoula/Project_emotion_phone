import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import numpy as np
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage, AnnotationBbox)
from matplotlib.cbook import get_sample_data
from wordcloud import WordCloud,STOPWORDS
from sklearn.feature_extraction.text import CountVectorizer
from pandas import DataFrame
from PIL import Image
from plotly import tools
from plotly.offline import init_notebook_mode,iplot,plot
#from nrclex import NRCLex
from nltk.corpus import stopwords
from colorama import Fore, Back, Style
from io import BytesIO
import base64