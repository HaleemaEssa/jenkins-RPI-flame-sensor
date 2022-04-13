pipeline {
    agent { label "linuxslave1" }
    environment {
        DOCKERHUB_CREDENTIALS=credentials('haleema-dockerhub')
    }
    stages {
        stage('GitClone') {
            steps {
                git branch: 'main', url: 'https://github.com/HaleemaEssa/jenkins-RPI-flame-sensor.git'
            }
        }
    stage('Createdockerimage on RPI') {
            steps {
                sh 'docker build -t haleema/docker-rpi-flame:latest .'
            }
        }     
    stage('Login to Dockerhub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        } 
        
    stage('runimage') {
         
            steps {
                sh 'docker run --privileged -t haleema/docker-rpi-flame'
            }
         }    
    
    stage('pushimage to Dockerhub') {
            steps {
                sh 'docker push haleema/docker-rpi-flame:latest'
            }
        }
         
    
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}
