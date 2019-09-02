#!/usr/bin/env python3

from aws_cdk import core
from cdkdemo.cdkdemo_stack import CdkdemoStack
from cdkdemo.cdkdemo_context import CdkdemoContextStack
from cdkdemo.cdkdemo_assets import CdkdemoAssetsStack
from cdkdemo.cdkdemo_aspect import CdkdemoAspectStack
from cdkdemo.cdkdemo_custom import CdkdemoCustomStack
import os

app = core.App()
CdkdemoAssetsStack(app, "cdkdemoassets")
CdkdemoAspectStack(app, "cdkdemoaspect")
CdkdemoCustomStack(app, "cdkdemocustom")
CdkdemoContextStack(app, "cdkdemocontext", env={'region': os.environ.get('CDK_DEFAULT_REGION'),
                                  'account': os.environ.get('CDK_DEFAULT_ACCOUNT')})

app.synth()
