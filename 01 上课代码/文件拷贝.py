
def copy_file(scr, dest):
    try:
        with open(f"{scr}.txt", 'rb') as scr_file:
            with open(f"{dest}.txt", 'wb') as dest_file:
                dest_file.write(scr_file.read())
            print(f"文件 {scr} 已成功复制到 {dest}")

    except Exception as e:
        print(f"复制文件时出现错误: {e}")