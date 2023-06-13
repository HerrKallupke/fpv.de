const express = require('express');

const app = express();

app.use((req, res, next) => {
  if (!req.secure) {
    return res.redirect(`https://${req.headers.host}${req.url}`);
  }
  next();
});

app.listen(80, () => {
  console.log('Server listening on port 80');
});
