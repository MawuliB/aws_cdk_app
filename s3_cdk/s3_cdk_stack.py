from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
)

import aws_cdk.aws_s3 as s3
import aws_cdk as cdk

class CdkS3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "CdkS3Bucket",
            versioned=True,
            auto_delete_objects=True,
            removal_policy=cdk.RemovalPolicy.DESTROY
        )