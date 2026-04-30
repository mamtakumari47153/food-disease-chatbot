# 🍎 AI Food Quality Detection System (YOLOv8 + FastAPI)

An AI-powered backend system that detects whether a fruit is **fresh** or **rotten** using a custom-trained YOLOv8 classification model. The system exposes a REST API built with FastAPI, enabling real-time image-based predictions.

---

## 🚀 Overview

This project combines **Computer Vision** and **Backend Development** to solve a real-world problem — identifying food quality through image analysis.

Users can upload fruit images, and the system will:
- Classify the fruit as **Fresh** or **Rotten**
- Return a confidence score
- Handle unsupported inputs intelligently

---

## ✨ Key Features

- 📷 Image-based food classification
- 🤖 YOLOv8 custom-trained model (Ultralytics)
- ⚡ FastAPI for high-performance APIs
- 📊 Confidence-based prediction filtering
- 🚫 Handles unknown/unsupported fruits
- 🧠 Smart validation logic (low confidence & misclassification handling)

---

## 🧠 Tech Stack

| Layer              | Technology |
|-------------------|------------|
| Backend           | FastAPI |
| AI Model          | YOLOv8 (Ultralytics) |
| Programming Lang. | Python |
| Image Processing  | OpenCV, Pillow |
| ML Framework      | PyTorch |

---

## 📁 Project Structure
food-disease-chatbot/
│
├── main.py
├── requirements.txt
├── runs/
│ └── classify/train/weights/
│ └── best.pt
│
├── frontend/ (optional)
│ └── index.html
│
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/food-disease-chatbot.git
cd food-disease-chatbot


2️⃣ Create Virtual Environment
python -m venv myenv
myenv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Server
uvicorn main:app --reload

5️⃣ Open API Documentation
http://127.0.0.1:8000/docs

📡 API Usage
🔹 Endpoint
POST /chat/

🔹 Request
Method: POST
Content-Type: multipart/form-data
Body:
file: Image file

Response Example
{
  "detected_labels": ["freshbanana"],
  "confidence": 0.97,
  "bot": "✅ The banana is fresh and safe to eat."
}

⚠️ Supported Fruits
Currently trained on:


🍎 Apple


🍌 Banana


👉 If an unsupported fruit is uploaded:
⚠️ This fruit is not supported by the system.

🧪 Model Details


Model: YOLOv8 Classification


Framework: Ultralytics


Dataset: Custom dataset (Fresh vs Rotten fruits)


Model Path:


runs/classify/train/weights/best.pt

🧠 Core Logic


Confidence threshold filtering


Top-1 vs Top-2 probability gap validation


Label normalization (handles plural forms)


Robust error handling



🚀 Future Enhancements


Add more fruits (grapes, mango, etc.)


Improve model accuracy with larger dataset


Add chatbot UI interface


Deploy on cloud (AWS / Render / Docker)



👩‍💻 Author
Mamta Kumari
Python Backend Developer | AI Enthusiast

