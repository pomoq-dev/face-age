import os

from PIL import Image


def convert_images(directory):
    file_names = os.listdir(directory)
    cnt = 0
    for file_name in file_names:
        if file_name.endswith('.jpeg') or file_name.endswith('.png') or file_name.endswith('.jpg'):
            print(file_name)
            just_name = '.'.join(file_name.split('.')[:-1])
            original_path = os.path.join(directory, file_name)
            img = Image.open(original_path)
            rgb_img = img.convert('RGB')
            rgb_img = rgb_img.resize((256, 256))
            res_name = 'hobana_image_{}'.format(cnt)
            cnt += 1
            res_path = os.path.join(directory, '{}.jpg'.format(res_name))
            rgb_img.save(res_path)
            if res_path != original_path:
                os.remove(os.path.join(directory, file_name))
