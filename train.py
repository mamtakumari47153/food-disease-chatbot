from ultralytics import YOLO

print("🚀 Training started...")

# Load YOLO classification model
model = YOLO("yolov8n-cls.pt")

# Train model on your dataset
model.train(
    data="dataset",
    epochs=10,
    imgsz=224
)

print("✅ Training completed!")