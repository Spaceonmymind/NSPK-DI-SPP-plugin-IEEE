import datetime

from selenium import webdriver
from logging import config
import pickle
import pandas

from src.spp.types import SPP_document

def to_dict(doc: SPP_document) -> dict:
    return {
        'title': doc.title,
        'abstract': doc.abstract,
        'text': doc.text,
        'web_link': doc.web_link,
        'local_link': doc.local_link,
        'other_data': '',
        'pub_date': str(doc.pub_date.timestamp()) if doc.pub_date else '',
        'load_date': str(doc.load_date.timestamp()) if doc.load_date else '',
    }


try:
    with open('backup/documents.backup.pkl', 'rb') as file:
        docs = pickle.load(file)
        dataframe = pandas.DataFrame.from_records([to_dict(d) for d in docs])
        dataframe.to_csv('out/documents.csv')

except Exception as e:
    print(e)
