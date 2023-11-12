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
                sh "/usr/local/bin/docker-compose down -v"
                sh "/usr/local/bin/docker-compose up -d --build"
            }
        }
    }
}