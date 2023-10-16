import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_price(type_of_obj, obj):
    starter_subscription = stripe.Product.create(
        name=f'{type_of_obj} "{obj.title}"',
    )

    starter_subscription_price = stripe.Price.create(
        unit_amount=obj.price * 100,
        currency="dkk",
        recurring={"interval": "month"},
        product=starter_subscription['id'],
    )

    link = stripe.PaymentLink.create(
        line_items=[
            {
                "price": starter_subscription_price.id,
                "quantity": 1,
            },
        ],
    )

    return link.get('url', 'Сосамба, нет ссылки!')
