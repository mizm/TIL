import os
# os import
# 해당 폴더
# 폴더안에 모든 파일을 돌며 이름바꾸기

os.chdir(r'C:\Users\student\work\day02\dummy')
#print(os.getcwd())
for filename in os.listdir('.'):
    os.rename(filename,filename.replace("지원서","합격자"))
