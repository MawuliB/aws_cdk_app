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

class VpcCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # implementation of the VPC
        self.vpc = ec2.Vpc(
            self, "MyVpc",
            max_azs=3,
            # 'nat_gateways' defines the number of NAT Gateways to create.
            nat_gateways=1,
            # 'subnet_configuration' defines the subnet configuration.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                )
            ],
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.1/16")
        )


        CfnOutput(self, "VPCID", value=self.vpc.vpc_id)
        CfnOutput(self, "CIDR", value=self.vpc.vpc_cidr_block)
        CfnOutput(self, "PublicSubnets", value=str(self.vpc.public_subnets))
        CfnOutput(self, "PrivateSubnets", value=str(self.vpc.private_subnets))
