import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'LoginAndRe.settings'

if __name__ == '__main__':

    send_mail(
        '宫彦胜的自动邮件测试',
        '今天是周四，你好',
        'gong_yan_sheng@sina.com',
        ['1874735924@qq.com'],
    )

