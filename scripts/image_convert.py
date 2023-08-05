from PIL import Image
import glob
import os, sys

images = [*glob.glob("gifs/*.gif")]

#size = (256,192)
size=(384,288)
#size=(256,256)

for i,fname in enumerate(images):
    fout = os.path.join('images',os.path.basename(fname)).replace('.gif', '.png')
    im = Image.open(fname)
    im = im.convert('RGB')
    if im.size != size:
        print('resizing', fname, 'to', size, 'was', im.size)
        im = im.resize(size)
    im.save(fout)
    im.close()
    sys.stderr.write("file %d of %d      \r"% (i, len(images)))

