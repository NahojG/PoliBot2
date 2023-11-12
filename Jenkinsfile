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
        stage ('Deploy'){
            steps{
                sh "/usr/bin/docker-compose down -v"
                sh "/usr/bin/docker-compose up -d --build"
            }
        }
    }
}