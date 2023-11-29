// Import necessary modules
import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Function to send a notification
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process jobs in the push_notification_code queue
queue.process('push_notification_code', (job, done) => {
  // Extract phone number and message from the job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function
  sendNotification(phoneNumber, message);

  // Mark the job as completed
  done();
});

// Handle any errors that occur during job processing
queue.on('error', (err) => {
  console.error(`Error in job processing: ${err}`);
});

// Log a message when the queue is ready to process jobs
console.log('Worker is ready to process jobs');

