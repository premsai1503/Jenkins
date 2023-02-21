pipeline { 
agent any
    stages {
        stage('Cloning Git') {
            steps {
                git 'https://github.com/premsai1503/Jenkins.git'
            }
        }
        stage('Building Code') {
            steps {
                sh "chmod 777 IMT2019067_prog.py"
                sh "./IMT2019067_prog.py"
            }
        }
     stage('Testing Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
