compose: prepare
		docker compose -f docker-compose.yaml up --build -d

compose-down:
		docker compose down

compose-dev:
		docker-compose up --build

lint:
	poetry run flake8 src/ tests/

prepare:
	cp -n .example.env .env || true

test: compose-test-up compose-test compose-test-down

compose-test-up:
		docker compose -f docker-compose-test.yaml -p test-softspace up -d --build

compose-test:
		docker exec test-softspace-app poetry run flake8 src/ tests/ || true
		docker exec test-softspace-app poetry run pytest -s tests/ || true

compose-test-down:
		docker compose -f docker-compose-test.yaml -p test-softspace down