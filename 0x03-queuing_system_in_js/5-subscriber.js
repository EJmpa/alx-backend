// Import necessary modules
import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient();

// Handle the connection event
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle the error event
subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the channel
subscriber.subscribe('holberton school channel');

// Handle incoming messages
subscriber.on('message', (channel, message) => {
  console.log(`Message received on channel ${channel}: ${message}`);

  // Check if the message is KILL_SERVER
  if (message === 'KILL_SERVER') {
    // Unsubscribe and quit
    subscriber.unsubscribe();
    subscriber.quit();
  }
});

