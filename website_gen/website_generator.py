import glob
import os

this_folder = os.path.dirname(__file__)

text = '''<p><strong>Testowy projekt.</strong></p>\n
<p>Ta strona zawiera przykładowy projekt pythonowy.<br /></p>\n'''


wheels = glob.glob(os.path.join(this_folder, '..', 'dist', '*.whl'))

for i in wheels:
   add = '<p><a title="Latest_release" href="./{}">Latest_release</a></p>'.format(os.path.basename(i))
   wheels = text + '\n' + add
print(wheels)
