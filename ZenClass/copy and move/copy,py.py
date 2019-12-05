import shutil
src=input("enter the source path:")
dst=input("enter the destination path:")
print("1.move 2.copy")
c=int(input())
if c ==1:
    shutil.move(src,dst)
if c ==2:
    shutil.copyfile(src, dst)  
