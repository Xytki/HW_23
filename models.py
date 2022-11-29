from marshmallow import fields, Schema, validates_schema, ValidationError


class RequestParamsSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        valid_cmd_command = {'filter', 'sort', 'map', 'limit', 'unique'}

        if values['cmd'] not in valid_cmd_command:
            raise ValidationError({'cmd': f'contains invalid command={values["cmd"]}'})

        return values


class RequestParamsListSchema(Schema):
    queries = fields.Nested(RequestParamsSchema, many=True)
    filename = fields.Str(required=True)
