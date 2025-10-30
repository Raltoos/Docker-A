const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = 3000;
const BACKEND_URL = 'http://backend:5000';

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static('public'));

// Routes
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/submit-form', async (req, res) => {
    try {
        const response = await axios.post(`${BACKEND_URL}/api/submit`, req.body);
        res.json({
            success: true,
            message: 'Form submitted successfully!',
            data: response.data
        });
    } catch (error) {
        console.error('Error submitting form:', error.message);
        res.status(500).json({
            success: false,
            message: 'Error submitting form',
            error: error.message
        });
    }
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Frontend server running on port ${PORT}`);
});