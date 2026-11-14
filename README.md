# SAE5.02 - Automatisation du déploiement d'une application web avec Docker et Ansible


## Sommaire

1. Objectif du projet
2. Architecture actuelle
3. Versions utilisées
4. Inventaire Ansible
5. Configuration Ansible
6. Réseau Docker
7. Base de données MariaDB
8. Application Flask  : fait pour le déploiement de base, mais pas encore la vraie gestion de tâches/authentification
9. Accès à l'application
10. Communication Flask / MariaDB
11. Playbooks
12. Sauvegarde / restauration
13. Scénarios de tests prévus
14. État d'avancement


## 1. Objectif du projet

L'objectif de ce projet est d'automatiser le déploiement d'une application web de gestion de tâches à l'aide de Docker et Ansible.

L'application est développée avec Flask et utilise une base de données MariaDB.

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

Dans la première version du cahier des charges, un conteneur `ansible-manager` était prévu.

J'ai finalement choisi d'exécuter Ansible directement sur la VM Ubuntu afin de simplifier l'administration et d'éviter de donner l'accès au socket Docker à un conteneur supplémentaire.

L'inventaire utilise donc :

`localhost ansible_connection=local`

Architecture actuelle :

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
|-- volume Docker
|   `-- sae502_mariadb_data
|
`-- réseau Docker
    `-- sae502_net

Le réseau `sae502_net` permet la communication entre l'application Flask et MariaDB.

Le volume `sae502_mariadb_data` permet de conserver les données MariaDB indépendamment du cycle de vie du conteneur.

---

## 3. Versions utilisées

Environnement hôte :

- Ubuntu : 26.04.1 LTS
- Python : 3.14.4
- Docker : 29.1.3
- Ansible Core : 2.20.1
- community.docker : 5.0.4

Environnement applicatif :

- Flask : 3.1.1
- MariaDB : 11.4
- PyMySQL : 1.1.1
- image Python de l'application : `python:3.14-slim`
- image MariaDB : `mariadb:11.4`

---

## 4. Inventaire Ansible

Fichier :

`inventory/hosts.ini`

Contenu :

```ini
[manager]
localhost ansible_connection=local

```markdown

## 13. Scénarios de tests prévus

Les tests prévus concernent notamment :

- démarrage des conteneurs ;
- accessibilité de Flask ;
- communication Flask / MariaDB ;
- persistance des données MariaDB ;
- authentification des utilisateurs ;
- séparation des droits utilisateur et administrateur ;
- impossibilité pour un utilisateur de consulter les tâches d'un autre ;
- impossibilité pour un utilisateur de modifier les tâches d'un autre ;
- interdiction d'accès aux fonctions administrateur pour un utilisateur simple ;
- création d'une sauvegarde ;
- restauration d'une sauvegarde ;
- conservation des 7 dernières sauvegardes ;
- idempotence des playbooks Ansible.

---

## 14. État d'avancement

### Réalisé

- VM Ubuntu préparée ;
- dépôt GitHub créé ;
- arborescence du projet créée ;
- Docker installé ;
- Ansible installé ;
- collection `community.docker` disponible ;
- inventaire Ansible créé ;
- fichier `ansible.cfg` créé ;
- réseau `sae502_net` créé avec Ansible ;
- premier test d'idempotence réalisé ;
- Ansible Vault configuré ;
- volume MariaDB `sae502_mariadb_data` créé ;
- conteneur MariaDB `db-server` déployé ;
- idempotence du déploiement MariaDB vérifiée ;
- conteneur Flask `web-app` construit et déployé avec Ansible ;
- port `8080` publié vers le port `5000` du conteneur Flask ;
- communication Flask / MariaDB validée avec la route `/db-test`.

### Prochaines étapes

- développer la gestion réelle des tâches ;
- ajouter l'authentification ;
- ajouter les rôles utilisateur et administrateur ;
- mettre en œuvre la sauvegarde MariaDB ;
- mettre en œuvre la restauration ;
- appliquer la politique de rétention des 7 dernières sauvegardes ;
- compléter les scénarios de tests.


