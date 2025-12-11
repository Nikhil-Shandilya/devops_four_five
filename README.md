open -a Docker
systemctl --user start docker-desktop
systemctl --user force-reload docker-desktop


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

# last
kubectl apply -f service-nodeport.yaml
kubectl get svc student-portal-node-port
kubectl get nodes -o wide
curl http://localhost:30080
curl http://192.168.3.10:30080
if not then  
kubectl delete svc student-portal-node-port
kubectl scale deployment <deployment-name> --replicas=3
kubectl get pods -l app=<app name>

