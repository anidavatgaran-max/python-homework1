'''a=input('رشته را وارد کنید:')
for i in range(len(a)-10,len(a)):
   print(a[i],end='')'''


'''m=input('شماره موبایل را وارد کنید:')
for i in range(4):
    print(m[i],end='')'''
    
    
'''n=input('نام و نام خانوادگی را وارد کنید:')
x=n.index(' ')
print(n[0]+'.',end='')
for i in range(x+1,len(n)):
    print(n[i],end='')'''
    
    
'''t=input('شماره حساب بانکی را وارد کنید:')
x=len(t)-1
for i in range(x, -1, -1):
    print(t[i],end='')'''
    
    
'''d=float(input('مسافت طی شده را وارد کنید:'))
if d<=2:
    f=20000    
else:
    f=20000+((d-2)*5000)
print(f)'''


'''p=int(input('قیمت را وارد کنید:'))
if 500000 <=p<= 1000000:
    x=p*0.9
    print(x)'''
    
    
'''c=input('شماره کارت را وارد کنید:')
p=c[:4]
if p =='6037':
    print('بانک فرضی')
else:
    print('بانک شناسایی نشد')'''
    
    
'''h=int(input('ساعت را وارد کنید:'))
if h<0 or h>23:
    print('خطا')
elif h<12:
    print('صبح')
elif h==12:
    print('ظهر')
elif h>12 and h<17:
    print('بعد از ظهر')
elif h>17 and h<20:
    print('عصر')
elif h>20 and h<23:
    print('شب')'''