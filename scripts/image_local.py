import csv
import os
import urllib.request
from PIL import Image
import io
import sys

data = []

names = set()

basedir = 'gifs'

local_source_dir = 'kartoteka/media/s'

sources = set([e for e in os.scandir(local_source_dir)])
print(f'found {len(sources)} screens in {local_source_dir}')
for src in sources:
    id = os.path.splitext(os.path.basename(src.name))[0]
    fname = basedir + '/'+ id + '.gif'
    data.append((id, fname, os.path.normpath(src), 'localfile'))

existing = set([e.name for e in os.scandir(basedir)])

total = len( names )
count = len( existing )

for i, (id, fname, srcpath, title) in enumerate(data):
    if not os.path.exists(fname):
        with open(srcpath, 'rb') as srcfile:
            buf = srcfile.read()

        sys.stderr.write('writing file %d of %d %s\r' % (count, total, fname.ljust(60)))
        count += 1

        if srcpath.endswith('.png') or srcpath.endswith('.jpg') or srcpath.endswith('.gif'):
            im = Image.open(io.BytesIO(buf))
            
            im = im.resize((384,288), Image.Resampling.NEAREST)
            im.thumbnail((384,288), Image.Resampling.NEAREST)
            p_img = Image.new('P', im.size)
            im = im.convert('RGB')
            im = im.quantize()

            b = io.BytesIO()
            im.save(b, 'gif')
            buf = b.getvalue()

        f = open(fname,'wb')
        f.write(buf)
        f.close()



