## Yolo3-keras 实现

有问题！请你们及时反馈

## 快随启动

- [下载YOLOv3权重](https://pjreddie.com/media/files/yolov3.weights)

- 将Darknet YOLO模型转换为Keras模型

- 运行YOLO进行检测

## 读取Darknet配置和权值，并使用TF后端创建Keras模型

    python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5

## 图片检测

    python yolo_detection.py --image 
     
    随后有输入图片路径的提示，如：Input image filename:

## 视频检测

    python yolo_detection.py --input **A**
    
    **A**:标识进行检测的视频路径

## 远程跟踪及本地相机检测

    python yolo_detection.py --input 0
    
    0：标识打开本地相机开启检测，远程的也是

## 使用

使用 --help 查看yolo_video.py的用法

    使用: yolo_detection.py [-h] [--model MODEL] [--anchors ANCHORS]
                            [--output]

    位置参数:[--classes CLASSES] [--gpu_num GPU_NUM] [--image]
                           [--input]
    
      --input        视频输入路径
      --output       视频输出路径
    
    可选参数:
    
      -h, --help         显示此帮助消息并退出
      --model MODEL      模型权重文件的路径, 默认 model_data/yolo.h5
      --anchors ANCHORS  锚定义路径, 默认 model_data/yolo_anchors.txt
      --classes CLASSES  类定义的路径, 默认 model_data/coco_classes.txt
      --gpu_num GPU_NUM  要使用的GPU数量, 默认 1
      --image            图像检测模式，将忽略所有位置参数

## 训练

- 生成您自己的注释文件和类名文件
    - 一行对应一个图像
    
    - 行格式：image_file_path box1 box2 ... boxN
    
    - 盒子格式：x_min,y_min,x_max,y_max,class_id (no space).
    
    - 对于VOC数据集，请尝试  python voc_annotation.py
    
    - 这里有一个例子：
    
    path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
    
    path/to/img2.jpg 120,300,250,600,2
    ...

-- -

你确保已经跑过了 

    python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5

文件model_data/yolo_weights.h5用于加载预先训练好的权重

修改train.py开始训练
    
    python train.py
    
用您的训练权重或检查点权重与命令行选项 --model model_file 当使用yolo_video.py 记得修改类路径或锚点路径 --classes class_file and --anchors anchor_file.

如果你想为YOLOv3使用原始的预先训练的权重:

    https://pjreddie.com/media/files/darknet53.conv.74
    
将其重命名为darknet53.weights
    
    python convert.py -w darknet53.cfg darknet53.weights model_data/darknet53_weights.h5
    
use model_data/darknet53_weights.h5 in train.py


## 参考其他资料

- [优先](https://blog.csdn.net/mingqi1996/article/details/83343289)

- [其次](https://blog.csdn.net/KKKSQJ/article/details/83587138)
