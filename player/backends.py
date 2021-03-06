from django.conf import settings
from django.contrib.auth.models import User
import hashlib

class GenMD5ModelBackend(object):
	def authenticate(self, username=None, password=None):
		try:
			user = User.objects.get(username=username)
			if user.check_password(password):
				user.get_profile().pass_md5 = hashlib.md5(password).hexdigest()
				user.get_profile().pass_sha1 = hashlib.sha1(password).hexdigest()
				user.get_profile().save()
				return user
		except User.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
