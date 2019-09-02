from aws_cdk import (aws_ec2 as ec2, core)
from aws_cdk.core import IAspect, IConstruct
import jsii


@jsii.implements(IAspect)
class ProjectStatusChecker:
    def visit(self, node: "IConstruct") -> None:
        print(type(node))


class CdkdemoAspectStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.node.apply_aspect(ProjectStatusChecker())
