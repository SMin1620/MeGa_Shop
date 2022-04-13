from .common import *

DEBUG = False

ALLOWED_HOSTS = ['*']


# 운영서버 DB 정보
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'site1',
        'USER': 'dltmdals1620',
        'PASSWORD': '1234',
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'test_base',
#         'USER': 'root',
#         'PASSWORD': '1234',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'OPTIONS': {
#             # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # 추가, 만약에 이 부분 때문에 오류가 난다면, 이 라인을 지우고 다시 시도해주세요.
#             'charset': 'utf8mb4',
#             'use_unicode': True,
#         },
#     }
# }