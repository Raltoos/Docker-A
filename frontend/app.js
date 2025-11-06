const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
// default to localhost for local dev; docker-compose will inject BACKEND_URL=http://backend:5000
const BACKEND_URL = process.env.BACKEND_URL || 'http://127.0.0.1:5000/';

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Home page: shows form
app.get('/', (req, res) => {
    res.render('index');
});

// Receive form POST from browser; Forward to backend service (server-side)
app.post('/submit', async (req, res) => {
    try {
        const payload = req.body; // { name, email, message }
        // Forward as JSON to backend API
        const response = await axios.post(`${BACKEND_URL}/process`, payload, { timeout: 10000 });
        res.render('result', { result: response.data });
    } catch (err) {
        console.error('Error forwarding to backend:', err.message || err);
        res.status(500).send('Error communicating with backend: ' + (err.message || err));
    }
});

app.listen(PORT, () => {
    console.log(`Frontend listening on port ${PORT} — forwarding backend requests to ${BACKEND_URL}`);
});
