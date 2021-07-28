install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	py -m pip install dist/hexlet_code-0.1.3-py3-none-any.whl

lint:
	poetry run flake8 brain_games
