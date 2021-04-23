'''
Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là string, age và height là number. Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp là:

Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là tên > tuổi > điểm.
Nếu đầu vào là:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

Thì đầu ra sẽ là:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''
try:
    n=int(input('Nhap so luong nguoi muon so sanh:'))
    list1=[]
    for i in range(n):
        print('Nhap thong tin nguoi thu{}:'.format(i))
        a=str(input('Nhap ten :'))
        b=int(input('Nhap tuoi:'))
        c=int(input('Nhap diem:'))
        list1+=[(a,b,c)]
except:
    print('Dinh dang dau vao ko hop le!!!')
# List khi chưa sxep
print(list1)
# Sap xếp với key nhận 1 tuple
#idea1=lambda tup : (tup[0],tup[1],tup[2])
#new_list=sorted(list1,key=idea1)
#print(new_list)

# Sxep với key nhận operator.itemgetter
from operator import itemgetter
new_list1=sorted(list1,key=itemgetter(0,1,2))
print(new_list1)

