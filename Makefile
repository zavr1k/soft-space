compose: prepare
		docker compose -f docker-compose.yaml up --build -d

compose-down:
		docker compose down

lint:
	poetry run flake8 src/ tests/

prepare:
	cp -n example.env .env || true
