import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as apigw
)
from constructs import Construct
import os

class InfraStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        phone_number_lookup_lambda = lambda_.Function(
            self,
            "PhoneNumberLookupFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("lambda_function"),
            handler="app.lambda_handler"
        )

        api = apigw.LambdaRestApi(
            self,
            "PhoneNumberLookupApi",
            handler=phone_number_lookup_lambda,
            proxy=False
        )

        phone_numbers_resource = api.root.add_resource("phone-numbers")
        phone_numbers_resource.add_method("GET")
