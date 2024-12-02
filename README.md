# Drones Simulation

## Content

`TODO`:

- complete `Invaded` and `OnMission` behaviors in `src/drones_simulation/services/behaviors`.

- add a graphical way (animated plot) to see drones' positions changing.

- add connection intensity variable in `Drone`. Besides, there must be a region next to its companions that a drone need to stay in to maintain a good connection intensity.

## Running

Firstly, execute Docker (on Windows, you must open Docker Desktop).

Then, go to project's root directory (where the `docker-compose.yml` file is) and run on terminal:

- `docker compose up`

## Install Poetry (for dev)

- https://python-poetry.org/docs/#installing-with-the-official-installer

After installing `poetry`, run on terminal:

- `poetry install`
- `pre-commit install`

## References

- Python Sockets (TCP): https://realpython.com/python-sockets/
