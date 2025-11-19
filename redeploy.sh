#!/bin/bash

echo "Nettoyage de Kubernetes..."
kubectl delete deployment flask-deployment 2>/dev/null
kubectl delete service flask-service 2>/dev/null

echo "Suppression des images Docker..."
docker rmi flask-api:latest --force 2>/dev/null
docker image prune -f

echo "Reconstruction de l'image..."
docker build --no-cache -t flask-api:latest .

echo "Déploiement sur Kubernetes..."
kubectl apply -f flask-deployment.yaml
kubectl apply -f flask-service.yaml

echo "Attente du démarrage des pods..."
kubectl wait --for=condition=ready pod -l app=flask-api --timeout=60s

echo "Terminé! Logs des pods:"
kubectl logs -l app=flask-api --tail=20