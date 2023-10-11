check-dependencies:
	@echo "Checking dependencies..."
	@which minikube > /dev/null || (echo "Minikube is not installed. Please install it and try again." && exit 1)
	@which kubectl > /dev/null || (echo "Kubectl is not installed. Please install it and try again." && exit 1)

setup: check-dependencies
	@echo "All dependencies are installed."
	@echo "Setting up environment..."

	@echo "Starting minikube..."
	@minikube start --nodes 3
	@echo "Minikube started."

	@echo "Setting up minikube..."
	@minikube addons enable ingress
	@minikube addons enable metrics-server
	@minikube addons enable dashboard
	@echo "Minikube setup complete."

	@echo "Setting up kubectl..."
	@kubectl config set-context minikube
	@echo "Kubectl setup complete."

	@echo "Environment setup complete."

setup-argocd:
	@echo "Setting up argocd..."
	@minikube status | grep -q "Running" || (echo "Minikube is not running. Please start it and try again." && exit 1)
	@kubectl create namespace argocd
	@kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


start: setup
	@echo "Starting application..."
	@kubectl apply -f kubernetes/
	@echo "Application started."