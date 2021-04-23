'''
    Định nghĩa một class có ít nhất 2 method: 
    getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
    printString: in chuỗi vừa nhập sang chữ hoa. 
    Thêm vào các hàm kiểm tra đơn giản để kiểm tra method của class.
    Ví dụ: Chuỗi nhập vào là weatherplus.vn thì đầu ra phải là: WEATHERPLUS.VN
'''
class Change:
    def __init__ (self,stringIn):
        self.stringOut=stringIn
    def getString(self):
        return self.stringOut.upper()
    def printString(self):
        print(self.getString())
n=input('Enter string input:')
c1=Change(n)
c1.printString()