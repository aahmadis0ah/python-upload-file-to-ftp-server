__author__ = 'ahc0d3r'

from ftplib import FTP
import os
import shutil
def connect(server=None,username=None,password=None):
    try:
        ftp=FTP(server)
        ftp.login(username,password)
        return ftp
    except:
        import traceback
        print traceback.print_exc()

def upload_all_files(topdir,ftp):
    outdir=ftp.pwd()+"/"
    for path,files,dirs in os.walk(topdir):
        print (outdir+"your dir"+path[23:]).replace("/","//")
        ftp.mkd((outdir+"your dir"+path[23:]).replace("/","//"))
        ftp.cwd((outdir+"your dir"+path[23:]).replace("/","//"))

        #os.mkdir("/home/s01ah/Desktop/"+"your dir"+path[23:])

        for file in dirs:
            #shutil.copy(path+"/"+file,"/home/ahc0d3r/Desktop/"+"your dir"+path[23:]+"/"+file)
            f=open(path+"/"+file,"rb")
            print "uploading "+file+"    file"
            ftp.storbinary('STOR '+file,f)
            f.close()



def main():
    ftp=connect("127.0.0.1","ahc0d3r","aaaaaaaaa") #connecting to localhost ftp server
    if ftp !=None:
        print("connected to ftp server!\n")
        #upload_all_files("/home/s01ah/phproot/pio",ftp)
        ftp.mkd ((ftp.pwd()+"httpdocs/server sub dir").replace("/","//"))
        print "Please Wait ......\n"

    else:
        print("exception occur in network try again")
if __name__=="__main__":
    main()




