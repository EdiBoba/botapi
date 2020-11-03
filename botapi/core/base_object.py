from abc import ABCMeta

from botapi.core.base_field import Field


class BaseObjectMeta(ABCMeta):
    def __new__(mcs, name, bases, attr):
        new_class = super().__new__(mcs, name, bases, attr)

        fields = set()
        aliases = {}

        for parent in bases:
            if isinstance(parent, BaseObjectMeta):
                fields.update(getattr(parent, '_fields'))
                aliases.update(getattr(parent, '_aliases'))

        for key, value in attr.items():
            if isinstance(value, Field):
                fields.add(key)
                if value.alias is not None:
                    aliases.update({key: value.alias})
                if value.self_base is True:
                    value.base = new_class

        setattr(new_class, '_aliases', aliases)
        setattr(new_class, '_fields', fields)
        return new_class


class FieldSerializeMixin:
    def serialize(self):
        serialized_obj = {}
        for field in getattr(self, '_fields', []):
            field_value = getattr(self, field)
            if field_value is not None:
                serialized_field_value = field_value
                if isinstance(field_value, (list, tuple, set)):
                    serialized_field_value = \
                        [item.serialize() if isinstance(item,
                                                        FieldSerializeMixin) else item
                         for item in field_value]
                elif isinstance(field_value, FieldSerializeMixin):
                    serialized_field_value = field_value.serialize()
                serialized_obj.update({
                    getattr(self, '_aliases', {}).get(field, field):
                        serialized_field_value
                })
        return serialized_obj


class BaseObject(FieldSerializeMixin, metaclass=BaseObjectMeta):
    def serialize(self, data_to_update: dict = None):
        result = super().serialize()
        if data_to_update is not None:
            result.update(data_to_update)
        return result
