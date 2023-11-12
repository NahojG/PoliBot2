pipeline{
    agent any
    stages{
        stage ('Build'){
            steps{
                echo "Estapa BUILD no disponible"
            }
        }
        stage ('Tests'){
            steps{
                echo "Etapa TEST no disponible"
            }
        }
        stage ('Check Docker Compose') {
        steps {
            sh "docker-compose --version"
            }
        }
        stage ('Deploy'){
            steps{
                sh "docker-compose down -v"
                sh "docker-compose up -d --build"
            }
        }
    }
}