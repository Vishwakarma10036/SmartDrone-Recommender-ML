# 🚁 SmartDrone-Recommender-ML

SmartDrone-Recommender-ML is a machine learning-powered system that helps users select optimal drone components based on their desired payload capacity. Whether you're building drones for delivery, surveillance, or emergency response, this tool streamlines the component selection process by analyzing performance data and recommending the best fit.

---

## 📌 Features

- 💡 **Payload-Based Recommendation**: Input your desired payload (in grams or kg).
- ⚙️ **Component Prediction**:
  - Motor KV & thrust capacity
  - Propeller size and pitch
  - ESC rating
  - Battery type (LiPo, cell count, mAh)
  - Frame size
- 🧠 **ML-Powered**: Trained using regression and classification models on real-world drone configuration datasets.
- 📊 **Performance-Oriented**: Ensures optimal thrust-to-weight ratio, flight time, and stability.
- 🌐 **Interactive Web UI** (via Streamlit/Flask)

---

## 📁 Project Structure

- `data/`: Cleaned and labeled dataset used for training.
- `notebooks/`: Jupyter notebooks for EDA and model development.
- `src/`: Core ML code for preprocessing and inference.
- `webapp/`: Lightweight UI for user interaction and predictions.
- `requirements.txt`: Python dependencies list.

---

## 📊 Dataset Format

Sample columns in `drone_components.csv`:

| Payload (g) | Motor KV | Propeller Size (inch) | ESC Rating (A) | Battery (mAh) | Battery Cells | Frame Size (mm) |
|-------------|----------|------------------------|----------------|----------------|----------------|-----------------|
| 500         | 920      | 10x4.5                 | 30             | 2200           | 3S             | 450             |

---

## 🧠 Model Training

- ML Algorithms: Random Forest, XGBoost, Decision Trees
- Evaluation Metrics: MAE, R² Score
- Hyperparameter tuning via GridSearchCV

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/SmartDrone-Recommender-ML.git
cd SmartDrone-Recommender-ML
