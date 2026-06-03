#!/bin/bash

echo "Creating SENTINEL Cluster..."

kind create cluster \
  --name sentinel \
  --config infra/kind/kind-cluster.yaml

echo "Installing Metrics Server..."

kubectl apply -f \
https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

echo "Cluster Ready."