from aws_cdk import (aws_ecs as ecs, core)


class CdkdemoAssetsStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        task_def = ecs.FargateTaskDefinition(self, "CdkDemoTaskDef")
        task_def.add_container("CdkDemoContainerImage", image=ecs.ContainerImage.from_asset('./assets'))
