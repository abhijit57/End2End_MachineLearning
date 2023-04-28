
## End to End Machine Learning Project

#### This is an end to end project which predicts student performances using machine learning techniques incorporating robust software engineering and MLOps practices.


#### Deployment: AWS CodePipeline and Elastic Beanstalk
A web app can be created in the AWS Elastic Beanstalk. Then, the whole project once pushed to a Github repository can be linked to the CodePipeline which would then link with Elastic Beanstalk as deployment provider and the environment created by the web app by beanstalk itself. So, after the github repo is linked with code pipeline which is then linked to elastic beanstalk web app. Then, a continuous delivery pipeline would be created with an URL available. That URL can be triggered in the web-app to access the web app. Moreover, github actions can be integrated into the project pushed into the repo which would then run based on the actions yaml file and act as a Continuous Inegration pipeline. So, if any code changes were done and pushed to the repo, github actions (CI) would be triggered and then the AWS CodeDeploy & Elastic Beanstlak would be triggered too as part of (CD). This is how we can incorporate CI/CD practices into this project.

#### Docker, AWS ECR, EC2, GitHub Actions, Self-Hosted Runner, CI-CD
Docker Build checked
Github Workflow
Iam User In AWS
Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

Configure EC2 as self-hosted runner:
Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app

