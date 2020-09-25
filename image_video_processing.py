import cv2
import glob

image_types = ['gif', 'jpg', 'png']

image_files = []

# add all image file type in directory
for img_type in image_types:
    images = glob.glob("*"+img_type)
    for img in images:
        image_files.append(img)


for image in image_files:
    # 0 flag black and white, 1 colored and - 1 unchanged including transparency
    img = cv2.imread(image, 1)
    print(img.shape)
    # resize image to 20% of current size
    res_img = cv2.resize(img, (int(img.shape[1]*0.2), int(img.shape[0]*0.2)))
    print(res_img.shape)
    # display resized image before saving
    cv2.imshow("resized_"+image, res_img)
    cv2.waitKey(0)  # wait till a key is pressed
    cv2.imwrite("resized_"+image, res_img)
    cv2.destroyAllWindows()


# print(img.ndim)

cv2.destroyAllWindows()
