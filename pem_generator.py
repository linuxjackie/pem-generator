#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PEM Key Generator
Version: 1.0.0
Author: CodeBear
"""

import os
import sys
import subprocess
import argparse
import platform
from OpenSSL import crypto

__version__ = "1.0.0"


def generate_pem_key(filename=None, use_password=False, key_size=2048):
    """
    生成PEM密鑰文件
    
    參數:
        filename (str, optional): 輸出文件名。如果未提供,將通過交互方式詢問用戶。
        use_password (bool): 是否使用密碼保護密鑰。
        key_size (int): 密鑰位數大小。
    """
    # 如果未提供文件名,則詢問用戶
    if not filename:
        filename = input("請輸入PEM文件名稱(不含副檔名):")
        filename = filename.strip()
        if not filename:
            print("錯誤: 文件名不能為空。")
            return False
    
    # 確保有.pem副檔名
    if not filename.endswith(".pem"):
        filename = filename + ".pem"

    # 檢查文件是否已存在
    if os.path.exists(filename):
        print(f"錯誤: 文件 '{filename}' 已存在。請選擇另一個名稱。")
        return False

    try:
        # 生成密鑰對
        key = crypto.PKey()
        key.generate_key(crypto.TYPE_RSA, key_size)
        
        # 如果需要密碼保護
        if use_password:
            print("請輸入密碼來保護您的密鑰文件:")
            password = input("密碼: ").encode('utf-8')
            pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, key, 'des3', password)
        else:
            pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, key)

        # 寫入文件
        with open(filename, 'wb') as f:
            f.write(pem)

        print(f"PEM密鑰已成功生成並保存到 '{filename}'")

        # 設置文件權限,僅所有者可讀寫
        try:
            if platform.system() != "Windows":
                os.chmod(filename, 0o600)
                print("文件權限已設置為僅所有者可讀寫(600)。")
        except Exception as e:
            print(f"警告: 無法設置文件權限: {e}")
            print("請手動確保文件的安全。")

        return True

    except Exception as e:
        print(f"生成密鑰時出錯: {str(e)}")
        # 如果文件已創建,嘗試刪除
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print(f"已刪除部分創建的文件 '{filename}'")
            except:
                print(f"警告: 無法刪除部分創建的文件 '{filename}'")
        return False


def main():
    """
    主函數,處理命令行參數並運行程序
    """
    # 創建命令行參數解析器
    parser = argparse.ArgumentParser(
        description="生成PEM格式的RSA密鑰文件",
        epilog="示例: python pem_generator.py --filename my_key.pem --password --size 4096"
    )
    
    # 添加參數
    parser.add_argument("-f", "--filename", 
                        help="輸出PEM文件的名稱(可選,如未提供將通過交互方式詢問)")
    parser.add_argument("-p", "--password", action="store_true", 
                        help="使用密碼保護密鑰(預設為否)")
    parser.add_argument("-s", "--size", type=int, default=2048, 
                        choices=[1024, 2048, 4096], 
                        help="密鑰大小(位),預設為2048")
    parser.add_argument("-v", "--version", action="version", 
                        version=f"PEM Key Generator v{__version__}")
    
    # 解析命令行參數
    args = parser.parse_args()
    
    # 運行生成函數
    success = generate_pem_key(
        filename=args.filename,
        use_password=args.password,
        key_size=args.size
    )
    
    # 根據結果設置退出碼
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n程序已被用戶中斷。")
        sys.exit(1)
    except Exception as e:
        print(f"程序錯誤: {e}")
        sys.exit(1)
