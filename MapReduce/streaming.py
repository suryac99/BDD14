import os
import re
import sys

# determine value of n in the current block of ngrams by parsing the filename
input_file = os.environ['map_input_file']
#expected_tokens = int(re.findall(r'([\d]+)gram', os.path.basename(input_file))[0])

for line in sys.stdin:
    data = line.split()

    
    for d in data:
        print >>sys.stdout, "%s\t%s" % (str(d)+''.join(sys.path), 1)



subprocess.call("hadoop fs -put ./test.txt /tmp/test_files/"+fname, shell=True)
hadoop fs -put ./checkov.txt /tmp/checkov-2.txt