TeeKart/
├── backend/             # Flask app
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/            # React app (Vite or CRA)
│   ├── src/
│   └── Dockerfile
├── db/                  # PostgreSQL docker-compose or init
│   └── init.sql
├── jenkins/
│   └── Jenkinsfile
├── k8s/
│   ├── postgres.yaml
│   ├── backend.yaml
│   ├── frontend.yaml
│   ├── ingress.yaml
│   └── hpa.yaml
├── monitoring/
│   ├── prometheus.yaml
│   ├── grafana.yaml
│   └── loki.yaml
└── README.md
