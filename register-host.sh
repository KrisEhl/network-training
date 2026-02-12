# uv run ray metrics launch-prometheus # not working correctly
echo RAY_ENABLE_WINDOWS_OR_OSX_CLUSTER=$RAY_ENABLE_WINDOWS_OR_OSX_CLUSTER
RAY_ENABLE_WINDOWS_OR_OSX_CLUSTER=1 uv run ray start --head --port=6379 --dashboard-host=0.0.0.0 --dashboard-port=8265