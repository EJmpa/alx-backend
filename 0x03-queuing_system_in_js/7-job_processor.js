// Import the required modules
import kue from 'kue';

// Create a new job queue
const queue = kue.createQueue();

// Define an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Define a function to send a notification
function sendNotification(phoneNumber, message, job, done) {
  // Start the job's progress at 0%
  job.progress(0, 100);

  // If the phone number is blacklisted, fail the job with an error message
  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    // Otherwise, update the job's progress to 50% and log a message
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    // Mark the job as done
    done();
  }
}

// Set up a process to handle new jobs on the 'push_notification_code_2' queue
// The process can handle two jobs concurrently
queue.process('push_notification_code_2', 2, function(job, done){
  // For each new job, call the sendNotification function with the job's data and the done callback
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

