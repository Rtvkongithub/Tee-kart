pipeline {
  agent any

  environment {
    IMAGE_NAME = "rtvk/products-service"
    REGISTRY = "ghcr.io"
    GITHUB_USERNAME = "rtvkongithub"
  }

  stages {
    stage('Clone') {
      steps {
        git 'https://github.com/Rtvkongithub/Tee-kart.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        dir('backend') {
          sh 'docker build -t $IMAGE_NAME:latest .'
        }
      }
    }

    stage('Push to GitHub Container Registry') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'ghcr-creds', usernameVariable: 'USERNAME', passwordVariable: 'TOKEN')]) {
          sh '''
            echo $TOKEN | docker login ghcr.io -u $USERNAME --password-stdin
            docker tag $IMAGE_NAME:latest ghcr.io/$GITHUB_USERNAME/products-service:latest
            docker push ghcr.io/$GITHUB_USERNAME/products-service:latest
          '''
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f k8s/'
      }
    }
  }
}
