import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("ipl_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="IPL Score Predictor", page_icon="🏏", layout="centered")
st.title("🏏 IPL Score Prediction App")
st.markdown("### Predict the final score of an IPL innings based on the current match situation.")

# --- INPUTS ---
batting_team = st.selectbox("Batting Team", [
    'Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab',
    'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
])

bowling_team = st.selectbox("Bowling Team", [
    'Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab',
    'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'
])

venue = st.selectbox("Match Venue", [
    'Wankhede Stadium', 'Eden Gardens', 'Feroz Shah Kotla',
    'M. Chinnaswamy Stadium', 'M. A. Chidambaram Stadium'
])

col1, col2 = st.columns(2)
with col1:
    runs = st.number_input("Current Runs", min_value=0)
    wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10)
with col2:
    overs = st.number_input("Overs Completed", min_value=5.0, max_value=20.0, step=0.1)
    runs_last_5 = st.number_input("Runs Scored in Last 5 Overs", min_value=0)

# --- ENCODING ---
team_encoder = {
    'Chennai Super Kings': 0, 'Delhi Capitals': 1, 'Kings XI Punjab': 2,
    'Kolkata Knight Riders': 3, 'Mumbai Indians': 4,
    'Rajasthan Royals': 5, 'Royal Challengers Bangalore': 6,
    'Sunrisers Hyderabad': 7
}

venue_encoder = {
    'Wankhede Stadium': 0, 'Eden Gardens': 1, 'Feroz Shah Kotla': 2,
    'M. Chinnaswamy Stadium': 3, 'M. A. Chidambaram Stadium': 4
}

bat_team_encoded = team_encoder[batting_team]
bowl_team_encoded = team_encoder[bowling_team]
venue_encoded = venue_encoder[venue]

# Create input dataframe with proper feature names
input_data = pd.DataFrame({
    'bat_team': [bat_team_encoded],
    'bowl_team': [bowl_team_encoded],
    'venue': [venue_encoded],
    'runs': [runs],
    'wickets': [wickets],
    'overs': [overs],
    'runs_last_5': [runs_last_5]
})

# --- PREDICT ---
if st.button("Predict Final Score"):
    try:
        prediction = model.predict(input_data)
        st.success(f"🏁 **Predicted Final Score:** {int(prediction[0])} runs")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

st.markdown("---")
st.caption("Developed by Shuban Borkar | Powered by Streamlit 🚀")
