"""foods-test 项目入口"""

import os
from dotenv import load_dotenv


def main():
    # 加载 .env 环境变量
    load_dotenv()

    app_name = os.getenv("APP_NAME", "foods-test")
    env = os.getenv("APP_ENV", "development")
    port = os.getenv("APP_PORT", "3000")

    print(f"===== {app_name} =====")
    print(f"Environment: {env}")
    print(f"Port: {port}")

    # 示例：使用 requests 请求 API
    try:
        import requests
        print("\n[requests 库可用]")
        resp = requests.get("https://httpbin.org/get", timeout=5)
        print(f"HTTP Status: {resp.status_code}")
    except Exception as e:
        print(f"\nNetwork error: {e}")

    print("\nApp is running...")


if __name__ == "__main__":
    main()
