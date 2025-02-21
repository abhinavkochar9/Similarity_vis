import streamlit as st
import os
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Similarity Graphs Viewer", layout="wide")
st.title("Similarity Graphs Viewer")

# Base directory where your similarity database is stored.
# Structure assumed:
# BASE_DIR/
#   Patient1/
#     Exercise1/
#       similarity_individual.html
#       similarity_average.html
#     Exercise2/
#       ...
#   Patient2/
#     Exercise1/
#       similarity_individual.html
#       similarity_average.html
current_dir = os.path.dirname(__file__)
BASE_DIR = os.path.join(current_dir, "..", "Similarity_DB_HTML")

if not os.path.exists(BASE_DIR):
    st.error("The base directory does not exist. Please check the path in BASE_DIR.")
else:
    # List all patient folders
    patients = sorted([d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))])
    selected_patient = st.sidebar.selectbox("Select Patient", patients)
    
    patient_dir = os.path.join(BASE_DIR, selected_patient)
    # List all exercise folders for the selected patient
    exercises = sorted([d for d in os.listdir(patient_dir) if os.path.isdir(os.path.join(patient_dir, d))])
    selected_exercise = st.sidebar.selectbox("Select Exercise", exercises)
    
    st.header(f"Patient: {selected_patient} | Exercise: {selected_exercise}")
    
    # Construct paths to the HTML graph files
    exercise_dir = os.path.join(patient_dir, selected_exercise)
    html_graph1_path = os.path.join(exercise_dir, "similarity_individual.html")
    html_graph2_path = os.path.join(exercise_dir, "similarity_average.html")
    
    # Display the Individual Similarity Graph HTML
    if os.path.exists(html_graph1_path):
        with open(html_graph1_path, "r", encoding="utf-8") as f:
            graph1_html = f.read()
        st.subheader("Individual Similarity Graph")
        # You may adjust the height and scrolling parameters as needed
        components.html(graph1_html, height=600, scrolling=True)
    else:
        st.warning("Individual Similarity Graph HTML file not found.")
    
    # Display the Average Similarity Graph HTML
    if os.path.exists(html_graph2_path):
        with open(html_graph2_path, "r", encoding="utf-8") as f:
            graph2_html = f.read()
        st.subheader("Average Similarity Graph")
        components.html(graph2_html, height=600, scrolling=True)
    else:
        st.warning("Average Similarity Graph HTML file not found.")
