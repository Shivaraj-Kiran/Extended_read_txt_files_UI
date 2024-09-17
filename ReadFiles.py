import pandas as pd
import streamlit as st

st.title('Welcome to the ETL-TEST-UI-Astra')

# File uploaders for both the CSV and the text file
uploaded_column_def = st.file_uploader("Upload Column Definition CSV", type="csv")
uploaded_text_file = st.file_uploader("Upload Text File", type="txt")

# Proceed only if both files are uploaded
if uploaded_column_def is not None and uploaded_text_file is not None:
    # Reading the column definitions CSV
    column_defination = pd.read_csv(uploaded_column_def)

    # Initializing a list to store extracted column data
    column_data = [[] for _ in range(len(column_defination))]

    # Reading the text file line by line
    lines = uploaded_text_file.read().decode("utf-8").splitlines()

    # Extracting data based on column definitions (index and length)
    for line in lines:
        for i, row in column_defination.iterrows():
            index = row['index']
            length = row['length']
            # Extracting based on index and length, and stripping whitespaces
            column_data[i].append(line[index:index+length].strip())

    # Creating a dictionary to store extracted data
    extracted_data = {f'Column{i+1}': column_data[i] for i in range(len(column_defination))}

    # Converting the dictionary to a DataFrame
    extracted_df = pd.DataFrame(extracted_data, dtype=str)

    # Display the extracted data in the Streamlit app
    st.write("Extracted Data:")
    st.dataframe(extracted_df)

else:
    st.warning("Please upload both the Column Definition_CSV and the Text_File to proceed.")
