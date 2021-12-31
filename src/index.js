const express = require('express');
const app = express();
pool = require('./database.js');

// Start the app
app.use(express.json());

// CRUD Functions

// Create (post)
app.post('/todos', async (req, res) => {
    console.log('Oooh wee we tryin');
    try {
        // Try to add the new todo
        const { description } = req.body;
        const newTodo = await pool.query(
            'INSERT INTO todo (description) VALUES ($1) RETURNING *',
            [description]
        );
    } catch (err) {
        console.error(err.message);
    }
});


app.listen(3000, () => {
    console.log('Server on port 3000');
})
