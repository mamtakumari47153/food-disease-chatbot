from ultralytics import YOLO

model = YOLO("runs/classify/train/weights/best.pt")

def detect_disease(image_path):
    results = model(image_path)

    label = results[0].names[results[0].probs.top1]
    return [label]