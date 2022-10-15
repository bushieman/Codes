# create a new resource, the imperative way.
# This may be used in secrets.
kubectl create <resource> --image=<image name> <resource name>

# create a new resource; the declarative way
# This is the preferred way.
kubectl apply -f manifest-file.yaml

# create new resources at once
kubectl apply -f .

# edit a specific resource
kubectl edit <resource> <resource name>

# show all resources available in our cluster
kubectl get all

# show persistent volumes
kubectl get pv

# show persistent volume claims
kubectl get pvc

# show all resources in a specific namespace
# Note: All commands are written in the default namespace by default
kubectl get all -n <namespace name>

# show available resources
kubectl get <resource>

# delete specific resource
kubectl delete <resource> <resource name>

# delete items of a given resource
kubectl delete <resource> --all

# delete all resources
kubectl delete all --all

# describe the details of a resource
kubectl describe <resource> <resource name>

# get the logs of a resource
kubectl log <resource> <resource name>

# there's no need to specify a resource type as a separate argument when the resource name is similar.
# This also applies to all options not just describe e.g
kubectl describe pods pods/client-server
# instead
kubectl describe pod/client-server
# but the following will not work
kubectl describe deployment.app/client-depl
# instead
kubectl describe deployment deployment.app/client-depl

