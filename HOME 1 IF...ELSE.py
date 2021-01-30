import random
comodity = input('enter good name')
goodcode = eval(input('please input good code to know the price'))
cake = 1
milk = 2
flour = 3
jik = 4
mandazi = 5
egg = 6
sweet = 7
book = 8
pen = 9
ndovu = 9.1
if comodity == (cake or milk or flour or jik or mandazi or egg or sweet or book or pen or ndovu):
  if goodcode >= 1 and goodcode < 10:
    print('the price is: sh.')
     if goodcode == 1:
        print('100')
     elif goodcode == 2:
        print('50')
     elif goodcode == 3:
        print('110')
     elif goodcode == 4:
        print('80')
     elif goodcode == 5:
        print('10')
     elif goodcode == 6:
        print('15')
     elif goodcode == 7:
        print('5')
     elif goodcode == 8:
        print('25')
     elif goodcode == 9:
        print('20')
     elif goodcode > 9:
        print('130')
     else:
        print('invalid good entry, try again')
else:
    print('invalid good name please try again')