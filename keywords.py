from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd


class Keywords:     
    def vectorizer(self,text):
        tfidf=TfidfVectorizer(ngram_range=(1,4))
        vect=tfidf.fit_transform([text])
        keywords=[]
        keywords=tfidf.get_feature_names()
        return keywords
    
    def keyword(self,keywords,column_name):
        df=pd.read_csv('Domain_keyword.csv',encoding = 'unicode_escape')
        df=df.fillna(method='ffill')
        try:
            domains=df[column_name].tolist()
        except KeyError:
            column_name=column_name.title()
            domains=df[column_name].tolist()
        domains=[i.lower() for i in domains]
        rs=[x for ele in keywords for x in domains if x in ele]
        return np.unique(rs)
