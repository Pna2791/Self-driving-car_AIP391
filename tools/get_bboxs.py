import cv2
import glob

# params options

img_folder = 'D:\Desktop\AIP391\Lane detection\data/traffic signs data\cleaned data/'
label_folder = 'D:\Desktop\AIP391\Lane detection\data/traffic signs data\cleaned data/'
saveing_folder = "D:\Desktop\AIP391\Lane detection\data/traffic signs data/50x50 bboxs/"
shape = (50, 50)

# =================================================================================

if __name__ == "__main__":
    image_paths = glob.glob(img_folder+"*.png")
    image_paths.sort()
    label_paths = glob.glob(label_folder+"*.txt")
    label_paths.sort()
    print(len(image_paths), len(label_paths))
    cnt = 0
    for i in range(len(image_paths)):
        img = cv2.imread(image_paths[i])
        texts = open(label_paths[i], "r")
        print(image_paths[i])
        print(label_paths[i])
        print(f'{i}            {img.shape}')
        lines, names = [], []
        while (line := texts.readline()):
            lines.append(line)
            name, b1, b2, b3, b4, *tmp = [float(x) for x in line.split()]
            name = int(name)
            names.append(name)
        #     b3 *= 1.1
        #     b4 *= 1.1
        #     cv2.rectangle(img, pt1=(int((b1+b3/2)*img.shape[1]), int((b2+b4/2)*img.shape[0])),
        #                   pt2=(int((b1-b3/2)*img.shape[1]), int((b2-b4/2)*img.shape[0])), color=(0, 0, 255), thickness=2)
        # # print(names)
        # ratio = max(img.shape)/1080
        # img = cv2.resize(img, (int(img.shape[1]/ratio), int(img.shape[0]/ratio)), interpolation=cv2.INTER_NEAREST)
        # # cv2.imshow('image', img)

        # if cv2.waitKey(0)==ord(' '):
        img = cv2.imread(image_paths[i])
        for line in lines:
            name, b1, b2, b3, b4, *tmp = [float(x) for x in line.split()]
            name = int(name)
            b3 *= 1.1
            b4 *= 1.1
            # cropped image
            cropped_image = img[max(int((b2-b4/2)*img.shape[0]), 0): min(int((b2+b4/2)*img.shape[0]), img.shape[0]),
                                max(int((b1-b3/2)*img.shape[1]), 0): min(int((b1+b3/2)*img.shape[1]), img.shape[1])]
            # save to folder
            cropped_image = cv2.resize(cropped_image, shape)
            cnt += 1
            cv2.imwrite(
                filename=f'{saveing_folder}{name}/{cnt}.png', img=cropped_image)
        

    print(cnt)
    cv2.destroyAllWindows()
