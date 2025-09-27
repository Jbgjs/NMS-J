#!/bin/bash

echo "elimNMS Server Starting..."
echo "elimNMS 서버를 시작합니다..."

# 스크립트가 있는 디렉터리로 이동
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/elimNMS-public"

echo "Starting Flask application..."
"$SCRIPT_DIR/.venv/bin/python" app.py

echo ""
echo "Server has stopped. Press Enter to exit..."
read
