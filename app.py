import pickle
import streamlit as st
import math
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, Dependents, Education, Self_Employed, Property_Area, Loan_Amount, Total_Income, EMI, Balance_Income, Credit_History):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
        
    if Dependents == "0":
        Dependents = 0
    elif Dependents == "1":
        Dependents = 1
    elif Dependents == "2":
        Dependents = 2
    else:
        Dependents = 3
        
    if Education == "NonGraduate":
        Education = 0
    else:
        Education = 1
        
    if Self_Employed == "No":
        Self_Employed = 0
    else:
        Self_Employed = 1  
 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
        
    if Property_Area == "Rural":
        Property_Area = 0
    elif Property_Area == "Semiurban":
        Property_Area = 1
    else:
        Property_Area = 2
        
    Loan_Amount = math.log(Loan_Amount)
    
    Total_Income = math.log(Total_Income)
    
    EMI = math.log(EMI)
    
    Balance_Income = math.log(Balance_Income)
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married, Dependents, Education, Self_Employed, Property_Area, Loan_Amount, Total_Income, EMI, Balance_Income, Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:purple;padding:20px"> 
    <h1 style ="color:black;text-align:center;">Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    Dependents = st.selectbox('Number of Dependents',("0","1","2","3"))
    Education = st.selectbox('Education',("Graduate", "NonGraduate"))
    Self_Employed = st.selectbox('Self_Employed',("Yes", "No"))
    Property_Area = st.selectbox('Property Area',("Rural", "Semiurban", "Urban"))
    Loan_Amount = st.number_input("Total loan Amount")
    Total_Income = st.number_input("Applicants Monthly Income") 
    EMI = st.number_input("Equated Monthly Installment (EMI)")
    Balance_Income = st.number_input("Balance Income")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Married, Dependents, Education, Self_Employed, Property_Area, Loan_Amount, Total_Income, EMI, Balance_Income, Credit_History) 
        st.success('Your loan is {}'.format(result))
        print(Loan_Amount)
     
if __name__=='__main__': 
    main()