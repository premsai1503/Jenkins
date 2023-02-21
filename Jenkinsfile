pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/BThangaraju/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod 777 IMT2019067_prog.py"
                sh "./IMT2019067_prog.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
