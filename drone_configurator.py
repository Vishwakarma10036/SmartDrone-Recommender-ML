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
            "Battery Cells": "4S-6S",
            "Motor KV": "700-800",
            "Propeller Size (inches)": "10-12",
            "ESC Amperage (A)": "60",
            "Pictures and Purchase Links": {
                "Battery": {
                    "image": "https://m.media-amazon.com/images/I/71XiwBHsHgL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=4S-6S+LiPo+Battery"
                },
                "Motor": {
                    "image": "https://m.media-amazon.com/images/I/61Vni0HSOEL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=700-800kv+drone+motor"
                },
                "Propeller": {
                    "image": "https://m.media-amazon.com/images/I/61XSRSXxnmL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=10-12+inch+propeller"
                },
                "ESC": {
                    "image": "https://m.media-amazon.com/images/I/61rkq3A3Z7L._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=60A+ESC"
                }
            }
        }
    elif 500 <= payload_weight < 1000:
        return {
            "Battery Cells": "3S-4S",
            "Motor KV": "800-1000",
            "Propeller Size (inches)": "8-10",
            "ESC Amperage (A)": "50",
            "Pictures and Purchase Links": {
                "Battery": {
                    "image": "https://m.media-amazon.com/images/I/61HXIjP4OuL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=3S-4S+LiPo+Battery"
                },
                "Motor": {
                    "image": "https://m.media-amazon.com/images/I/71oH82RYQoL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=800-1000kv+drone+motor"
                },
                "Propeller": {
                    "image": "https://m.media-amazon.com/images/I/61PkpZPt1yL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=8-10+inch+propeller"
                },
                "ESC": {
                    "image": "https://m.media-amazon.com/images/I/61GAUPiEVOL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=50A+ESC"
                }
            }
        }
    elif 100 <= payload_weight < 500:
        return {
            "Battery Cells": "3S",
            "Motor KV": "1000-1500",
            "Propeller Size (inches)": "6-8",
            "ESC Amperage (A)": "40",
            "Pictures and Purchase Links": {
                "Battery": {
                    "image": "https://m.media-amazon.com/images/I/51bTq1cFtiL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=3S+LiPo+Battery"
                },
                "Motor": {
                    "image": "https://m.media-amazon.com/images/I/71pQMEFLVPL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=1000-1500kv+drone+motor"
                },
                "Propeller": {
                    "image": "https://m.media-amazon.com/images/I/51Hc15lcRaL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=6-8+inch+propeller"
                },
                "ESC": {
                    "image": "https://m.media-amazon.com/images/I/61JPnq+n7BL._AC_SL1500_.jpg",
                    "link": "https://www.amazon.com/s?k=40A+ESC"
                }
            }
        }
    else:
        return "Invalid payload weight. Please enter a value between 100g and 1500g."

# Streamlit app
st.title("Drone Configuration Recommender")
st.subheader("Get the best configuration for your payload weight.")

payload_weight = st.number_input("Enter the payload weight (in grams):", min_value=100, max_value=1500, step=50)

if st.button("Get Recommendation"):
    config = get_recommendations(payload_weight)
    if isinstance(config, dict):
        st.subheader("Recommended Drone Configuration")
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
