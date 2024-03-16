import fileinput
import re
def replace_string_in_file(file_path, pattern, replacement):
    try:
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                output = re.sub(pattern, replacement, line)
                print(output, end='')
        print(f"在文件 {file_path} 中成功替换了字符串")
    except Exception as e:
        print(f"在文件 {file_path} 中替换字符串时出现错误: {e}")