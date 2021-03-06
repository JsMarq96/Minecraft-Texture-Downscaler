#!/usr/bin/env python3

from Img_Resizer import CMODE, img_compress
from DirectoryTransversal import file_search
from multiprocessing import Pool, cpu_count
from PIL import Image


def resize_img(file_dir):
    img_compress(file_dir[0], file_dir[1])
    #imgs = Image.open(file_dir)
    #imgs.quantize(256, method=3, dither=0).save(file_dir)

       
def resize(pack_dir='.', file_term={}):
    file_dirs = file_search(('.png'), pack_dir)
    file_dirs_tuple= []

    for f_dir in file_dirs:
        type_data = file_term['COLOR']

        file_dirs_tuple.append((f_dir, type_data))
        #Image.open(f_dir).quantize(256, method=2, dither=0)

    #print(file_dirs_tuple[0:20])
    #for f_dir in file_dirs_tuple:
    #   resize_img(f_dir)
   

    with Pool(processes=cpu_count()) as pool:
        pool.map(resize_img, file_dirs_tuple)



if __name__ == '__main__':
    file_modes = { 'COLOR': CMODE.LIGHT,
                   'NORM': CMODE.LIGHT,
                   'SPEC':CMODE.HEAVY
                  }
    resize('/home/js/.minecraft/resourcepacks/NAPP_1024x_1.4.1_red/assets/minecraft', file_modes)
    print('finished')
