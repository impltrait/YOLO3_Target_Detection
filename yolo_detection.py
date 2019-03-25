# file: yolo_detection.py
# author: BINWong
# time: 2019/1/12 12:30
# Copyright 2019 BINWong. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import os
import time
save_image = 'image_save'


def detect_img(yolo):

    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except AttributeError:
            print('AttributeError ----> 您没有输入路径')
            continue
        except FileNotFoundError:
            print('FileNotFoundError ----> 寻找不到你输入的路径内容! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
            if not os.path.exists(save_image):
                os.makedirs(save_image)
            image_name = str(int(time.time()))+'.jpg'
            r_image.save(os.path.join(save_image, image_name), quality=95)

    yolo.close_session()


FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    命令行参数
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str, required=False, default='./video_path_two',
        help="Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="",
        help="[Optional] Video output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        图像检测模式，忽略任何剩余的命令行参数
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)))
    elif "input" in FLAGS:
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")

