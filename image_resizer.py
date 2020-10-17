import cv2
import glob
import os
import ntpath


image_types = ['gif', 'jpg', 'png']

image_files = []

image_path = str(input("Please enter path of the images (default: current location): ").lower() or ".")

reduction_rate = int(input("how many percent reduction do you want? (default: 50): ") or "50")

def resize(path):
    # add all image file type in directory
    print("inside function")
    print(path)
    # if path == "":
        # path = "."
        
    # if reduction_rate == "" | isinstance(reduction_rate, str) == True:
        # reduction_rate = 50
        # print(type(reduction_rate))

    for img_type in image_types:
        
        images = glob.glob(path+"/*"+img_type)
        for img in images:
            image_files.append(img)
        
        print("Images picked successful")


    for image in image_files:
        
        # 0 flag black and white, 1 colored and - 1 unchanged including transparency
        img = cv2.imread(image, 1)
        print(type(image))
        print(image)
        print(img.shape)
        
        # resize image to 20% of current size
        res_img = cv2.resize(img, (int(img.shape[1]*(reduction_rate/100)), int(img.shape[0]*(reduction_rate/100))))
        print(res_img.shape)
        
        # display resized image before saving
        #cv2.imshow("resized_"+image, res_img)
        #cv2.waitKey(0)  # wait till a key is pressed
        
        image_name = ntpath.basename(image)
        print(image_name)
        cv2.imwrite(os.path.join(path , "resized_"+image_name), res_img)
        print("Images resized successful")
        #retval = os.getcwd()
        #print("Current working directory: " + retval)
        
        cv2.destroyAllWindows()


resize(image_path)


# print(img.ndim)

cv2.destroyAllWindows()