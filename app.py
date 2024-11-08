#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_sample.cdk_sample_stack import CdkSampleStack
from vpc_cdk.vpc_cdk_stack import VpcCdkStack
from s3_cdk.s3_cdk_stack import CdkS3Stack
from ec2_cdk.ec2_cdk_stack import CdkEc2Stack


app = cdk.App()
stack1 = VpcCdkStack(app, "VpcCdkStack")
stack2 = CdkS3Stack(app, "CdkS3Stack")
stack3 = CdkEc2Stack(app, "CdkEc2Stack", vpc=stack1.vpc)

app.synth()
