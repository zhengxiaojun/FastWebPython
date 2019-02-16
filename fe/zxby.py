# zxby.py
# -*- coding: utf-8 -*-

import os, sys, subprocess, tempfile, time, io
import json

# 创建临时文件夹,返回临时文件夹路径
# TempFile = tempfile.mkdtemp(suffix='_test', prefix='python_')
TempFile = os.path.dirname(os.path.realpath(__file__)) + "/tmp"

# 文件名
FileNum = int(time.time() * 1000)
# python编译器位置
EXEC = sys.executable


# 获取python版本
def get_version():
    v = sys.version_info
    version = "python %s.%s.%s" % (v.major, v.minor, v.micro)
    return version


# 获得py文件名
def get_pyname():
    global FileNum
    return 'test_%d' % FileNum


# 接收代码写入文件
def write_file(pyname, code, version):
    fpath = os.path.join(TempFile, '%s.py' % pyname)
    with io.open(fpath, 'w', encoding='utf-8') as f:
        if version == 2:
            f.write(unicode(code, "utf-8"))
        if version == 3:
            f.write(str(code, encoding='utf-8'))
    # print('file path: %s' % fpath)
    return fpath


# 编码
def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')


# 主执行函数
def main(code):
    r = dict()
    r["version"] = get_version()
    ver = sys.version_info.major
    pyname = get_pyname()
    fpath = write_file(pyname, code, ver)
    try:
        # subprocess.check_output 是 父进程等待子进程完成，返回子进程向标准输出的输出结果
        # stderr是标准输出的类型
        outdata = decode(subprocess.check_output([EXEC, fpath], stderr=subprocess.STDOUT))
    except subprocess.CalledProcessError as e:
        # e.output是错误信息标准输出
        # 错误返回的数据
        r["status"] = 'Error'
        r["output"] = decode(e.output)
    else:
        # 成功返回的数据
        r['output'] = outdata
        r["status"] = "Success"
    finally:
        # 删除文件(其实不用删除临时文件会自动删除)
        try:
            os.remove(fpath)
        except Exception as e:
            exit(1)
    if ver == 2:
        r = json.dumps(r, ensure_ascii=False, indent=4, encoding="utf-8")
    if ver == 3:
        r = json.dumps(r, ensure_ascii=False, indent=4)
    return r


if __name__ == '__main__':
    pass
