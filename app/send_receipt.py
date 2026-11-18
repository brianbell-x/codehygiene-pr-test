def send_receipt(order: Order) -> None:
    try:
        if order is not None and order.paid and not order.refunded:
            email = order.email
            if email is not None and len(email.strip()) > 0:
                mailer.send(email, order.id)
    except Exception:
        pass