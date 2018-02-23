from django.core.files.storage import FileSystemStorage
import ipfsapi

import random
import string

class ipfsFile:
    
    def generate_random_name(self):
        
        return ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

    def __init__(self, files):
        
        file_name_1 = self.generate_random_name()
        file_name_2 = self.generate_random_name()
        
        #using apis as of now, will remove it.
        f = open('front_end/core/ipfs/temp_files/' + file_name_1, 'w')
        f.write(files[0])
        f.close()
        
        fs = FileSystemStorage(location='front_end/core/ipfs/temp_files/')
        fs.save(file_name_2, files[1])
        
        self.fileHash = []
            
        api = ipfsapi.connect('127.0.0.1', 5001)
        res = api.add('front_end/core/ipfs/temp_files/' + file_name_1)
        print res
        self.fileHash.append(res['Hash'])
        res = api.add('front_end/core/ipfs/temp_files/' + file_name_2)
        print res
        self.fileHash.append(res['Hash'])
        
        #pinning all files
        
            
            
    def return_hash(self):
        
        return self.fileHash