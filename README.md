# 🏏 IPL Score Prediction App

A machine learning-powered web application that predicts the final score of an IPL (Indian Premier League) cricket match based on the current match situation.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 🌟 Features

- **Real-time Predictions**: Get instant score predictions based on current match situation
- **User-friendly Interface**: Clean and intuitive Streamlit interface
- **High Accuracy**: Machine learning model with 94.8% accuracy (R² score: 0.948)
- **Multiple Teams & Venues**: Supports 8 IPL teams and 5 major venues

## 📊 Supported Teams

- Chennai Super Kings
- Delhi Capitals
- Kings XI Punjab
- Kolkata Knight Riders
- Mumbai Indians
- Rajasthan Royals
- Royal Challengers Bangalore
- Sunrisers Hyderabad

## 🏟️ Supported Venues

- Wankhede Stadium
- Eden Gardens
- Feroz Shah Kotla
- M. Chinnaswamy Stadium
- M. A. Chidambaram Stadium

## 🚀 Local Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone this repository:
```bash
git clone <your-repo-url>
cd IPL-Score-Prediction
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## ☁️ Deploying to Streamlit Cloud

### Step 1: Prepare Your GitHub Repository

1. Create a new repository on GitHub
2. Push your code:
```bash
git init
git add .
git commit -m "Initial commit: IPL Score Prediction App"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Fill in the details:
   - **Repository**: Select your GitHub repository
   - **Branch**: `main` (or your default branch)
   - **Main file path**: `app.py`
5. Click "Deploy!"

Your app will be live in a few minutes! 🎉

## 📁 Project Structure

```
IPL-Score-Prediction/
├── app.py                          # Main Streamlit application
├── ipl_model.pkl                   # Trained ML model
├── ipl_data.csv                    # Training dataset
├── IPL_Score_Prediction.ipynb      # Jupyter notebook (model development)
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore file
└── README.md                       # Project documentation
```

## 🎯 How to Use

1. **Select Batting Team**: Choose the team that is currently batting
2. **Select Bowling Team**: Choose the team that is currently bowling
3. **Select Venue**: Choose the match venue
4. **Enter Current Match Stats**:
   - Current Runs scored
   - Wickets fallen
   - Overs completed (minimum 5 overs)
   - Runs scored in the last 5 overs
5. Click **"Predict Final Score"** to get the prediction

## 🧠 Model Details

- **Algorithm**: Random Forest Regressor
- **Features**: 7 input features (team encodings, venue, runs, wickets, overs, recent form)
- **Accuracy**: R² Score of 0.948
- **Training Data**: Historical IPL match data

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **ML Framework**: scikit-learn
- **Data Processing**: pandas, numpy
- **Model Serialization**: pickle

## 📝 Notes

- The app requires a minimum of 5 overs to be completed for prediction
- Predictions are based on historical IPL data and current match conditions
- The model considers team strength, venue characteristics, and recent performance

## 👨‍💻 Developer

**Shuban Borkar**

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## ⭐ Show Your Support

Give a ⭐️ if you like this project!

---

Made with ❤️ and Streamlit 🚀

