import pygame as py
from os import walk


def import_folder(path):

    surface_list = []
    for _,_,img_file in walk(path):
        for image in img_file:
            full_path = path + '/' + image
            img_surface =  py.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
    
    return surface_list

