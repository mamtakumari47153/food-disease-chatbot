# from ultralytics import YOLO

# # For now use pretrained model (we'll train later)
# model = YOLO("yolov8n.pt")

# def detect_disease(image_path):
#     results = model(image_path)

#     labels = []
#     for r in results:
#         for box in r.boxes:
#             cls = int(box.cls[0])
#             label = model.names[cls]
#             labels.append(label)

#     return labels

from ultralytics import YOLO

model = YOLO("runs/classify/train/weights/best.pt")

def detect_disease(image_path):
    results = model(image_path)

    label = results[0].names[results[0].probs.top1]
    return [label]