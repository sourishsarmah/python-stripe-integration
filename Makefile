#########################
# DEFAULTS
#########################
GUINICORN_PORT = 8000
GUINICORN_WORKERS = 1
GUINICORN_TIME_OUT = 123

#################################################################################
# COMMANDS                                                                      #
#################################################################################
format:
	set -e
	isort --recursive  --force-single-line-imports app
	autoflake --recursive --remove-all-unused-imports --remove-unused-variables --in-place app
	black app
	isort app

lint:
	set -e
	set -x
	flake8 app --exclude=app/core/config.py
	mypy app
	black --check app --diff
	isort --recursive --check-only app

run_dev_server:
	uvicorn app.main:app --reload

run_server:
	uvicorn app.main:app --reload