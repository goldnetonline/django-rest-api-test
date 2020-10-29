'''
File: private_backend.py
Project: token-credit-backend
File Created: Thursday, 25th June 2020 4:41:10 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Thursday, 29th October 2020 12:18:39 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''
import hmac
from .logging import logger
from .helper import randomStringDigits, config
from .http import request as http_request
from .exceptions import NoOrInvalidPaystackKey, Forbidden
from .dataclass import Dataclass


class PaystackStatus(Dataclass):
    """
    An enum class for paystack statuses
    """

    PENDING = 'pending'
    FAILED = 'failed'
    SUCCESS = 'success'
    QUEUED = 'queued'
    ABANDONED = 'abandoned'


class Paystack:
    """
    Perform all paystack request and some helper methods

    Raises:
        Forbidden: Webhook not from paystack
        NoOrInvalidPaystackKey: Paystack key is not provided
    """

    PAYSTACK_CHARGE_BENCHMARK = 2000
    PAYSTACK_WAIVER_100_MAX = 2500
    PAYSTACK_PROCESSING_FEE = 100

    @staticmethod
    def generate_txn_ref(chars: int = 12) -> str:
        """Generate Transaction Reference

        Args:
            digits (int, optional): Numbers of characters. Defaults to 12.

        Returns:
            str: The txn reference
        """
        return randomStringDigits(chars).lower()

    @staticmethod
    def verify_request(req, paystack_key=None) -> bool:
        """
        Verify webhook request is from paystack

        Args:
            req (Object): The request payload
            paystack_key (str, optional): Paystack secret key. Defaults to None.

        Raises:
            Forbidden: Webhook not from paystack
            NoOrInvalidPaystackKey: Paystack key is not provided

        Returns:
            bool: If the request is from paystack or not
        """

        if 'x-paystack-signature' not in req.headers:
            raise Forbidden

        if not paystack_key:
            paystack_key = config('PAYSTACK_SECRET_KEY', None)

        # Still no key
        if not paystack_key:
            raise NoOrInvalidPaystackKey

        confirm = hmac.new(
            bytes(paystack_key, encoding="utf-8"),
            req.body,
            'sha512'
        ).hexdigest()

        if not hmac.compare_digest(req.headers['x-paystack-signature'], confirm):
            raise Forbidden

        return True

    @staticmethod
    def request(endpoint: str, payload: dict = None, method: str = None, paystack_key: str = None):
        """
        Make Paystack request

        Args:
            endpoint (str): The endpoint to make request to
            payload (dict, optional): The request data/payload. Defaults to {}.
            method (str, optional): The request method. Defaults to None.
            paystack_key (str, optional): The paystack API key. Defaults to None.

        Raises:
            Exception

        Returns:
            [type]: [description]
        """
        if not method:
            method = 'get' if not payload else 'post'

        if not paystack_key:
            paystack_key = config('PAYSTACK_SECRET_KEY', None)

        paystack_api_endpoint = config(
            'PAYSTACK_API_ENDPOINT', 'https://api.paystack.co')

        endpoint = f"/{endpoint}" if not endpoint.startswith("/") else endpoint

        paystack_api_endpoint = f"{paystack_api_endpoint}{endpoint}"

        try:
            req = http_request(paystack_api_endpoint, {
                "data": payload,
                'headers': {
                    "Authorization": f"Bearer {paystack_key}"
                }
            }, method.upper())
            return req.json()
        except Exception as ex:
            logger.exception(ex)
            return {
                "success": False,
                "status": False,
                "message": "Cannot get information, please try again"
            }

    @classmethod
    def calculate_charges(
        cls,
        amount: float,
        percentage: float = 1.5,
        is_local_txn: bool = True,
        waived_100: bool = False
    ) -> float:
        """
        Calculate the local charges for a transaction

        Args:
            amount (float): The proposed transaction amount =
            percentage (float, optional): The paystack rate. Defaults to 1.5.
            is_local_txn (bool, optional): If the transaction is a local transaction. Defaults to True.
            waived_100 (bool, optional): if the 100 naora transaction charge is waived. Defaults to False.

        Returns:
            float: [description]
        """

        if amount <= cls.PAYSTACK_WAIVER_100_MAX and is_local_txn:
            waived_100 = True

        charge = amount * (percentage/100)

        if not waived_100:
            charge += cls.PAYSTACK_PROCESSING_FEE

        if is_local_txn and charge > cls.PAYSTACK_CHARGE_BENCHMARK:
            charge = cls.PAYSTACK_CHARGE_BENCHMARK

        return charge
