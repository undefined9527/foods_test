# foods-test

美食测试项目

## 环境要求

- Python >= 3.14

## 快速开始

```bash
# 创建并激活虚拟环境（Node.js 用户可用）
python -m venv .venv
.\.venv\Scripts\Activate

# 安装依赖
pip install requests python-dotenv

# 配置环境变量
copy .env.example .env
# 编辑 .env 填入实际配置

# 启动项目
python main.py
```

## 环境变量

参考 `.env.example` 文件配置所需的环境变量。

## 项目结构

```
foods_test/
├── .env.example      # 环境变量模板
├── .gitignore        # Git 忽略文件
├── .venv/            # Python 虚拟环境（不提交）
├── main.py           # 项目入口
├── package.json      # Node.js 配置（可选）
└── README.md         # 本文件
```
