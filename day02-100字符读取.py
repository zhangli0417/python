"""
    每次100字符读取，主目录下 examples.desktop 文件内容，并打印出来
"""
f = open("/home/tarena/examples.desktop", "r")
while True:
    s = f.read(100)
    if not s: break
    print(s, end="")
