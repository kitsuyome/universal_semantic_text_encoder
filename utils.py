import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import urllib.request
import zipfile
import os
import tarfile
import requests
from io import BytesIO
nltk.download('stopwords')

def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z ]', '', text)
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

def clone_senteval_repo():
    os.system('git clone https://github.com/facebookresearch/SentEval.git')

def download_transfer_data():
    os.system('curl -Lo senteval_data.tar https://dl.fbaipublicfiles.com/senteval/senteval_data.tar')
    os.system('tar -xvf senteval_data.tar')

def init_senteval_params():
    params = {
        'task_path': './data',
        'usepytorch': True,
        'kfold': 10,
        'seed': 1111,
        'batch_size': 16, 
        'cudaEfficient': True
    }
    
    tasks = ['SICKRelatedness', 'STSBenchmark']
    
    return params, tasks

def setup_senteval():
    os.system('rm -rf ./SentEval')
    
    os.system('git clone https://github.com/facebookresearch/SentEval.git')
    
    os.chdir('/content/SentEval/data/downstream')
    os.system('bash get_transfer_data.bash')
    os.chdir('/content/SentEval')