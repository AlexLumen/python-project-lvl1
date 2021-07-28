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

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime
