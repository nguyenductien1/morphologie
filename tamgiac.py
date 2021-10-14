import math

def khoang_cach(x1, y1, x2, y2):
    kc = math.sqrt((float(x1)-float(x2))**2 + (float(y1) - float(y2))**2)
    return kc


def tinh_chu_vi(x_run:float = 0, y_run:float = 0, x:float = 0 , y:float = 0, cv:float = 0, list_x:list = [], list_y:list = []):
 

    x = input("nhap x: "); y = input("nhap y: ")
    
    list_x.append(x)
    list_y.append(y)

    if x=='' or y=='':
        if len(list_x) < 2 or len(list_y) < 2:
            print("Phai dien nhieu hon 2 diem")
        else:
            cv = cv + khoang_cach(float(list_x[0]),float(list_y[0]),float(list_x[-1]),float(list_y[-1]))
        print("Chu vi la: ", cv)
    else:
        if len(list_x) < 2 or len(list_y) < 2:
            cv = cv + 0
            tinh_chu_vi(float(x_run), float(y_run), float(x), float(y), cv, list_x, list_y)
            x_run = x
            x_run = y
        else:
            cv = cv + khoang_cach(float(x), float(y), float(x_run), float(y_run))
            tinh_chu_vi(float(x_run), float(y_run), float(x), float(y), cv, list_x, list_y)
            x_run = x
            x_run = y
tinh_chu_vi()