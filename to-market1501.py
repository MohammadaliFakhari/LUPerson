import os
import shutil
import random

# base_path = '/media/vision/bigstorage/publish_data'
# bbox_test = '/home/vision/Repo/LUPerson/fast-reid/datasets/iust/bounding_box_test'
# bbox_train = '/home/vision/Repo/LUPerson/fast-reid/datasets/iust/bounding_box_train'
# query = '/home/vision/Repo/LUPerson/fast-reid/datasets/iust/query'

# # get ids from base_path directory(each id is a directory)
# def get_ids(base_path):
#     ids = []
#     for id in os.listdir(base_path):
#         ids.append(id)
#     return ids

# all_ids = get_ids(base_path)
# ids = []
# x = range(1, 103)
# for i in all_ids:
#     if int(i) not in x:
#         ids.append(i)
# # split ids into train and test(50%) sets based on odd and even indices
# # train_ids = ids[::2]
# # test_ids = ids[1::2]

# # get images from train_ids and test_ids. get one image from each camera
# # format of images like this: C#_F#_ID#.jpeg
# def get_images(ids, base_path):
#     images = {}
#     for id in ids:
#         images[id] = {}
#         for image in os.listdir(os.path.join(base_path, id)):
#             if image.split('_')[0] not in images[id]:
#                 images[id][image.split('_')[0]] = []
#             images[id][image.split('_')[0]].append(id + '/' + image)
#     return images

# train_images = get_images(ids, base_path)
# # test_images = get_images(ids, base_path)

# def copy_images(images, bbox_path, query_path=None):
#     for id in images:
#         for camera in images[id]:
#             images[id][camera].sort(key=lambda x: int(x.split('_')[1][1:]))
#             img_tmp = random.sample(images[id][camera], min(10, len(images[id][camera])))
#             for image in img_tmp:
#                 shutil.copyfile(os.path.join(base_path, image), os.path.join(bbox_path, image.split('/')[1]))
#             if query_path is not None:
#                 random_img = img_tmp[0]
#                 shutil.copyfile(os.path.join(base_path, random_img), os.path.join(query_path, random_img.split('/')[1]))


# copy_images(train_images, bbox_train)
# copy_images(test_images, bbox_test, query)




# base_path = '/home/vision/Repo/LUPerson/fast-reid/datasets/market1501/bounding_box_test'
# bbox_test = '/home/vision/Repo/LUPerson/fast-reid/datasets/market1501-2/bounding_box_test'
# bbox_train = '/home/vision/Repo/LUPerson/fast-reid/datasets/market1501-2/bounding_box_train'
# query = '/home/vision/Repo/LUPerson/fast-reid/datasets/market1501-2/query'

# def get_images(base_path):
#     images = {}
#     ids = []
#     for image in os.listdir(base_path):
#         if image.split('_')[0] != '0000' and image.split('_')[0] != '-1':
#             idd = image.split('_')[0]
#             if idd not in images:
#                 images[idd] = {}
#             if os.path.splitext(image)[1] == '.jpg':
#                 if image.split('_')[1][0:2] not in images[idd]:
#                     images[idd][image.split('_')[1][0:2]] = []
#                 images[idd][image.split('_')[1][0:2]].append(image)
#     return images

# test_images = get_images(base_path)
# def copy_images(images, bbox_path, query_path=None):
#     for id in images:
#         for camera in images[id]:
#             images[id][camera].sort(key=lambda x: int(x.split('_')[2]))
#             img_tmp = random.sample(images[id][camera], min(3, len(images[id][camera])))
#             for image in img_tmp:
#                 shutil.copyfile(os.path.join(base_path, image), os.path.join(bbox_path, image))
#             if query_path is not None:
#                 random_img = img_tmp[0]
#                 shutil.copyfile(os.path.join(base_path, random_img), os.path.join(query_path, random_img))

# copy_images(test_images, bbox_test, query)


base_path = '/home/vision/Repo/LUPerson/fast-reid/datasets/market1501/bounding_box_train'
bbox_train = '/home/vision/Repo/LUPerson/fast-reid/datasets/iust/bounding_box_train'

def copy_images(base_path, bbox_path):
    for image in os.listdir(base_path):
        if os.path.splitext(image)[1] == '.jpg':
            image_tmp = image.split('_')
            idd = 'ID' + str(int(image_tmp[0])+10000)
            cam = 'C' + image_tmp[1][1:2]
            frame = 'F' + str(int(image_tmp[2]))
            new_img_name = cam + '_' + frame + '_' + idd + '.jpeg'
            shutil.copyfile(os.path.join(base_path, image), os.path.join(bbox_path, image))
            shutil.move(os.path.join(bbox_path, image), os.path.join(bbox_path, new_img_name))

copy_images(base_path, bbox_train)