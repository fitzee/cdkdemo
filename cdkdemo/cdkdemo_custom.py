from aws_cdk import (aws_codebuild as codebuild, custom_resources as custom, core)


class CdkdemoCustomStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        uri = self.account + '.dkr.ecr.' + self.region + '.amazonaws.com'
        appl = 'colorteller'
        buildspec = {
            'version': '0.2',
            'phases': {
                'install': {
                    'commands': ['echo install step']
                },
                'pre_build': {
                    'commands': ['echo logging in to AWS ECR...',
                                 '$(aws ecr get-login --no-include-email --region %s)' % self.region]
                },
                'build': {
                    'commands': ['echo building Docker image...',
                                 'cd appmeshdemo/colorapp/%s' % appl,
                                 'docker build -t %s:latest .' % appl,
                                 'docker tag %s:latest %s/%s:latest' % (appl, uri, appl)]
                },
                'post_build': {
                    'commands': ['echo Docker image build complete!',
                                 'echo push latest Docker images to ECR...',
                                 'docker push %s/%s:latest' % (uri, appl)]
                }
            }
        }

        buildenviron = codebuild.BuildEnvironment(privileged=True,
                                                  build_image=codebuild.LinuxBuildImage.UBUNTU_14_04_DOCKER_18_09_0,
                                                  environment_variables={'AWS_DEFAULT_REGION': codebuild.BuildEnvironmentVariable(value=self.region),
                                                                         'AWS_ACCOUNT_ID': codebuild.BuildEnvironmentVariable(value=self.account),
                                                                         'IMAGE_REPO_NAME': codebuild.BuildEnvironmentVariable(value=appl),
                                                                         'IMAGE_TAG': codebuild.BuildEnvironmentVariable(value='latest')})

        proj = codebuild.Project(self, appl, build_spec=codebuild.BuildSpec.from_object(buildspec),
                                 environment=buildenviron)
        call = custom.AwsSdkCall(service='CodeBuild', action='startBuild', parameters={'projectName': proj.project_name},
                                 physical_resource_id='Custom%s' % proj.project_name)

        custom.AwsCustomResource(self, 'CustomCodeBuild', on_create=call, on_update=call)
