from marshmallow import Schema
from marshmallow import validate
from marshmallow import fields
from techtest.author.models import Author
from marshmallow.decorators import post_load

class AuthorSchema(Schema):
    class Meta(object):
        model = Author

    id = fields.Integer()
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)

    @post_load
    def update_or_create(self, data, *args, **kwargs):

        author, _ = Author.objects.update_or_create(
            id=data.pop("id", None), defaults=data
        )

        return author