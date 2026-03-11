# Flask DevSecOps Pipeline

Minimal Flask app with a reusable GitHub Actions DevSecOps pipeline.

## Tech Stack

- Python 3.12+
- Flask
- Gunicorn
- Docker
- GitHub Actions

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python app.py
```

App URL: `http://localhost:5000`

## Run Tests and Quality Checks

```bash
pytest -q
black --check --workers 1 app.py test_app.py
isort --check-only app.py test_app.py
flake8 --jobs=1 app.py test_app.py
bandit -q -r app.py
pip-audit -r requirements.txt --strict
```

## Docker

```bash
docker build -t flask-devsecops-pipeline:local .
docker run --rm -p 5000:5000 flask-devsecops-pipeline:local
```

## GitHub Actions Pipeline

Parent workflow: `.github/workflows/devsecops-pipeline.yml`

It orchestrates:

- code quality
- secret scan
- dependency scan
- Dockerfile lint
- tests
- image build/push (main only)
- image scan (main only)
- deploy (main only)

## Required GitHub Secrets

- `DEPLOY_HOST`
- `DEPLOY_USER`
- `DEPLOY_SSH_KEY`
- `REGISTRY_USER`
- `REGISTRY_TOKEN`
