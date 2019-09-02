from aws_cdk import (aws_ec2 as ec2, aws_ecr as ecr, aws_iam as iam, aws_codebuild as codebuild,
                     custom_resources as custom, core)
from aws_cdk.core import IAspect, IConstruct
import jsii
from jsii._kernel import ObjRef, Object

@jsii.implements(IAspect)
class ProjectStatusChecker:
    def visit(self, node: "IConstruct") -> None:
        print(type(node))


class CdkdemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        vpc = ec2.Vpc.from_lookup(self, 'vpc-e9cd4793', vpc_id='vpc-e9cd4793')
        print(vpc.availability_zones)


