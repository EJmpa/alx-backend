# Queuing System in JavaScript

## Requirements

- Ubuntu 18.04
- Node 12.x
- Redis 5.0.7

## Installation

1. **Install Redis:**

    ```bash
    # Download and extract Redis
    $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
    $ tar xzf redis-6.0.10.tar.gz
    $ cd redis-6.0.10

    # Compile Redis
    $ make

    # Start Redis in the background
    $ src/redis-server &

    # Check if the server is working
    $ src/redis-cli ping

    # Use Redis client to set the value "School" for the key "Holberton"
    $ src/redis-cli set Holberton School

    # Verify the value is set
    $ src/redis-cli get Holberton
    # Should return "School"
    ```

2. **Install project dependencies:**
   ```bash
   # Any additional setup instructions
