// 100-seat.js

import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();
const queue = kue.createQueue();

// Convert Redis functions to use Promises
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);
const hgetAsync = promisify(client.hget).bind(client);

// Initialize the number of available seats
const initialNumberOfSeats = 50;
setAsync('available_seats', initialNumberOfSeats);

// Initialize reservationEnabled to true
let reservationEnabled = true;

// Function to reserve a seat
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

// Function to get the current number of available seats
const getCurrentAvailableSeats = async () => {
  return parseInt(await getAsync('available_seats'), 10);
};

// Express route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

// Express route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Express route to process the queue and decrease available seats
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();

    if (currentAvailableSeats <= 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      reservationEnabled = true;
      await reserveSeat(currentAvailableSeats - 1);

      if (currentAvailableSeats - 1 === 0) {
        reservationEnabled = false;
      }

      done();
    }
  });
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

