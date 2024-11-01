from MyQR import myqr
ver,level,qr_name = myqr.run(words='https://i.csdn.net/#/user-center/profile')#一行代码生成二维码
print(ver,level,qr_name)#保存二维码于文件夹中