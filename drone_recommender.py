import streamlit as st
from PIL import Image
import requests
from io import BytesIO

def get_recommendations(payload_weight):
    """
    Recommends drone configuration based on payload weight with pictures and purchase links.
    """
    if 1000 <= payload_weight <= 1500:
        return {
            "Frame": "Frame 1 (Heavy Duty Frame)",
            "Frame Size (inches)": "450mm",
            "Recommended Payload Capacity": "1000-1500g",
            "Pictures and Purchase Links": {
                "Frame": {
                    "image": "https://m.media-amazon.com/images/I/71g3WzDqlVL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=450mm+drone+frame"
                }
            }
        }
    elif 500 <= payload_weight < 1000:
        return {
            "Frame": "Frame 2 (Medium Duty Frame)",
            "Frame Size (inches)": "350mm",
            "Recommended Payload Capacity": "500-1000g",
            "Pictures and Purchase Links": {
                "Frame": {
                    "image": "https://m.media-amazon.com/images/I/81t9IalpcwL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=350mm+drone+frame"
                }
            }
        }
    elif 100 <= payload_weight < 500:
        return {
            "Frame": "Frame 3 (Lightweight Frame)",
            "Frame Size (inches)": "250mm",
            "Recommended Payload Capacity": "100-500g",
            "Pictures and Purchase Links": {
                "Frame": {
                    "image": "https://m.media-amazon.com/images/I/71lhO-+tbdL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=250mm+drone+frame"
                }
            }
        }
    else:
        return "Invalid payload weight. Please enter a value between 100g and 1500g."

# Streamlit app
st.title("Drone Frame Configuration Recommender")
st.subheader("Get the best drone frame for your payload weight.")

payload_weight = st.number_input("Enter the payload weight (in grams):", min_value=100, max_value=1500, step=50)

if st.button("Get Recommendation"):
    config = get_recommendations(payload_weight)
    if isinstance(config, dict):
        st.subheader("Recommended Drone Frame Configuration")
        for key, value in config.items():
            if key == "Pictures and Purchase Links":
                st.subheader("Pictures and Purchase Links:")
                for component, details in value.items():
                    st.markdown(f"**{component}**")
                    st.image(details['image'], caption=f"[Buy Here]({details['link']})", use_column_width=True)
            else:
                st.markdown(f"**{key}:** {value}")
    else:
        st.error(config)
