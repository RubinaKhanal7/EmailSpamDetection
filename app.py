import streamlit as st
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer

st.title('Email Spam Detection')
st.image('https://imgs.search.brave.com/dU74FUiphT7piVBZtCko3v_l01gMoUG2hOycJwoZD8U/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/Z29jdXN0b21lci5h/aS9fbmV4dC9pbWFn/ZT91cmw9aHR0cHM6/Ly9pbWFnZXMuY3Rm/YXNzZXRzLm5ldC8y/YXplM3lzcnYyZDEv/NFlXYTNYZ0ZsVjJq/T2FhQzhWSlNHRS8w/MjZlY2NmMmZhM2Iw/ZWU0Nzk4YTUwODAw/Mzc5MWYzYS9Db3Zl/ci5wbmcmdz0zODQw/JnE9NzU')

with open('spam_detection.pickle', 'rb') as f:
    model = pk.load(f)

with open('tfidf_vectorizer.pickle', 'rb') as f:
    tfidf = pk.load(f)

text = st.text_area("Paste email content here:")

if st.button("Predict"):
    X_transformed = tfidf.transform([text])
    result = model.predict(X_transformed)
    
    if int(result[0]) == 1:
        st.error("SPAM DETECTED!")
    else:
        st.success("This email is legitimate")

