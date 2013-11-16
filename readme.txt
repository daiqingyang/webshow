1、主要程序在webshow\home目录，静态文件在webshow\templates目录。
2、需要更改webshow\webshow\settings里面的数据库设置，并在数据库中添加相应的库。
更改后运行manage.py sqlall生产建表语句，运行manage.py syncdb同步到数据库。
3、需要在后台管理的Add classs表里面插入课程和自定义的邀请码。（http://192.168.1.9:8000/admin/）
ClassName:（课程名字）
Invate key:（课程唯一邀请码）
CanRegister:(是否允许注册，当学员注册完毕后，可以关闭此项，禁止他人注册成为该类）
4、学员凭唯一邀请码注册成为相应课程的学员。
5、需要在后台管理的Add classs表里面插入admins和自定义的邀请码
ClassName: admins
Invate key: xxxx
CanRegister:(是否允许注册，关闭此项，禁止他人注册成为该类）
6、注册成为admins类的成员，在首页登录后的导航里有查看签到报表的链接。

7、如果想部署到apache按照下面步骤就可以，如果不想，那就直接./manage.py runserver 0.0.0.0:80.
1）安装wsgi_module
2）配置httpd.conf
LoadModule wsgi_module modules/mod_wsgi.so
WSGIScriptAlias / /your/path/webshow/django.wsgi

<Directory /your/path/webshow/>
    AllowOverride None
    Options FollowSymLinks
    Order allow,deny
    Allow from all
</Directory>
Alias /static/ /your/path/webshow/templates/