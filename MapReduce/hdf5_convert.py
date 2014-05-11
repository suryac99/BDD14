import iopro
import tables as tb
import numpy as np
from itertools import islice
from cStringIO import StringIO
import gzip
import os

for fgz in os.listdir('./'):
    if fgz.endswith('.gz'):
        print fgz
        name = fgz.split('.')
        datetime = name[0][12:]
        FILE = fgz
        SCHEMA = [
            ('project code', '|S5'),
            ('file', '|S20'),
            ('views', 'i4'),
            ('bytes', 'i8')
        ]

        f = gzip.GzipFile(FILE, "r")
        line = f.readline()
        values = np.genfromtxt(StringIO(line), dtype=SCHEMA, delimiter=' ')
        values.shape=1


        h5File = name[0]+'.h5'
        h5 = tb.openFile(h5File, 'w')
        table = h5.createTable(h5.root, description=values, name='wiki_log-'+datetime, title="wiki_log")
        table.flush()

        count = 0

        POINTS = 200000000
        while True:
            values = np.genfromtxt(islice(f, 500), dtype=SCHEMA, delimiter=' ')
            #values.shape = 500
            table.append(values)
            count += 500
            print '%0.2f %%' % round(((1.0*count) / POINTS)*100, 2)
            #print '\tlength: ', len(values)
            if count > POINTS or (len(values) == 0):
                break
                print 'Done'

        table.flush()
        h5.flush()
        h5.close()
        f.close()


# import h5py
# import numpy as np
# import pandas as pd

# h5File = 'pagecounts-20130501-010000.h5'
# file_hdf5 = h5py.File(h5File, 'r')
# keys = file_hdf5.keys()[0]

# data = file_hdf5[keys]['project_code','views']
# df = pd.DataFrame(data)
