import cv2
import dropbox
import time
import random

startTime=time.time()

def take_snapshot():
    number=random.randint(0,100)

    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()

        img_name="securitySnap"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        startTime=time.time()
        result=False
        return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    accessToken="sl.BNCfxCpEtc6So1tPbdrzfgo1EuN7LI26ziheJO28H37ZcrZz_J9EIyAeE0QJWDXT_iQP4bBcA2u1RuhE7BGJ3KGu0ATHPOnPpVpchLsepm9_J6EvNcCyUuymM1SxkRehuFWOyes"
    file=img_name
    filefrom=file
    fileto="/newFolder/"+(img_name)
    dbx=dropbox.Dropbox(accessToken)
    with open(filefrom,'rb')as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while(True):
        if((time.time()-startTime)>=30):
            name=take_snapshot()
            uploadFile(name) 
main()       
