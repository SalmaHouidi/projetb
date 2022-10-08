import pandas as pd
import numpy as np


df = pd.read_csv('./Data/survey_results_public.csv')
schema = pd.read_csv('./Data/survey_results_schema.csv')


PATH='./Data/survey_results_public.csv'
PATHSC='./Data/survey_results_schema.csv'
## a look at the Data 
num_rows = df.shape[0]
num_cols = df.shape[1]