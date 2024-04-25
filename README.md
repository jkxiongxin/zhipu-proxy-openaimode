# zhipu-proxy-openaimode

# 目的
经过对比，智谱ai的api是目前最便宜的人工智能api之一。由于市面上大多数开源软件只对openai模式的接口进行了支持，所以为了方便本人对各种支持openai模式的软件进行使用，开发了本项目。

## 启动

1. 安装python3.8及其以上版本
2. 创建python运行环境
```shell
python -m venv venv
```
3. 加载python运行环境
```shell
source ./venv/bin/activate
```
4. 安装智谱ai库，`flask`以及`flask_cors`
```shell
pip install zhipuai
pip install flask
pip install flask_cors
```
5. 在`zhipu.py`文件中找到`client = ZhipuAI(api_key="")`这一行，填入在智谱ai控制台中取到的apikey。[智谱ai控制台](https://open.bigmodel.cn/usercenter/apikeys)

6. 启动服务
```shell
python zhipu.py
```