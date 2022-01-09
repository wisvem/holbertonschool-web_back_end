import { createClient } from 'redis';

(async () => {
  const client = createClient();
  client.on('error', (err) => console.log('Redis client not connected to the server:', err));
  client.on('ready', () => console.log('Redis client connected to the server'));
  function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
      if (err) throw err;
      console.log(reply);
    });
    return (schoolName, value);
  }
  function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
      if (err) throw err;
      console.log(reply);
    });
  }
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})();
