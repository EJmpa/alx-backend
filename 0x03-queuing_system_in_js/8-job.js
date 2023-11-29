import kue from 'kue';

/**
 * Creates jobs in the Kue queue for push notifications.
 * @param {Array} jobs - Array of job objects.
 * @param {Object} queue - Kue queue.
 */
const createPushNotificationsJobs = (jobs, queue) => {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Process each job in the array
  jobs.forEach((jobData) => {
    // Create a new job in the push_notification_code_3 queue
    const job = queue.create('push_notification_code_3', jobData);

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
};

export default createPushNotificationsJobs;

