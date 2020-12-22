from datetime import datetime

from botapi import Model, Field, ListField, DateTimeField

order = {
    'user': {
        'name': 'Jack',
        'surname': 'Doe',
        'phone': '123456789',
    },
    'date': '2020-12-10 10:12:13',
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
    order_date = DateTimeField()


# deserialize data
obj = OrderModel(**order)

# work with data
obj.user.name = 'John'
obj.paid = True
obj.cart[0].subtotal = 12.5
obj.order_date = datetime.now()

# may be you want to add some data
comment = 'call before delivery'

# serialize data
print(obj.serialize(data_to_update={'comment': comment}))
