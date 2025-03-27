from ultralytics import YOLO

# Cargar modelo base (nano para empezar, más ligero)
model = YOLO('yolo11n.pt')

# Entrenar con el dataset
model.train(data='weapon-detection-16/data.yaml', epochs=50, imgsz=640, device='cpu')