import cv2
from ultralytics import YOLO

# Cargar el modelo entrenado
model = YOLO('runs/detect/train/weights/best.pt')

# Abrir la webcam
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar predicción
    results = model(frame)
    annotated_frame = results[0].plot()  # Dibuja bounding boxes

    # Mostrar resultado
    cv2.imshow('Detección de Armas', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()