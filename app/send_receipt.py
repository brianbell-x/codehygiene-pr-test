def send_receipt(order: Order) -> None:
    try:
        if order is not None:
            if order.paid and not order.refunded:
                # Extract email address from order
                email = order.email
                if email is not None:
                    if len(email.strip()) > 0:
                        mailer.send(email, order.id)
    except Exception:
        pass