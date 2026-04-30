from ultralytics import YOLO
from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI()

model = YOLO("runs/classify/train/weights/best.pt")

THRESHOLD = 0.5


# ✅ Only trained classes
SUPPORTED_CLASSES = [
    "freshapple", "rottenapple",
    "freshbanana", "rottenbanana"
]

@app.post("/chat/")
async def chat(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Prediction
        results = model(file_path)
        result = results[0]
        probs = result.probs

        predicted_class = result.names[probs.top1]
        top1_conf = float(probs.top1conf)

        # 🔥 GAP LOGIC (Top1 vs Top2)
        top5conf = probs.top5conf
        top2_conf = float(top5conf[1]) if len(top5conf) > 1 else 0.0
        gap = top1_conf - top2_conf

        label = predicted_class.lower()
        fruit = label.replace("fresh", "").replace("rotten", "")

        # 🔥 FINAL DECISION
        if gap < 0.3:
            response = "⚠️ This food item is not clearly recognized. Please upload a supported fruit image."

        elif predicted_class not in SUPPORTED_CLASSES:
            response = "⚠️ This fruit is not supported by the system. Please upload apple or banana."

        elif top1_conf < THRESHOLD:
            response = "❓ Unable to confidently detect the food. Please upload a clearer image."

        else:
            if "rotten" in label:
                response = f"⚠️ The {fruit} is rotten and not safe to eat."
            else:
                response = f"✅ The {fruit} is fresh and safe to eat."

        return {
            "detected_labels": [predicted_class],
            "confidence": round(top1_conf, 2),
            "gap": round(gap, 2),
            "bot": response
        }

    finally:
        # Cleanup (always runs)
        if os.path.exists(file_path):
            os.remove(file_path)