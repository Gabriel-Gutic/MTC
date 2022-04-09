import zipfile


def read_default_texture(path):
    archive = zipfile.ZipFile(path, 'r')
    
    files = archive.namelist()
    
    images = []
    for file in files:
        if file.endswith('.png'):
            images.append(file)
    return images
        

