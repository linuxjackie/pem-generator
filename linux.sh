#!/bin/bash
cd "$(dirname "$0")"
echo "檢查Python虛擬環境..."

if [ ! -f ".venv/bin/activate" ]; then
    echo "虛擬環境不存在,正在創建..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "創建虛擬環境失敗! 請確保您已安裝Python 3.x。"
        read -p "按Enter鍵繼續..." 
        exit 1
    fi
    echo "虛擬環境創建成功。"
fi

echo "啟動虛擬環境..."
source .venv/bin/activate
python3 pem_generator.py
deactivate
read -p "按Enter鍵繼續..." 