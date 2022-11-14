Python单元测试示例
---

# 一、简介
## 1. 项目介绍
一个简单的博客系统，包含：
- 创建文章
- 获取文章
- 获取文章列表

## 2. 关键技术
- Flask，web框架
- SQLite，数据库
- pytest，单元测试框架
- pydantic，数据校验

# 二、运行
## 1. 根据requirements.txt安装对应依赖 
```shell script
pip3 install -r requirements.txt
```

## 2. 初始化数据库
```shell script
python3 src/blog/init_db.py
```

## 3. 本地运行
直接在IDE运行，或者通过命令`FLASK_APP=blog/app.py python3 -m flask run`运行：
```shell script
$ FLASK_APP=src/blog/app.py python3 -m flask run
 * Serving Flask app "src/blog/app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

访问网站`http://localhost:5000/article-list/`

## 4. 运行测试
`python3 -m pytest src/tests`

```shell script
$ python3 -m pytest src/tests
================================================================= test session starts ==================================================================
platform darwin -- Python 3.8.3, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/yukki/Downloads/Project/python-ut
plugins: metadata-1.11.0, html-3.1.1
collected 11 items                                                                                                                                     

src/tests/blog/test_app.py ......                                                                                                                [ 54%]
src/tests/blog/test_commands.py ...                                                                                                              [ 81%]
src/tests/blog/test_queries.py ..                                                                                                                [100%]

================================================================== 11 passed in 0.18s ==================================================================
```

# 参考
* [Modern Test-Driven Development in Python](https://testdriven.io/blog/modern-tdd/#when-should-you-use-mocks)