from roboflow import Roboflow
rf = Roboflow(api_key="kz3zDWBl5DFNUazmZEca")  # Reemplaza con tu clave
project = rf.workspace("yolov7test-u13vc").project("weapon-detection-m7qso")
dataset = project.version(16).download("yolov8")  # YOLOv11 usa el mismo formato que YOLOv8