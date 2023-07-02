from marshmallow import Schema, fields


class Shop(Schema):
    id = fields.UUID(allow_none=True, missing=None)
    user_id = fields.UUID()
    name = fields.Str()
    created_at = fields.DateTime(missing=None)
    updated_at = fields.DateTime(missing=None)
