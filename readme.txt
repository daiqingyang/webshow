1����Ҫ������webshow\homeĿ¼����̬�ļ���webshow\templatesĿ¼��
2����Ҫ����webshow\webshow\settings��������ݿ����ã��������ݿ��������Ӧ�Ŀ⡣
���ĺ�����manage.py sqlall����������䣬����manage.py syncdbͬ�������ݿ⡣
3����Ҫ�ں�̨�����Add classs���������γ̺��Զ���������롣��http://192.168.1.9:8000/admin/��
ClassName:���γ����֣�
Invate key:���γ�Ψһ�����룩
CanRegister:(�Ƿ�����ע�ᣬ��ѧԱע����Ϻ󣬿��Թرմ����ֹ����ע���Ϊ���ࣩ
4��ѧԱƾΨһ������ע���Ϊ��Ӧ�γ̵�ѧԱ��
5����Ҫ�ں�̨�����Add classs���������admins���Զ����������
ClassName: admins
Invate key: xxxx
CanRegister:(�Ƿ�����ע�ᣬ�رմ����ֹ����ע���Ϊ���ࣩ
6��ע���Ϊadmins��ĳ�Ա������ҳ��¼��ĵ������в鿴ǩ����������ӡ�

7������벿��apache�������沽��Ϳ��ԣ�������룬�Ǿ�ֱ��./manage.py runserver 0.0.0.0:80.
1����װwsgi_module
2������httpd.conf
LoadModule wsgi_module modules/mod_wsgi.so
WSGIScriptAlias / /your/path/webshow/django.wsgi

<Directory /your/path/webshow/>
    AllowOverride None
    Options FollowSymLinks
    Order allow,deny
    Allow from all
</Directory>
Alias /static/ /your/path/webshow/templates/