import streamlit as st
import pandas as pd
st.title("trial publish app dashboard")
st.subheader("enjoy the first app")
st.write("""this is my first steamlit apps
         hahahah!!
         really love it!!
         """)
st.write("adding pandas dataframe")
data = pd.DataFrame({'series 1': [1,2,3,4], 
                     'series 2': [10,30,40,20]})
st.write(data)
st.write(data)