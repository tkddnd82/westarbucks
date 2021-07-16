DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'we',
        'USER': 'root',
        'PASSWORD':'1004',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        }
}

SECRET_KEY = 'django-insecure-^*12vw38cmep2g1xt_ysh0irxe0i%lnc$70*48fr&&x5&y)9)h' #settings.py에 있는 secret_key 를 사용합니다.
