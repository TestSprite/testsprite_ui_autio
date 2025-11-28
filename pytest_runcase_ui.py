# -*- coding: utf-8 -*- 
# 姓名：李万伦
# 时间：2025/11/13  15:41
# 文件名：pytest_runapicase.py
import os
import shutil
import pytest

def test_shutil():
    # 指定目录路径（相对路径或绝对路径均可）
    dir_path = 'results'
    # 创建目录（如果已存在则不报错）
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        print(f"目录 '{dir_path}' 创建成功")
    else:
        print(f"目录 '{dir_path}' 已存在")
        # removing directory
        shutil.rmtree(dir_path)
if __name__ == "__main__":
    #清除results下面的数据
    test_shutil()
    #运行测试用例
    # 执行 pytest，指定 allure 结果目录 "--alluredir","results"
    pytest.main(['-vs', 'testcase', "--alluredir", "./results"])
    #生成allure报告
    os.system("allure generate ./results -o ./html --clean")