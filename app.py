import streamlit as st

st.set_page_config(page_title='Engine Bay',page_icon="🔰")
st.markdown('<img align="left" src="https://github.com/GarethSequeira/Car-Resale-Valuation/blob/main/static/enginebay.png?raw=true" width="100%"> ', unsafe_allow_html=True)

import pickle
model = pickle.load(open('car_valuation_model.pkl','rb'))


def main():
    
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<h1>Car Resale Valuation</h1> ', unsafe_allow_html=True)
    st.markdown('<h3>Planning to sell your Car? Get a valuation now.</h3> ', unsafe_allow_html=True)

    # @st.cache(allow_output_mutation=True)
    # def get_model():
    #     model = pickle.load(open('car_valuation_model.pkl','rb'))
    #     return model

    st.write('')
    st.write('')

    car= st.text_input("Enter Car Company and Model Name")

    years = st.number_input('In Which Year was the Car Purchased?', 2000, 2020, step=1, key ='year')
    Years_old = 2020-years

    Present_Price = st.number_input('What is the Current Ex-Showroom Price of the Car?  ₹ (Lakhs)', 0.00, 50.00, step=0.5, key ='present_price') 

    Kms_Driven = st.number_input('How many Kms has the Car Completed?', 0, 500000, step=500, key ='drived')

    Owner = st.radio("How many Owners has the Car had?", (1, 2, 3), key='owner')

    Fuel_Type_Petrol = st.selectbox('What is the Fuel Type of the Car?',('Petrol','Diesel', 'CNG'), key='fuel')
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif(Fuel_Type_Petrol=='Diesel'):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0

    Seller_Type_Individual = st.selectbox('Are you a Dealer or an Individual?', ('Dealer','Individual'), key='dealer')
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0	

    Transmission_Mannual = st.selectbox('What is the Transmission Type of the Car?', ('Manual','Automatic'), key='manual')
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0

    st.markdown('<br>', unsafe_allow_html=True)
    if st.button("Get Valuation", key='predict'):
        try:
            Model = model  #get_model()
            prediction = Model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            output = round(prediction[0],2)
            if output<0:
                st.markdown('<br>', unsafe_allow_html=True)
                st.warning("This Car may be Unsellable!")
                st.markdown('<br>', unsafe_allow_html=True)
                st.markdown('<img align="left" src="https://github.com/GarethSequeira/Car-Resale-Valuation/blob/main/static/carrect.gif?raw=true" width="100%"> ', unsafe_allow_html=True)
            else:
                st.markdown('<br>', unsafe_allow_html=True)
                st.success("Estimated Resale Value for the Car is ₹ {} Lakhs!".format(output))
                st.markdown('<br>', unsafe_allow_html=True)
                st.markdown('<img align="left" src="https://github.com/GarethSequeira/Car-Resale-Valuation/blob/main/static/carrect.gif?raw=true" width="100%"> ', unsafe_allow_html=True)
        except:
            st.markdown('<br>', unsafe_allow_html=True)
            st.warning("Oops! Something went Wrong.\nPlease Try again.")
            st.markdown('<br>', unsafe_allow_html=True)
            st.markdown('<img align="left" src="https://github.com/GarethSequeira/Car-Resale-Valuation/blob/main/static/carrect.gif?raw=true" width="100%"> ', unsafe_allow_html=True)

    st.markdown('<br><br><br><br><br>', unsafe_allow_html=True)

    col1,col2,col3,col4 = st.beta_columns(4)
    col1.markdown('<a href="https://enginebay.herokuapp.com/"><img align="left" alt="Engine Bay" width="45px" src="https://img.icons8.com/ios-filled/2x/4a90e2/car-sale.png" /></a> ', unsafe_allow_html=True)
    col2.markdown('<a href="https://www.garethsequeira.com/"><img align="right" alt="Website" width="50px" src="https://img.icons8.com/material-sharp/2x/4a90e2/google-logo.png" /></a> ', unsafe_allow_html=True)
    col3.markdown('<a href="https://github.com/garethsequeira/"><img align="left" alt="Github" width="50px" src="https://img.icons8.com/ios-filled/2x/4a90e2/github.png" /></a> ', unsafe_allow_html=True)
    col4.markdown('<a href="https://www.linkedin.com/in/garethsequeira/"><img align="right" alt="Linkedin" width="50px" src="https://img.icons8.com/ios-filled/2x/4a90e2/linkedin-circled.png" /></a> ', unsafe_allow_html=True)

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

if __name__ == "__main__":
    main()