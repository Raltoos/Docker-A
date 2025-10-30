# DevOps Docker Project

This project demonstrates a **Node.js + Express frontend** and **Flask backend** running together using **Docker Compose**.

---

## Project Structure
```
docker/
│
├── client/ # Frontend (Node.js + Express)
│ ├── Dockerfile
│ ├── package.json
│ ├── index.js
│ └── public
│   ├── index.html
│   └── style.css
│
├── server/ # Backend (Flask)
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app.py
│
├── docker-compose.yml
└── .gitignore
```


## How to Run

### 1. Using Docker Compose

- docker-compose up --build
    - Frontend: http://localhost:3000
    - Backend: http://localhost:5000

### 2. Stop Containers

- docker-compose down

## Docker Hub Images
- Frontend: keyurpatil06/devops-client:latest
- Backend: keyurpatil06/devops-backend:latest