import glob, os
import random
from pprint import pprint
from tqdm import tqdm


if __name__ == "__main__":

    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    raw_dir = f'{basedir}/data/raw'

    os.system('mkdir ../data/images')
    os.system('mkdir ../data/labels')

    total_images_path_list = [image for img_dir in os.listdir(raw_dir)
                              for image in glob.iglob(os.path.join(raw_dir, img_dir, '*.jpg'))]

    for image in tqdm(total_images_path_list):

        title, ext = os.path.basename(image).split('.')
        label = title.split('_')[-1]
        num = random.random()
        if num < 0.1:
            with open('../data/labels/test.txt','a') as f:
                f.write(f'{image} {label}\n')
        elif 0.1 < num < 0.3:
            with open('../data/labels/val.txt','a') as f:
                f.write(f'{image} {label}\n')
        else:
            with open('../data/labels/train.txt','a') as f:
                f.write(f'{image} {label}\n')

        os.system(f'cp {image} ../data/images')



# # put your own path here
# dataset_path = 'dataset'
# # Percentage of images to be used for the validation set
# percentage_test = 20
# os.system('mkdir data')
# os.system('mkdir data/images')
# os.system('mkdir data/labels')
# os.system('mkdir data/images/train')
# os.system('mkdir data/images/valid')
# os.system('mkdir data/labels/train')
# os.system('mkdir data/labels/valid')
#
# # Populate the folders
# p = percentage_test/100
# for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpeg")):
#     title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#     if random.random() <=p :
#         os.system(f"cp {dataset_path}/{title}.jpeg data/images/valid")
#         os.system(f"cp {dataset_path}/{title}.txt data/labels/valid")
#     else:
#         os.system(f"cp {dataset_path}/{title}.jpeg data/images/train")
#         os.system(f"cp {dataset_path}/{title}.txt data/labels/train")
