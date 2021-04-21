from tensorflow.keras.models import load_model
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pickle
import os
script_dir = os.path.dirname(__file__)
class dudoan_Rate :
    
    def __init__(self,comment):
        self.comment = comment
        self.model = load_model (os.path.join(script_dir,"AI_doan.h5"))
        self.vectorizer  = TfidfVectorizer(vocabulary = pickle.load(open(os.path.join(script_dir,"vocabulary_3.pkl"), 'rb')), ngram_range=(1,3), min_df=5, max_df= 0.8, max_features=15000, sublinear_tf=True)
        self.xulycomment()
  
    def xulycomment (self):
        self.comment=np.array([self.comment])
   
       
    def return_rate(self):
        id_to_category={0: 5, 1: 1, 2: 4, 3: 2, 4: 3}
        convert = self.vectorizer.fit_transform(self.comment).toarray()
        
        predict_convert =self.model.predict(convert)
        predict_convert_label = predict_convert.argmax(-1)
        return id_to_category[predict_convert_label[0]]


comment="xinh"
d1 = dudoan_Rate(comment)
rate=d1.return_rate()
print(rate)









