import os
import pickle
from confs import settings


# 保存pickle文件
def save_pickle(username, data):
	user_path = os.path.join(settings.DB_PATH, f'{username}.pk')
	with open(user_path, 'wb')as fw:
		pickle.dump(data, fw)
		fw.flush()


# 读取pickle文件
def load_pickle(username):
	user_path = os.path.join(settings.DB_PATH, f'{username}.pk')
	if os.path.exists(user_path):
		with open(user_path, 'rb')as fr:
			data = pickle.load(fr)
			return data
