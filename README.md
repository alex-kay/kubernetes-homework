# kubernetes-homework

## Homework task for the Kubernetes module

* Create a kubernetes deployment and service with the `fortune` program  
* Docker image: [Docker Hub](https://hub.docker.com/r/perarneng/fortune/)
* Make this deployment accessible as a service from within the cluster
* A different fortune should show every time the service is called.  
* Use local Minikube

## Homework task completion steps

* Took a simple deployment yaml from k8s official tutorial, to use as a template for our app deployment
* Made a docker image from `python:slim` image adding `fortune-mod` and `Flask`
* Wrote a deployment with a simple service
* deployed it on Minikube and got a fortune answer from service inner ip:
![img1](img/Screenshot%202021-10-27%20080056.png)

## Task 2

* Added an ingress and created a namespace `alex` on cluster
* App works on [http://alex-fortune.kubelab.spainip.es](http://alex-fortune.kubelab.spainip.es)

### Task 3

In another repository, [https://github.com/alex-kay/kubernetes-homework3](https://github.com/alex-kay/kubernetes-homework3)
