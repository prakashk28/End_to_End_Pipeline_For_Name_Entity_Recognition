import streamlit as st
from src.Components.Predict import Predict

# Page configuration
st.set_page_config(page_title="Named Entity Recognition", layout="centered")

# Title of the application
st.header("Named Entity Recognition")

# Text input for the user to enter text
text = st.text_input("Enter text", placeholder="Enter text to extract Named Entities")

# When the predict button is pressed
if st.button("Predict"):

    # Check if the input text is not empty
    if text.strip() == "":
        st.error("Please enter some text to extract named entities.")
    else:
        try:
            # Call the prediction method from the Predict class
            predictions = Predict().predict_data(text=text)

            # Check if predictions are available and not empty
            if predictions:
                # Check if the predictions are a list of tuples (Entity, Label)
                if isinstance(predictions, list) and all(isinstance(i, tuple) and len(i) == 2 for i in predictions):
                    # Displaying named entities in a structured way (e.g., DataFrame)
                    st.subheader("Extracted Named Entities:")
                    entities = []
                    for entity, label in predictions:
                        entities.append({"Entity": entity, "Label": label})
                    # Show as a table
                    st.write(entities)
                else:
                    st.warning("The prediction format is not as expected.")
            else:
                st.warning("No named entities found in the text.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
