function apikey(req, res, next) {
    const api_key = '12345'; // Your API key

    // Extract API key from query parameters
    const providedApiKey = req.query.api_key;

    // Check if API key is provided and matches the expected key
    if (providedApiKey && providedApiKey === api_key) {
        // If the API key is valid, call the next middleware in the chain
        res.json([
            {
                id:"123",
                prodecj:'chrome'
            },
            {
                id:"124",
                prodecj:'firefox'
            },
            {
                id:"125",
                prodecj:'compass'
            }
        ])
        next();
    } else {
        // If the API key is missing or invalid, send an error response
        res.status(401).json({ error: 'Unauthorized' });
    }
    console.log(req.query)
}
module.exports = apikey;
