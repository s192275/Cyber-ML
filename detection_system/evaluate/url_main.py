from lightgbm import LGBMClassifier
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import warnings 

warnings.filterwarnings("ignore")

def clean_text(text):
    text = text.lower()
    token = re.split(r'[\/\-._:]', text)
    token.append(text)
    if "www" in token:
        token.remove("www")
    if "com" in token:
        token.remove("com")
    if "https" in token:
        token.remove("https")
    if  "http" in token:
        token.remove("http")
    token = token[:-1]
    return token

urls = []
urls.append(input("Input the URL that you want to check (eg. google.com) : "))

whitelist = ['hackthebox.eu','root-me.org','gmail.com']
s_url = [i for i in urls if i not in whitelist]

file = "detect/url_model.pkl"
with open(file, 'rb') as f1:  
    lgm = pickle.load(f1)
f1.close()

file = "detect/pickel_vector.pkl"
with open(file, 'rb') as f2:  
    vectorizer = pickle.load(f2)
f2.close()

#predicting
x = vectorizer.transform(s_url)
y_predict = lgm.predict(x)

for site in whitelist:
    s_url.append(site)
#print(s_url)

predict = list(y_predict)
for j in range(0,len(whitelist)):
    predict.append('good')
    
if predict[0] == 0 : 
    print("\nThe entered domain is malicious!... ")
    
if predict[0] == 1 : 
    print("\nThe entered domain is not malicious!... ")