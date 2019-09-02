from aws_cdk import (aws_ec2 as ec2, core)


class CdkdemoContextStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        vpc = ec2.Vpc.from_lookup(self, 'vpc-e9cd4793', vpc_id='vpc-e9cd4793')
        print(vpc.availability_zones)


        gw = ec2.CfnVPNGateway(self, 'vpngw', type='ipsec.1')
        gwa = ec2.CfnVPCGatewayAttachment(self, 'vpcgwa', vpc_id=vpc.vpc_id, vpn_gateway_id=gw.logical_id)\
            .add_depends_on(gw)

        gw.node.set_context("custom_val", "different")
        print("Child: " + gw.node.try_get_context("custom_val"))
        print("Global: " + self.node.try_get_context("custom_val"))
        print("VPC: " + vpc.node.try_get_context("custom_val"))
