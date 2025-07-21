import streamlit as st
import pandas as pd
import seaborn as sns
table = pd.DataFrame({"column1":[1,2,4,6,6,2],
"column2":[1,4,7,8,5,6]
})

st.title("hi this is streamlit web app")
st.header("temp")
st.subheader("hii im your subtitle")
st.text("hello")    
st.markdown("---")
st.markdown(" # hello ")
st.markdown("[Mayank](https://www/msaharkar.tech)")
st.caption("hellooooo")

st.latex(r"\begin{pmatrix}a&b\\c&d\\e&f\end{pmatrix}")
json = {"a" : [1,2,4,5,6] , "b" :[4,5,7,8,5]}
st.json(json)
c = """
    print("Hello")
    def fun(a):
        return a
    
    fun(a)
    """
st.code(c , language = "python")

st.metric(label="wind speed" , value="120ms−1" ,delta="1.4ms-1" )
st.metric(label="wind speed" , value="120ms−1" ,delta="-1.4ms-1" )

st.table(table)
st.dataframe(table)

