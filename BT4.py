'''
    Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. Viết chương 
trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.
Các tiêu chí kiểm tra mật khẩu bao gồm:
1. Ít nhất 1 chữ cái nằm trong [a-z]
2. Ít nhất 1 số nằm trong [0-9]
3. Ít nhất 1 kí tự nằm trong [A-Z]
4. Ít nhất 1 ký tự nằm trong [$ # @]
5. Độ dài mật khẩu tối thiểu: 6
6. Độ dài mật khẩu tối đa: 12
Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không.
Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345
Thì đầu ra sẽ là: ABd1234@1
'''
from BT4_module import*
print('{:=>35}S'.format('* Sign In *')+'{:=<28}'.format(' '))

n=input('Enter your password: ')
n1=n.split(',')
for i in range(len(n1)):
    if check_lenght(n1[i])==1 and check_az(n1[i])==1 and check_AZ(n1[i])==1 and check_09(n1[i])==1 and check_char(n1[i]):
            print(n1[i])
    


