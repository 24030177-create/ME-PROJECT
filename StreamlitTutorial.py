# import packages
import streamlit as st # frontend userinterface design
import numpy as np # it is used for scientific calculation
# import pandas as pd #it is used for data analysys

st.title("Hello, streamlit")
st.write("streamlit: This is your first streamlit app")
st.text("Lets go started")
st.write("My name is Trupti khobragade")

# conditional logic 
name = st.text_input("Enter Your Name :")
if st.button("Greet"):
    st.success(f"Hello {name}")

# #Displaying data and charts
# df= pd.DataFrame(np.random.randn(10,2), columns=["A","B"])
# st.bar_chart(df)


#File iuploading and catching 
upload_file = st.file_uploader("Upload File", type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

    # all the userinterface of streamlit 
st.header("this is a header")
st.subheader("This is a Subheader")
st.markdown("**Bold**, *Italic*, [Link](https://help4code.com/)")
st.text_area("Write your messege")
st.number_input("pick a number", min_value=0, max_value=100)
st.slider("choose a range",0, 100)
st.selectbox("Select a fruit",["Apple","Banana", "Mango"])
st.multiselect("choose toppings",["cheese", "Tomato", "Olives"])
st.radio("Pick one",["Option A", "Option B"])
st.checkbox("I agree terms and condition")

# form code 
with st.form("Login Form"):
    username = st.text_input("username")
    password = st.text_input("password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        st.success(f"welcome, {username}")
#
#check radio button 
option = st.radio("Choose View", ["Show chart", "Show Table"])
if option == "Show chart":
    st.write("Table would be appear heare")
else:
    st.write("Table would be appear heare")

if st.checkbox("Show details"):
    st.info("Here are more details")

#Media layout and advance 
st.sidebar.title("New Chat")
st.image("https://static.wikia.nocookie.net/marvelcinematicuniverse/images/9/9d/Iron_Man_Infobox.jpg/revision/latest?cb=20240802142023")
st.video("https://youtube.com/shorts/U6T5oJ6Twrs?si=w3hrz4LKAhElkOOb")