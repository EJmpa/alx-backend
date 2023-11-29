// Import the required modules
import express from 'express';
import kue from 'kue';
import { promisify } from 'util';
import redis from 'redis';

// Define an array of products
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// Define a function to get a product by its ID
const getItemById = (id) => listProducts.find((item) => item.id === id);

// Create a Redis client and promisify the get and set methods
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Define a function to reserve stock for a product
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

// Define a function to get the current reserved stock for a product
const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? stock : getItemById(itemId).stock;
};

// Create an Express application
const app = express();
// Create a Kue queue
const queue = kue.createQueue();

// Define a route to get a list of all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Define a route to get a product by its ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);

  res.json({
    ...item,
    currentQuantity,
  });
});

// Define a route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  let currentQuantity = await getCurrentReservedStockById(itemId);

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, --currentQuantity);

  res.json({ status: 'Reservation confirmed', itemId });
});

// Start the server
app.listen(1245, () => {
  console.log('Server running on port 1245');
});

