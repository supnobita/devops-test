package org.test
class Utilities implements Serializable {
  def steps
  Utilities(steps) {this.steps = steps}
  def mvn(args) {
    steps.sh "${steps.tool 'Maven'}/bin/mvn -o ${args}"
  }
  def k8sdeploy(k8sYamlName){
      steps.kubernetesDeploy( configs: ${k8sYamlName},
                enableConfigSubstitution: true,
                kubeConfig: [path: ''], kubeconfigId: 'kube-deploy', secretName: '',
                dockerCredentials: [[credentialsId: 'docker-id', url: 'https://registry.xxx.com']]
                )
  }
}