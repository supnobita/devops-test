///vars/pipeline.groovy

def call(String k8sDeploymentName,String nameSpace){
if nameSpace.indexOf("master") != -1 {
    nameSpace = "production"
}
else {
    nameSpace = "develop"
}
pipeline {

    agent any

    environment {
        K8S_DEPLOYMENT_NAME = "${k8sDeploymentName}"
        NAME_SPACE= "${nameSpace}"
    }

    stages {

        stage('Python unit test'){
            steps{
                sh echo "Run python unit test"      
            }
        }

        stage('Docker build'){
            steps{
                script{
                    withDockerRegistry(url: 'https://registry.xxx.com','docker-id') {
                        def app = docker.build("registry.xxx.com/$GIT_BRANCH/$JOB_NAME:$BUILD_NUMBER")
                        app.push()
                    }
                }      
            }
        }

        stage('Deploying'){
            steps {
                kubernetesDeploy( configs: 'k8s_deploy.yaml',
                enableConfigSubstitution: true,
                kubeConfig: [path: ''], kubeconfigId: 'kube-deploy', secretName: '',
                dockerCredentials: [[credentialsId: 'docker-id', url: 'https://registry.xxx.com']]
                )
            }
        }
    }
}
}