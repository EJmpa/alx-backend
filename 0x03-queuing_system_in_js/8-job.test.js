import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    // Create a Kue queue in test mode
    kue.createQueue({ redis: { port: 6379, host: '127.0.0.1', db: 3 } });
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  after(() => {
    // Clear the queue and exit test mode
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    // Call the function with a non-array argument
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    // Create jobs array
    const jobs = [
      { phoneNumber: '1234567890', message: 'Test message 1' },
      { phoneNumber: '9876543210', message: 'Test message 2' },
    ];

    // Call the function to create jobs
    createPushNotificationsJobs(jobs, queue);

    // Assert that jobs were added to the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Assert that job creation messages were logged
    // expect(queue.testMode.jobs[0].log[0]).to.equal('Notification job created: 1');
    // expect(queue.testMode.jobs[1].log[0]).to.equal('Notification job created: 2');
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
