from ultralytics import YOLO

model=YOLO("yolov8m.pt")

model.train(data="data_custom.yaml",imgsz=640,epochs=5,workers=1)

