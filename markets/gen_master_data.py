from markets.models import Market


# 마켓 더미데이터
def gen_master(apps, schema_editor):
    Market(name="A 매장", site_url="https://www.abc1.co.kr", email="test1@test.com", master_id=2).save()
    Market(name="B 매장", site_url="https://www.abc2.co.kr", email="test2@test.com", master_id=3).save()
    Market(name="C 매장", site_url="https://www.abc3.co.kr", email="test3@test.com", master_id=4).save()