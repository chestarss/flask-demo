## 核心思想
*controller* 和 *model* 在定义时均没有绑定任何配置数据
<p>
所有的配置都是在flask app创建之后调用init_api 和 init_db关联 flsak和restful api和sqlalchemy db的,这样做的好处就是可以复用model，而不需要依赖app
</p>

## 文件结构
<pre><code>
├── app.py
├── config
│   ├── config.py
│   └── __init__.py
├── controller
│   ├── common.py
│   ├── controller.py
│   ├── __init__.py
│   ├── server.py
│   └── user.py
├── init_db.py
├── model
│   ├── __init__.py
│   ├── model.py
│   └── test_model.py
├── README.md
├── requirement.txt
└── runserver.py
</code></pre>

## 启动
<pre><code>
pip install -r requirement.txt
python runserver.py
</code></pre>

##扩展
<p>
todo:
权限控制:Flask-RBAC
登录：Flask-Login
任务执行框架:celery  定时任务，异步执行，并发执行
</p>
