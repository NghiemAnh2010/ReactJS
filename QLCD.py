# -----------------------------------------------------------
#Cafedev.vn - Kênh thông tin IT hàng đầu Việt Nam
#@author cafedevn
#Contact: cafedevn@gmail.com
#Fanpage: https://www.facebook.com/cafedevn
#Group: https://www.facebook.com/groups/cafedev.vn/
#Instagram: https://instagram.com/cafedevn
#Twitter: https://twitter.com/CafedeVn
#Linkedin: https://www.linkedin.com/in/cafe-dev-407054199/
#Pinterest: https://www.pinterest.com/cafedevvn/
#YouTube: https://www.youtube.com/channel/UCE7zpY_SlHGEgo67pHxqIoA/
# -----------------------------------------------------------

from thuvien.XL_CD import *
tt=1
DSCD=[]
while tt==1:
    TenCD=input('Nhap Ten CD\t')
    TenCaSi=input('Nhap Ten ca si\t')
    SoBaiHat=int(input('Nhap Bai hat\t'))
    GiaTien=eval(input('Nhap Gia tien\t'))
    cd = XL_CD(TenCD,TenCaSi,SoBaiHat,GiaTien)
    DSCD.append(cd)
    tt=int(input('NHap so 1 de tiep tuc'))
tongtien=0
for cd in DSCD:
    print(cd.TenCD)
    print(cd.TenCaSi)
    print(cd.SoBaiHat)
    print(cd.GiaTien)
    print('=============================================')
    tongtien+=cd.GiaTien
print("Tong tien : " + str(tongtien))
