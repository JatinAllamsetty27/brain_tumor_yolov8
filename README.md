## Brain Tumor Detection using YOLOv8 Model

This repository contains instructions for training a YOLOv8 model to detect brain tumors in medical images. The dataset for this project is randomly downloaded from the browser using `download_images.py` and later labeled using the `labelImg` tool.

### Prerequisites

Before you begin, make sure you have the following:

- Python installed on your system.
- [YOLOv8 repository](https://github.com/ultralytics/yolov5) cloned to your local machine.
- [labelImg](https://github.com/tzutalin/labelImg) installed for labeling the images.


### Steps to be followed

- Clone the YOLOv8 repository
- git clone https://github.com/ultralytics/yolov8.git

- Install dependencies
- pip install -r requirements.txt

- Run download_images.py to download brain scan images and save to a folder, e.g. /data/images
- Use labelImg tool to manually label tumor locations in the images and export annotation XMLs
- Add the labeled image folder path and details in data.yaml
- Modify yolov8-custom.yaml for custom model architecture
- Preprocess the images using preprocess.py
- Train the YOLOv8 model on the brain tumor data:
- python train.py --data data.yaml --cfg yolov8-custom.yaml --weights yolov8.pt

- Evaluate the model on test data:
- python test.py --weights runs/train/exp/weights/best.pt --data data.yaml --img 640

- Perform inference on new images:
- python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.4 --source img1.png

- Postprocess detections using postprocess.py

### Dataset Preparation

1. Download the dataset of medical images containing brain scans with and without tumors. You can do this using the `download_images.py` script.

2. Label the downloaded images to indicate the location and boundaries of the tumors using the `labelImg` tool. This step is crucial for training the YOLOv8 model.

### Model Training

1. Go to the YOLOv8 repository directory that you cloned earlier.

2. Train the YOLOv8 model on the labeled brain tumor dataset. You can use the following command:

   ```bash
   python train.py --data path/to/your/data.yaml --cfg path/to/your/yolov8-config.yaml --weights yolov8.weights
   ```

   Replace `path/to/your/data.yaml` with the path to your dataset configuration file and `path/to/your/yolov8-config.yaml` with the path to your YOLOv8 configuration file. You can also specify the pre-trained weights you want to use with the `--weights` option.

3. During training, monitor the model's performance and loss on the training and validation sets to ensure it's learning correctly and not overfitting.

### Testing

1. Once the model is trained, evaluate its performance on a separate test dataset to assess its ability to generalize to new, unseen data.

### Post-processing and Visualization

After obtaining predictions from the model, you may need to post-process the results to filter out false positives and refine the tumor boundaries. Visualize the results by overlaying bounding boxes or contours on the original medical images to show the detected tumors.

### Performance Metrics

Calculate performance metrics such as precision, recall, F1-score, and accuracy to assess the model's accuracy in detecting brain tumors.

![image](https://github.com/JatinAllamsetty27/brain_tumor_yolov8/assets/78016929/28e26264-b956-49a7-be06-4b3089e5b8a4)



### Prediction

![image](https://github.com/JatinAllamsetty27/brain_tumor_yolov8/assets/78016929/d16d51ca-310e-4802-bce4-73c21243dbe7)






### Deployment



![image](https://github.com/JatinAllamsetty27/brain_tumor_yolov8/assets/78016929/e796feef-39bd-4878-abde-d3406cfb378c)  




---


