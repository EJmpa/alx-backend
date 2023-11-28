// Import necessary modules
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle the connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle the error event
client.on('error', function(err) {
    console.log(`Redis client not connected to the server: ${err.toString()}`);
});

// Close the Redis connection on process exit
//  process.on('SIGINT', () => {
//  client.quit();
// });

// Uncomment the following line if you want to explicitly close the connection after a certain time
// setTimeout(() => client.quit(), 5000);
