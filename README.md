<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>AI Mental Health Chatbot - README</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 800px; margin: auto; padding: 2rem; line-height: 1.6; background: #f9f9f9; }
    h1, h2, h3 { color: #2c3e50; }
    a { color: #3498db; text-decoration: none; }
    a:hover { text-decoration: underline; }
    pre { background: #2d2d2d; color: #f8f8f2; padding: 1rem; overflow-x: auto; border-radius: 5px; }
    ul { margin-left: 1rem; }
    .badge { display: inline-block; background: #3498db; color: white; padding: 0.2em 0.5em; border-radius: 4px; font-size: 0.85rem; margin-right: 0.5em; }
    .button { display: inline-block; background: #2ecc71; color: white; padding: 0.5em 1em; border-radius: 5px; margin-top: 1rem; text-decoration: none; font-weight: bold; }
    .button:hover { background: #27ae60; }
    hr { border: 0; border-top: 1px solid #ddd; margin: 2rem 0; }
  </style>
</head>
<body>

<h1>MindEase: AI Mental Health Chatbot</h1>
<p><strong>Overview:</strong> MindEase is a conversational AI chatbot powered by a fine-tuned BlenderBot model, designed for empathetic and safe mental health dialogue. The model was trained on the MentalChat16K dataset incorporating advanced preprocessing and contextual optimization techniques.</p>

<hr />

<h2>Features</h2>
<ul>
  <li>Fine-tuned BlenderBot-400M-distill model for empathetic responses</li>
  <li>Text preprocessing, tokenization, and conversational context optimization</li>
  <li>FastAPI backend serving the chatbot model</li>
  <li>Interactive web-based chat interface using HTML, CSS, and JavaScript</li>
  <li>Lightweight CPU optimized inference for wider accessibility</li>
</ul>

<hr />

<h2>The Challenge</h2>
<p>Ensuring consistent empathy and coherent dialogue across sensitive mental health topics, while balancing response diversity with safety. Additionally, optimizing model training and inference to operate efficiently on CPU environments.</p>

<hr />

<h2>The Solution</h2>
<p>Implemented a fine-tuning pipeline using Hugging Face Transformers and evaluation metrics like ROUGE-L and F1-score. Integrated FastAPI as backend with a responsive frontend chat UI, enabling scalable, lightweight deployment with emphasis on safe and emotionally adaptive responses.</p>

<hr />

<h2>Tech Stack</h2>
<span class="badge">Python</span>
<span class="badge">PyTorch</span>
<span class="badge">Hugging Face Transformers</span>
<span class="badge">FastAPI</span>
<span class="badge">JavaScript</span>
<span class="badge">HTML/CSS</span>

<hr />

<h2>Usage</h2>
<p>Clone the repo and run the backend service to start the chatbot. Access the web frontend to interact with the AI mental health assistant.</p>
<pre><code>git clone https://github.com/Anup-Sarkar-DD/AI-Mental-health-chatbot.git
cd AI-Mental-health-chatbot
uvicorn api.main:app --reload
</code></pre>

<hr />

<!-- <h2>Links</h2>
<ul>
  <li><a href="https://github.com/Anup-Sarkar-DD/AI-Mental-health-chatbot" target="_blank">GitHub Repository</a></li>
  <li><a href="https://your-portfolio-url.com" target="_blank">My Portfolio</a></li>
</ul>

<hr />

<p>Feel free to open issues, fork or contribute. Reach out for collaboration!</p> -->

</body>
</html>
