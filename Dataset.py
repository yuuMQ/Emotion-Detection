import cv2
import json
import glob
import os
from sympy.physics.units import yocto

if __name__ == '__main__':
    root = "./Data/ExpW/data"
    image_folder = os.path.join(root, "image", "origin")
    label_path = os.path.join(root, "label")
    output_path = "emotion_yolo"
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
        os.makedirs(os.path.join(output_path, "labels"))
        os.makedirs(os.path.join(output_path, "images"))

    output_folder = os.path.join(output_path, "labels")
    output_images = os.path.join(output_path, "images")
    for label_file in os.listdir(label_path):
        data_path = os.path.join(label_path, label_file)

        with open(data_path, "r") as f:
            lines = [file.rstrip() for file in f.readlines()]
            data = [line.split() for line in lines]

            for line in data:
                image_name, _, ytop, xtop, xbot, ybot, _, category = line
                xtop, ytop, xbot, ybot, category = int(xtop), int(ytop), int(xbot), int(ybot), int(category)

                label_file_path = os.path.join(output_folder, image_name.replace(".jpg", ".txt"))
                image = cv2.imread(os.path.join(image_folder, image_name))
                img_height, img_width, _ = image.shape

                box_width = xbot - xtop
                box_height = ybot - ytop
                xcent = xtop + box_width / 2
                ycent = ytop + box_height / 2

                xcent /= img_width
                ycent /= img_height
                box_width /= img_width
                box_height /= img_height

                with open(label_file_path, "a") as txt_file:
                    txt_file.write("{} {:6f} {:6f} {:6f} {:6f}\n".format(category, xcent, ycent, box_width, box_height))

                save_path = os.path.join(output_images, image_name)
                if not os.path.exists(save_path):
                    cv2.imwrite(save_path, image)
        break