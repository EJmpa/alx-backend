// Import necessary modules
import redis from 'redis';

// Create a Redis client
const publisher = redis.createClient();

// Handle the connection event
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle the error event
publisher.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Function to publish a message after a given time
const publishMessage = (message, time) => {
  console.log(`About to send ${message}`);
  
  // Publish the message after the specified time
  setTimeout(() => {
    publisher.publish('holberton school channel', message);
  }, time);
};

// Call the publishMessage function with different messages and times
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);

