open -a Docker
docker build -t image-name:v1 .
docker run -d --name container-name -p 5007:5000 image-name:v1

docker logs -f container-name
docker ps
docker ps -a
docker images

docker stop container-name
docker rm container-name
docker rmi image-name:v1

# optional (only if needed)
docker rm -f container-name
docker rmi -f image-name:v1

# first setup kubernetes
kubectl config get-contexts
kubectl apply -f deployment.yaml
kubectl get deployments
kubectl get pods -l app=<app name>
kubectl logs <pod-name>
