uv sync
# uv run ray metrics launch-prometheus # not working correctly
uv run ray start --head --port=6379 --dashboard-host=0.0.0.0 --dashboard-port=8265