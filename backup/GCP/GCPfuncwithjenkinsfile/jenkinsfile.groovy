pipeline {
  agent any
  environment {
    CLOUDSDK_CORE_PROJECT='hopeful-summer-368213'
  }
parameters {
    string(name: 'URL_API', defaultValue: 'default', description: 'token para acessar a url.')
    string(name: 'TOKEN', defaultValue: 'default', description: 'token para acessar a url.')
    string(name: 'ENVIROMENT', defaultValue: 'default', description: 'ambiente para url.')
    string(name: 'PRODUCT', defaultValue: 'default', description: 'token para acessar a url.')
    string(name: 'PROJECT_ID', defaultValue: 'default', description: 'Project Name passar entre aspas duplas.')

}
  stages {
   stage ('Clean Workspace'){
     steps{
       deleteDir()
      }
    }
    stage('Clone') {
    steps {
        git url: 'https://github.com/alexandreponte2/functionGCP2.git', branch: 'main'
      }
    }
    stage('ta aqui') {
    steps {
        echo "==================================================++++===============\n"
        sh 'ls -lha'
      }
    }
    stage('test') {
      steps {
        withCredentials([file(credentialsId: 'gcloud-creds', variable: 'GCLOUD_CREDS')]) {
          sh '''
            gcloud auth activate-service-account --key-file="$GCLOUD_CREDS"
            cd src/
            gcloud functions deploy get_secret_list \
               --entry-point=get_secret_list \
               --source=. \
               --runtime=python37 \
               --allow-unauthenticated \
               --trigger-http \
               --set-env-vars URL_API=$URL_API,TOKEN=$TOKEN,ENVIROMENT=$ENVIROMENT,PRODUCT=$PRODUCT \
               --project $PROJECT_ID
          '''
        }
      }
    }
  }
}