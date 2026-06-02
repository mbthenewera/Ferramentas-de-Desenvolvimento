import express from 'express';
import crypto from 'node:crypto';

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json({ limit: '1mb' }));

app.get('/health', (_request, response) => {
  response.json({ status: 'ok', service: 'devtools-api' });
});

app.post('/hash', (request, response) => {
  const { value } = request.body;

  if (typeof value !== 'string' || value.length === 0) {
    return response.status(400).json({ error: 'value must be a non-empty string' });
  }

  const hash = crypto.createHash('sha256').update(value).digest('hex');
  return response.json({ algorithm: 'sha256', hash });
});

app.post('/text-summary', (request, response) => {
  const { text } = request.body;

  if (typeof text !== 'string') {
    return response.status(400).json({ error: 'text must be a string' });
  }

  const words = text.trim() ? text.trim().split(/\s+/).length : 0;
  const lines = text.length ? text.split('\n').length : 0;

  return response.json({
    characters: text.length,
    words,
    lines
  });
});

app.post('/extension-stats', (request, response) => {
  const { files } = request.body;

  if (!Array.isArray(files)) {
    return response.status(400).json({ error: 'files must be an array' });
  }

  const stats = files.reduce((acc, file) => {
    if (typeof file !== 'string') return acc;
    const match = file.toLowerCase().match(/\.[a-z0-9]+$/);
    const extension = match ? match[0] : '[no-extension]';
    acc[extension] = (acc[extension] || 0) + 1;
    return acc;
  }, {});

  return response.json({ total: files.length, stats });
});

app.listen(port, () => {
  console.log(`DevTools API running on port ${port}`);
});
