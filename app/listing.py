import os

def list_all():
    rootdir= os.getcwd()
    dir= rootdir+"/app/static/uploads"
    print dir
    return os.listdir(dir)
    
    # for subdir, dirs, files in os.walk(rootdir+"/app/static/uploads"):
    #     for file in files:
    #         return os.path.join(subdir, file)
            
        

    