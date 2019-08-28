from interface import admin_interface

admin_info = {
	'admin': None
}


def admin_register():
	while True:
		username = input('请输入您想注册的账号').strip()
		password = input('请输入您想注册的密码').strip()
		re_password = input('请再次输入您想注册的密码').strip()
		if password == re_password:
			flag, msg = admin_interface.register_interface(username, password)
			print(msg)
			if flag:
				break
		else:
			print('两次密码输入不一致，请重新输入')
			continue


# admin_register()


def admin_login():
	while True:
		if admin_info['admin']:
			print('已有账户在登录，请注销后再登录')
			break
		username = input('请输入您的账号').strip()
		password = input('请输入您的密码').strip()
		flag, msg = admin_interface.login_interface(username, password)
		print(msg)
		if flag:
			admin_info['admin'] = username
			break


def create_school():
	pass


def create_teacher():
	pass


def creat_course():
	pass


ADMIN_MSG = ('''
	1. 注册
	2. 登录
	3. 创建学校
	4. 创建老师
	5. 创建课程
	''')

ADMIN_DIC = {
	'1': admin_register,
	'2': admin_login,
	'3': create_school,
	'4': create_teacher,
	'5': creat_course
}


def enter_admin():
	while True:
		print(ADMIN_MSG)

		choice = input('欢迎来到管理员界面，请选择您需要的功能的编号，q退出').strip()

		if choice == 'q':
			break
		if choice not in ADMIN_DIC:
			print('没有这个功能，请重新选择')
			continue
		ADMIN_DIC[choice]()
enter_admin()