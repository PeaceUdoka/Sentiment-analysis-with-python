# import streamlit run app.py

# import librarues 
import streamlit as st
import joblib

#load model and vectorizer
model = joblib.load('LR_model.pkl')
vect = joblib.load('TfIdf_vect.pkl')

# app title
st.title("What's Your Mood?")

# read user feedback input 
input_text = st.text_area("Your feelings matter! Drop your feedback below, and let’s analyze the vibes!", "Type here...")

# predict button
predict = st.button("Decode my mood")

if input_text != "":
    st.session_state.prediction = None  # Reset prediction when user types

if predict:
    # Transform the input text using the vectorizer
    input_vector = vect.transform([input_text])
    
    # Make prediction
    st.session_state.prediction = model.predict(input_vector)[0]

# Display results based on prediction
if st.session_state.prediction is not None:
    if st.session_state.prediction == 0:
        st.markdown(f"If complaining were an Olympic sport, you’d definitely take home the gold!")
        st.markdown("![unhappy](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMThvamM0ZWE4MHU5cWRybmozYTAwdHAwZjVuMW4xOGo2Ynlyd2g1NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/c3XhrmfoN5fOpjcl3z/giphy.gif)")
    else:
        st.markdown(f"Glad you are feeling good. Just remember to share that joy with the world!")
        st.markdown("![happy](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjI1ZXo1a2JjZ3Z2cDE2eGVtZmp5Z3l2bTIybnd5YjNoY3l6OWowdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/14udF3WUwwGMaA/giphy.gif)")

