// Import necessary modules
import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Array of jobs
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// Process each job in the array
jobs.forEach((jobData, index) => {
  // Create a new job in the push_notification_code_2 queue
  const job = queue.create('push_notification_code_2', jobData);

  // Handle successful job creation
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Handle job failure
  job.on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  // Handle job progress
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });

  // Save the job to the queue
  job.save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });
});

// Log a message when the script completes
console.log('Job creation script completed');

