from db import db_handler


class Admin:
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def create_school(self):
		pass

	def create_teacher(self):
		pass

	def create_course(self):
		pass


def register_interface(username, password):
	admin_db = db_handler.load_pickle(username)
	if admin_db:
		return False, '用户已存在，请更换用户名或用已有账户登录'
	admin = Admin(username, password)
	# print(admin.)
	db_handler.save_pickle(username, admin)
	return True, f'管理员{username}注册成功'


# print(register_interface('admin','123456'))

def login_interface(username, password):
	admin_db = db_handler.load_pickle(username)
	if admin_db.password == password:
		return True, f'{username}登陆成功'
	else:
		return False, '密码或账号错误'
