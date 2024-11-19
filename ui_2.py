import streamlit as st 
st.set_page_config(page_title='My first project')

# # # form 
# with st.form(key='myform'):
#     st.write("Registration Form")
#     # col1,col2,col3= st.columns([1,2,1])
#     col1,col2= st.columns(2)
#     with col1:
#         name= st.text_input("First Name")
#         email= st.text_input("Email")
        
#     with col2:
#         name2= st.text_input("Last Name")
#         password= st.text_input("Password", type='password')
        
#     # with col3:
#     #     name3= st.text_input("Confirm Password", type='password')
    
#     address= st.text_area("Address")
    
# #     # col1,col2,col3= st.columns([1,3,1])
#     col1,col2= st.columns([1,2])
    
#     with col1:
#         dob= st.date_input("Date of Birth")
#         cond= st.checkbox("Agree Terms and conditions")
#         st.selectbox("State",options=['Punjab','HP','UK','UP','MP'])
#     with col2:
#         gender=st.radio("Gender", options=['Male','Female','Others'], horizontal=True)
#         st.text_input("Pincode")
#         st.multiselect("Interest",options=['Movies','Cricket','Web Series','Games','Reading Books'])
#     st.slider("Age",min_value=5,max_value=70)
#     st.time_input("Time")
#     btn= st.form_submit_button("Submit", type='secondary')
    
# if btn:
#     if name=="" or email=="" or password=="" or address=="" or dob=="" or gender=="":
#         st.warning("Please fill all the fields")
#         st.success("Please fill all the fields")
#         st.error("Please fill all the fields")

###with side bar

with st.sidebar:
   a= st.selectbox("Menu",options=['Home','About','Contact'])

if a=='Home':
   # # form 
    with st.form(key='formStudent'):
        st.write("Registration Form")
        # col1,col2,col3= st.columns([1,2,1])
        col1,col2= st.columns(2)
        with col1:
            name= st.text_input("First Name")
            email= st.text_input("Email")
            
        with col2:
            name2= st.text_input("Last Name")
            password= st.text_input("Password", type='password')
            
        # with col3:
        #     name3= st.text_input("Confirm Password", type='password')
        
        address= st.text_area("Address")
        
    #     # col1,col2,col3= st.columns([1,3,1])
        col1,col2= st.columns([1,2])
        
        with col1:
            dob= st.date_input("Date of Birth")
            cond= st.checkbox("Agree Terms and conditions")
            st.selectbox("State",options=['Punjab','HP','UK','UP','MP'])
        with col2:
            gender=st.radio("Gender", options=['Male','Female','Others'], horizontal=True)
            st.text_input("Pincode")
            st.multiselect("Interest",options=['Movies','Cricket','Web Series','Games','Reading Books'])
        st.slider("Age",min_value=5,max_value=70)
        st.time_input("Time")
        btn= st.form_submit_button("Submit", type='secondary')
        
    if btn:
        if name=="" or email=="" or password=="" or address=="" or dob=="" or gender=="":
            st.warning("Please fill all the fields")
            st.success("Please fill all the fields")
            st.error("Please fill all the fields")
        else:
            st.write("Name:",name)
            st.write("Email:",email)
            st.write("Password:",password)
            st.write("Address:",address)
            st.write("Date of Birth:",dob)
            st.write("Gender:",gender)
            st.write("Pincode:",st.text_input("Pincode"))
            st.write("Interest:",st.multiselect("Interest",options=['Movies','Cricket','Web Series','Games','Reading Books']))
            st.write("Age:",st.slider("Age",min_value=5,max_value=70))
            st.write("Time:",st.time_input("Time"))

elif a=='About':
    st.write("About")

elif a=='Contact':
    st.write("Contact us at 1234567890 or 987654321")
    

# st.sidebar.text_input("Check")


# coll1,coll2= st.columns(2)
# with coll1:
#     # st.image('covid.png')
#     with st.form(key='myform'):
#         st.write("Registration Form")
#         # col1,col2,col3= st.columns([1,2,1])
#         col1,col2= st.columns(2)
#         with col1:
#             name= st.text_input("First Name")
#             email= st.text_input("Email")
            
#         with col2:
#             name2= st.text_input("Last Name")
#             password= st.text_input("Password", type='password')
#         btn=st.form_submit_button("Submit")

# with coll2:

#     st.image('images1.jpeg')
    
    
# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# with tab1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
# with tab2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
# with tab3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
