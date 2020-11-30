from botapi import Model, Field, ListField

order = {
    'user': {
        'name': 'Jack',
        'surname': 'Doe',
        'phone': '123456789',
    },
    'paid': True,
    'items': [
        {
            'name': 'product 1',
            'id': 1,
            'quantity': 2,
            'subtotal': 10.5
        },
        {
            'name': 'product 2',
            'id': 2,
            'quantity': 1,
            'subtotal': 5
        }
    ]
}


class Item(Model):
    name = Field()
    item_id = Field(alias='id')


# inherit model
class CartItem(Item):
    quantity = Field(base=int)
    subtotal = Field()


class UserModel(Model):
    name = Field()
    surname = Field()
    phone = Field()


class OrderModel(Model):
    user = Field(base=UserModel)
    paid = Field(base=bool, default=False)
    cart = ListField(item_base=CartItem, default=[], alias='items')


# deserialize data
obj = OrderModel(**order)

# work with data
obj.user.name = 'John'
obj.paid = True
obj.cart[0].subtotal = 12.5

# may be you want to add some data
comment = 'call before delivery'

# serialize data
print(obj.serialize(data_to_update={'comment': comment}))
