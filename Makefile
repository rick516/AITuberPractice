# pyenv前提のpythonバージョン変更コマンド
# 起動はsource venv/bin/activate
setup-python:
	@echo "Setting up Python virtual environment"
	@python_version=$$(python -c 'import sys; print(".".join(map(str, sys.version_info[:3])))'); \
	if [ $$python_version != "3.11.4" ]; then \
		echo "Python version is not 3.11.4. Changing version using pyenv..."; \
		pyenv install 3.11.4; \
		pyenv local 3.11.4; \
	fi; \
	python -m venv venv

# テスト実行
test:
	@echo "Running tests with coverage"
	@if [ -z "$(file)" ]; then \
		coverage run --source=src -m pytest; \
	else \
		coverage run --source=src -m pytest $(file); \
	fi; \
	coverage report -m