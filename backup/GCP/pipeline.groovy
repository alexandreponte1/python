pipeline {
  agent any
  environment {
    CLOUDSDK_CORE_PROJECT='active-chimera-359118'
  }
parameters {
    string(name: 'SECRET_VALUE', defaultValue: 'default', description: 'Secret Value.')
    string(name: 'SECRET_NAME', defaultValue: 'default', description: 'Secret Name.')
    string(name: 'PROJECT_NAME', defaultValue: 'default', description: 'Project Name passar entre aspas duplas.')
}
  stages {
    stage('test') {
      steps {
        withCredentials([file(credentialsId: 'gcloud-creds', variable: 'GCLOUD_CREDS')]) {
          sh '''
            gcloud version
            gcloud auth activate-service-account --key-file="$GCLOUD_CREDS"
            printf $SECRET_VALUE| gcloud secrets create $SECRET_NAME --data-file=- --replication-policy=user-managed --locations=us-central1 --project $PROJECT_NAME
          '''
        }
      }
    }
  }
}