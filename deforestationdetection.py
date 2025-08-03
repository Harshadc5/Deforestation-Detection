import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Forest Fire Prediction",
    page_icon="🔥",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stNumberInput, .stSelectbox {
        margin-bottom: 1rem;
    }
    .prediction-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header section
col1, col2 = st.columns([1, 6])
with col1:
    st.image(Image.open("fire_icon.png"), width=60)  # Replace with your icon or use "🔥"
with col2:
    st.title("Forest Fire Prediction")

# Input section
st.subheader("Predict the probability of Forest Fire Occurrence")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        temperature = st.number_input(
            "Temperature (°C)",
            min_value=-20.0,
            max_value=60.0,
            value=25.0,
            step=0.1,
            help="Ambient temperature in Celsius"
        )
        
        oxygen = st.number_input(
            "Oxygen (ppm)",
            min_value=0.0,
            max_value=25.0,
            value=19.5,
            step=0.1,
            help="Oxygen content in parts per million"
        )
    
    with col2:
        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=0.1,
            help="Relative humidity percentage"
        )
        
        co2 = st.number_input(
            "CO₂ Level (ppm)",
            min_value=300.0,
            max_value=2000.0,
            value=400.0,
            step=1.0,
            help="Carbon dioxide concentration"
        )
    
    predict_button = st.form_submit_button("Predict")

# Prediction section
if predict_button:
    # Corrected calculation with proper parentheses
    risk_score = min(max((temperature - 20) * 2 + (100 - humidity) * 0.3, 0), 100)
    
    st.markdown("---")
    st.subheader("Prediction Result")
    
    if risk_score > 70:
        risk_level = "🔥 High Risk"
        color = "#ff4b4b"
    elif risk_score > 40:
        risk_level = "⚠️ Moderate Risk"
        color = "#ffa500"
    else:
        risk_level = "✅ Low Risk"
        color = "#2ecc71"
    
    st.markdown(f"""
    <div class="prediction-box">
        <h3 style='color: {color}; text-align: center;'>{risk_level}</h3>
        <p style='text-align: center; font-size: 24px;'>
            Probability: <b>{risk_score:.1f}%</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Visual feedback
    st.progress(risk_score/100)
    
    if risk_score > 70:
        st.warning("High probability of fire - take precautions!")
    elif risk_score > 40:
        st.info("Moderate fire risk - monitor conditions")
    else:
        st.success("Low fire risk - normal conditions")

# Footer
st.markdown("---")
st.caption("Forest Fire Prediction System v1.0 | 127.0.0.1:8501")