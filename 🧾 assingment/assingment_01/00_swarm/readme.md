# 📂 00_swarm

## Overview

`00_swarm` typically refers to distributed computing or container orchestration, such as Docker Swarm.  
This folder is for orchestrating services—no coding is required here.

---

## What is Docker Swarm?

Docker Swarm is a container orchestration tool that helps manage and coordinate multiple Docker containers across a cluster of machines (called **nodes**).  
It enables your application to be scalable and fault-tolerant.

---

## Why Use Docker Swarm?

- **Easy Deployment & Scaling:** Simplifies deploying and scaling applications.
- **Built-in Features:** Provides load balancing, service discovery, and rolling updates.

---

## Key Concepts

- **Swarm:** A group of Docker nodes working together.
- **Node:** A single Docker host in the swarm.
- **Manager Node:** Handles orchestration and cluster management.
- **Worker Node:** Runs containers as instructed by managers.
- **Service:** Defines how your app should run (image, replicas, etc.).

---

## Basic Docker Swarm Commands

> _Note: You do **not** need to run these commands for this assignment!_

```sh
# Initialize a swarm
docker swarm init

# List nodes in the swarm
docker node ls

# Deploy a service
docker service create --name my_web_app -p 8080:80 nginx

# Check running services
docker service ls
```
