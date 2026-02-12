# uv run ray metrics launch-prometheus # not working correctly
echo RAY_ENABLE_WINDOWS_OR_OSX_CLUSTER=$RAY_ENABLE_WINDOWS_OR_OSX_CLUSTER
echo Registering on RAY_API_SERVER_IP=$RAY_API_SERVER_IP with RAY_API_SERVER_PORT=$RAY_API_SERVER_PORT
RAY_ENABLE_WINDOWS_OR_OSX_CLUSTER=1 uv run ray start \
                            --head \
                            --port=$RAY_API_SERVER_PORT \
                            --node-ip-address $RAY_API_SERVER_IP \
                            --dashboard-host=0.0.0.0 \
                            --dashboard-port=8265 \
                            --ray-client-server-port=10001