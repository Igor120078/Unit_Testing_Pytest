import pytest
from pay.processor import PaymentProcessor


API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"

def test_api_key_invalid() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge("1249190007575069", 12, 2024, 100)

def test_validate_cart_valid_date() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge("5168440734096733", 10, 2025, 100)

def test_validate_cart_invalid_date() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("5168440734096733", 8, 2023, 100)

def test_validate_card_valid_number() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.validate_card("5168440734096733", 12, 2025)

def test_validate_cart_invalid_number() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("5168440734096734", 12, 2025, 100)

def test_validate_cart_invalid_month() -> None:
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor(API_KEY)
        payment_processor.charge("5168440734096733", 13, 2025, 100)

def test_validate_cart_invalid_year() -> None:
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor(API_KEY)
        payment_processor.charge("5168440734096733", 10, 2023, 100)



