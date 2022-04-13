from django.conf import settings

from accounts.models import User


# 유저 더미데이터
def gen_master(apps, schema_editor):

    # 총 관리자 어드민
    User.objects.create_superuser(
        username='admin',
        password='admin',
        name='관리자',
        email='admin@email.com',
        gender=User.GenderChoices.FEMALE
    )

    # 일반 유저
    for id in range(2, 6):
        username = f"user{id}"
        password = f"user{id}"
        name = f"이름{id}"
        email = f"test{id}@test.com"
        gender = User.GenderChoices.MALE

        User.objects.create_user(username=username, password=password, name=name, email=email, gender=gender)

    # 마켓 관리자 어드민
    for id in range(2, 6):
        username = f"master{id}"
        password = f"master{id}"
        name = f"이름{id}"
        email = f"master{id}@email.com"
        gender = User.GenderChoices.MALE

        User.objects.create_user(username=username, password=password, name=name, email=email, gender=gender)


