
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
  <li>Created Live Demo Dashboard link using Hugging face hub and space</li>
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
<span class="badge">Hugging Face Space</span>
<hr />

<h2>Usage</h2>
<p>Clone the repo and run the backend service to start the chatbot. Access the web via hugging face .</p>
<pre><code>git clone https://github.com/Anup-Sarkar-DD/AI-Mental-health-chatbot.git
cd AI-Mental-health-chatbot
uvicorn api.main:app --reload
</code></pre>

<hr />

<h2>Links</h2>
<ul>
  <li><a href="https://github.com/Anup-Sarkar-DD/AI-Mental-health-chatbot" target="_blank">GitHub Repository</a></li>
  <li><a href="https://huggingface.co/spaces/AnupSarkarDD/mental-health-chatbot">Hugging Face Repo</a></li>   
  <li><a href="https://anup-sarkar-dd.github.io/AnupTheAIMLVisionary.github.io/" target="_blank">My Portfolio</a></li>
</ul>

</body>
</html>
