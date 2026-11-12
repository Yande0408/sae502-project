# SAE5.02 - Automatisation du déploiement d'une application web avec Docker et Ansible

## 1. Objectif du projet

L'objectif de ce projet est d'automatiser le déploiement d'une application web de gestion de tâches à l'aide de Docker et Ansible.

L'application sera développée avec Flask et utilisera une base de données MariaDB.

Le projet prévoit également :
- une authentification des utilisateurs ;
- deux rôles : utilisateur et administrateur ;
- un mécanisme de sauvegarde et de restauration de la base de données ;
- une politique de rétention des sauvegardes ;
- des tests permettant notamment de vérifier l'idempotence des playbooks Ansible.

---

## 2. Architecture actuelle

L'environnement repose sur une machine virtuelle Ubuntu.

Ansible est exécuté directement sur la VM et administre localement le moteur Docker.

Choix actuel :
- Ansible n'est pas exécuté dans un conteneur `ansible-manager` ;
- l'inventaire utilise `localhost` avec `ansible_connection=local` ;
- Docker est installé directement sur la VM.
 Dans la première version du cahier des charges, un conteneur ansible-manager était prévu. Pour simplifier l’administration et éviter de donner l’accès au socket Docker à un conteneur supplémentaire, j’ai finalement choisi d’exécuter Ansible directement sur la VM Ubuntu hôte. Les playbooks administrent donc localement le moteur Docker avec ansible_connection=local


Architecture prévue :

VM Ubuntu
|
|-- Ansible
|   `-- exécution locale
|
|-- Docker
|   |
|   |-- web-app
|   |   `-- Flask
|   |
|   `-- db-server
|       `-- MariaDB
|
`-- réseau Docker : sae502_net

Le réseau `sae502_net` permettra la communication entre l'application Flask et MariaDB.

---

## 3. Versions actuellement utilisées

- Ubuntu : 26.04.1 LTS
- Python : 3.14.4
- Docker : 29.1.3
- Ansible Core : 2.20.1
- community.docker : 5.0.4

Les versions de Flask et MariaDB seront précisées avant leur déploiement.

---

## 4. Inventaire Ansible

Fichier :

`inventory/hosts.ini`

Contenu :

```ini
[manager]
localhost ansible_connection=local# sae502-project
