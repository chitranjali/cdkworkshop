from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)

class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime= _lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='hello.handler'
        )

        apigw.LambdaRestApi(self, 'Endpoint', handler=my_lambda)
