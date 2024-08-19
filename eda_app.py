import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport

st.markdown('''
# **The EDA App**
This is the **EDA APP** created in Streamlit using the **pandas-profiling** library
''')

with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV data")
    st.sidebar.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")

if uploaded_file is not None:
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv

    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    pr.to_file("report.html")  # Save report to HTML file

    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    # Read and display HTML
    with open("report.html", "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a 

        df = load_data()
        pr = ProfileReport(df, explorative=True)
        pr.to_file("report.html")  # Save report to HTML file

        st.header('**Input DataFrame**')
        st.write('---')
        st.header('**Pandas Profiling Report**')
        # Read and display HTML
        with open("report.html", "r") as f:
            st.markdown(f.read(), unsafe_allow_html=True)
