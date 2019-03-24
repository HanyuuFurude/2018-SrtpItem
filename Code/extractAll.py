import os
import gzip
import re
print('[start to unzip files]')
count = 0
countFiled = 0
for folder, subfolders, files in os.walk('.\\'):
    for f in files:
        # file type filter
        if re.search('(.*).gz$', f):
            # these statement was disabeld for you can use os.path.join() to repalce them
            # res = str(folder + ('/' if folder is not './' else '') + f)
            # res = re.sub('\\\\', '/', res)
            res = os.path.join(folder,f)
            print('[find file]', res)
            # unzip files
            try:
                with gzip.open(res, 'rb') as input:
                    inputContent=input.read()
                    output = res.replace('.gz', '')
                    size = len(inputContent)
                    with open(output, 'wb') as o:
                        o.write(inputContent)
                    print('[unzip successfully]', output, '\t[size]', size)
                    count+=1
            except Exception as e:
                print(e)
                print('[file unzip failed]')
                countFiled+=1
print('[unzip files finished]',count,'file(s) unziped successfully and',countFiled,' filed.')
