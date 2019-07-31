# k8s manifests for deploying quotes app

Application deployment relies on the existence of three secrets. Create and label them as follows:

We assume `pwgen`is available, otherwise generate these however you see fit.

```bash
# root password for mariadb container image
kubectl create secret generic quotes-app-dbrootuser-pass --from-literal=MYSQL_ROOT_PASSWORD=$(pwgen 20 1)

# our DB user password for mariadb container image
kubectl create secret generic quotes-app-dbuser-pass --from-literal=MYSQL_PASSWORD=$(pwgen 20 1)

# (optional) Admin Token for API POST requests
kubectl create secret generic quotes-app-admin-token --from-literal=ADMIN_TOKEN=$(pwgen 36 1)

# label your secrets
kubectl label secret quotes-app-admin-token quotes-app-dbuser-pass quotes-app-dbrootuser-pass --overwrite app=quote
```