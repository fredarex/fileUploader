import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
#image 
from PIL import Image

@st.cache


# Create a list to store uploaded files


def image_load(img_file):
    img = Image.open(img_file)
    return img

# Function to sort files based on user's choice
def sort_files(files, sort_option):
    if sort_option == "File Name":
        return sorted(files, key=lambda x: x.name)
    elif sort_option == "File Type":
        return sorted(files, key=lambda x: x.type)
    elif sort_option == "File Size":
        return sorted(files, key=lambda x: x.size)
    else:
        return files

# Function to filter files based on user's choice
def filter_files(files, filter_option, filter_value):
    if filter_option == "File Name":
        return [file for file in files if filter_value.lower() in file.name.lower()]
    elif filter_option == "File Type":
        return [file for file in files if filter_value.lower() in file.type.lower()]
    else:
        return files

def main(): 
    st.title("File Uploader")
    menu  = ["File Uploader"]

    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "File Uploader":
        # Sort options
        sort_option = st.selectbox("Sort by", ["File Name", "File Type", "File Size"])

        # Filter options
        filter_option = st.selectbox("Filter by", ["None", "File Name", "File Type"])
        if filter_option != "None":
            filter_value = st.text_input(f"Enter {filter_option}", "")

        datafile = st.file_uploader("Upload your file here", type=None,accept_multiple_files=True)
        if datafile is not None:
            my_details = {"file size": datafile.size, "file Type": datafile.type, "Last Modified": "23"}
            if datafile.type.startswith('image'):
                st.write("Uploaded file is an image.")
                st.write(my_details)
                # Process the image
                newimg = image_load(datafile)
                st.image(newimg,height=250,width=250) 
        
                # Check if the uploaded file is a text file
            elif datafile.type.startswith('text'):
                st.write("Uploaded file is a text file.")
                # Process the text file
                st.write(my_details)
                text = datafile.read().decode("utf-8")  # Read and decode text
                st.write(text)
        
            # Check if the uploaded file is a CSV file
            elif datafile.type == 'text/csv':
                st.write("Uploaded file is a CSV file.")
                # Process the CSV file
                st.write(my_details)
                df = pd.read_csv(datafile)
                st.write(df)

        sorted_files = sort_files(datafile, sort_option)
        # Filter the sorted files
    if filter_option != "None":
        filtered_files = filter_files(sorted_files, filter_option, filter_value)
    else:
        filtered_files = sorted_files

    # Create a DataFrame to display file details
    file_details = pd.DataFrame(columns=['File Name', 'File Type', 'File Size'])

    # Populate the DataFrame with details of uploaded files
    for file in filtered_files:
        file_details = file_details.append({
            'File Name': file.name,
            'File Type': file.type,
            'File Size': f"{file.size} bytes"
        }, ignore_index=True)

    # Display the sorted/filtered list of uploaded files in a table
    st.write("Uploaded Files:")
    st.write(file_details)

    