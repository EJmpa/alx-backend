import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.toString()}`);
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
}

const displaySchoolValue = async (schoolName) => {
    const getAsync = promisify(client.get).bind(client);
    console.log(await getAsync(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
