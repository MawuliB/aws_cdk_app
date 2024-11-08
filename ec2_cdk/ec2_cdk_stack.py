from constructs import Construct
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
)

import aws_cdk.aws_ec2 as ec2
import aws_cdk as cdk

class CdkEc2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # implementation of the EC2
        self.first = ec2.Instance(
            self, 
            "MyEc2",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2,
                ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            vpc=vpc,
            security_group=ec2.SecurityGroup(
                self,
                "MySecurityGroup",
                vpc=vpc,
                allow_all_outbound=True,
                security_group_name="MySecurityGroup"
            ),
            instance_name="MyFirstInstance"
        )

        CfnOutput(self, "InstanceID", value=self.first.instance_id)
