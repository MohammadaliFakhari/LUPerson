import os
import os.path as osp
import re
import warnings

from .bases import ImageDataset
from ..datasets import DATASET_REGISTRY


@DATASET_REGISTRY.register()
class FruitShop(ImageDataset):
    dataset_name = "fruitshop"
    dataset_dir = ''
    def __init__(self, root='datasets', **kwargs):
        self.root = root
        self.dataset_dir = osp.join(self.root, self.dataset_dir)

        self.data_dir = self.dataset_dir
        data_dir = osp.join(self.data_dir, 'fruitshop')
        if osp.isdir(data_dir):
            self.data_dir = data_dir
        else:
            warnings.warn('The current data structure is deprecated. Please '
                          'put data folders such as "bounding_box_train" under '
                          '"fruitshop".')

        self.train_dir = osp.join(self.data_dir, 'bounding_box_train')
        self.query_dir = osp.join(self.data_dir, 'query')
        self.gallery_dir = osp.join(self.data_dir, 'bounding_box_test')

        required_files = [
            self.data_dir,
            self.train_dir,
            self.query_dir,
            self.gallery_dir,
        ]
        self.check_before_run(required_files)
        train = self.process_dir(self.train_dir)
        query = self.process_dir(self.query_dir, is_train=False)
        gallery = self.process_dir(self.gallery_dir, is_train=False)

        super(FruitShop, self).__init__(train, query, gallery, **kwargs)


    def process_dir(self, dir_path, is_train=True):
        img_paths = os.listdir(dir_path)
        data = []

        for img_path in img_paths:
            camid = img_path.split('_')[0][1:]
            pid = img_path.split('_')[2].removesuffix('.jpeg')[2:]

            if is_train:
                pid = self.dataset_name + "_" + str(pid)
                camid = self.dataset_name + "_" + str(camid)
            data.append((img_path, pid, camid))

        return data
