// Import necessary modules
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle the connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle the error event
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Create Hash using hset
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display Hash using hgetall
client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.error(`Error retrieving hash: ${err}`);
  } else {
    console.log(reply);
  }
});
