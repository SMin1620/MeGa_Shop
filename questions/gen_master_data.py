from django.contrib.contenttypes.models import ContentType

from questions.models import Question, Answer
from products.models import Product


def gen_master(apps, schema_editor):
    product = Product.objects.get(id=1)
    product_content_type = ContentType.objects.get_for_model(product)
    Question(user_id=2, content_type=product_content_type, object_id=product.id, content="이거 물빠짐 심한가요?").save()
    Question(user_id=3, content_type=product_content_type, object_id=product.id, content="이거 입으면 인싸?").save()

    product = Product.objects.get(id=2)
    product_content_type = ContentType.objects.get_for_model(product)
    Question(user_id=1, content_type=product_content_type, object_id=product.id, content="이거 원단이 튼튼한가요?").save()
    Question(user_id=3, content_type=product_content_type, object_id=product.id, content="이거 세탁해도 되나요?").save()


