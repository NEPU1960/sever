#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: manage.py.py
@time: 2019/3/6 0006 14:40
@desc:
"""
#!/usr/bin/python
# -*- coding:utf-8 -*-:
'''
@author: qkyzs
@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.
@contact: nepu1960@yeah.net
@file: wechat_get.py
@time: 2019/1/20 22:52
@desc:
'''
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

#app.config.from_object('main.config')
#app.config.from_pyfile('config.py')
from main import db,create_app

app=create_app()
db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# def make_shell_context():
#     return dict(app=app, db=db)
#     manager.add_command("shell",Shell(make_context=make_shell_context))
#     manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
