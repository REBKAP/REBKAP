#!/bin/bash
# entrypoint.sh

# Run database migrations
echo "Running database migrations..."
flask db upgrade

# Start your application
exec "$@"
