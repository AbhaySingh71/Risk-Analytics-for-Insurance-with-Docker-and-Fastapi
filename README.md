<h1> Risk Analytics for Insurance — FastAPI, Docker & AWS Deployment</h1>
<span class="badge">FastAPI-Insurance_Analytics</span>

<p>
  A full-stack <strong>API-first project</strong> that demonstrates how to build and deploy a
  <strong>FastAPI-based prediction service</strong> using <strong>Docker</strong> and <strong>AWS EC2</strong>.
  This project is not about ML model building, but focuses on the <strong>end-to-end deployment pipeline</strong> including:
</p>

<ul>
  <li>🚀 FastAPI for high-performance backend API</li>
  <li>🐳 Docker for containerization</li>
  <li>☁️ AWS EC2 for production deployment</li>
  <li>🌐 Streamlit frontend integration</li>
  <li>🔁 Model integration to serve predictions as an API</li>
</ul>

<h2>📌 Project Objective</h2>
<p>
  To demonstrate an end-to-end deployment pipeline using <strong>FastAPI</strong> for API development,
  <strong>Docker</strong> for containerization, and <strong>AWS EC2</strong> for hosting a cloud-based prediction service.
</p>
<p><em>The ML model (predicting insurance premium category) is pre-trained and used only for demonstration purposes.</em></p>

<h2>🧱 Tech Stack</h2>
<table>
  <tr><th>Layer</th><th>Tool/Tech</th><th>Purpose</th></tr>
  <tr><td>🧠 Model</td><td>sklearn</td><td>Predict insurance premium category</td></tr>
  <tr><td>⚙️ Backend</td><td><a href="https://fastapi.tiangolo.com" target="_blank">FastAPI</a></td><td>RESTful API creation</td></tr>
  <tr><td>📦 Container</td><td><a href="https://www.docker.com" target="_blank">Docker</a></td><td>Packaging application</td></tr>
  <tr><td>☁️ Cloud</td><td><a href="https://aws.amazon.com/ec2/" target="_blank">AWS EC2</a></td><td>Hosting FastAPI + Docker</td></tr>
  <tr><td>🌐 Frontend</td><td><a href="https://streamlit.io" target="_blank">Streamlit</a></td><td>Simple interactive UI</td></tr>
</table>

<h2>🗂️ Project Structure</h2>
<pre><code>
├── app.py               # FastAPI application
├── frontend.py          # Streamlit UI
├── model/               # Pretrained model + loading logic
│   └── model.pkl
├── config/              # Configs for API behavior
├── schema/              # Pydantic data validation schemas
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration for app
├── .dockerignore        # Files to ignore in Docker build
└── README.md            # This file
</code></pre>

<h2>🚀 How to Run This Project</h2>

<h3>1️⃣ Clone the Repository</h3>
<pre><code>git clone https://github.com/AbhaySingh71/Risk-Analytics-for-Insurance-with-Docker-and-Fastapi.git
cd Risk-Analytics-for-Insurance-with-Docker-and-Fastapi</code></pre>

<h3>2️⃣ Create Virtual Environment (Optional)</h3>
<pre><code>python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt</code></pre>

<h3>3️⃣ Run FastAPI App</h3>
<pre><code>uvicorn app:app --reload</code></pre>

<h3>4️⃣ Launch Streamlit Frontend (Optional)</h3>
<pre><code>streamlit run frontend.py</code></pre>

<h3>5️⃣ Dockerize and Run</h3>
<pre><code>docker build -t insurance-api .
docker run -d -p 8000:8000 insurance-api</code></pre>

<h2>☁️ AWS EC2 Deployment Instructions</h2>

<ol>
  <li><strong>Create an EC2 instance</strong> (Ubuntu)</li>
  <li><strong>Connect to EC2 instance</strong>:
    <pre><code>ssh ubuntu@your-ec2-ip</code></pre>
  </li>
  <li><strong>Run the following setup commands:</strong>
    <pre><code>sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
exit</code></pre>
  </li>
  <li><strong>Reconnect to EC2 instance</strong>:
    <pre><code>ssh ubuntu@your-ec2-ip</code></pre>
  </li>
  <li><strong>Run Docker container</strong>:
    <pre><code>docker pull abhaysingh71/fastapi-insurance-premium-prediction:latest
docker run -p 8000:8000 abhaysingh71/fastapi-insurance-premium-prediction</code></pre>
  </li>
  <li><strong>Update Security Group:</strong> Open port <code>8000</code> in EC2 security group settings</li>
  <li><strong>Test the API</strong>:
    <br>Visit: <code>http://your-ec2-ip:8000/docs</code>
  </li>
  <li><strong>Update frontend</strong>: In <code>frontend.py</code>, change:
    <pre><code>API_URL = "http://your-ec2-ip:8000/predict"</code></pre>
  </li>
</ol>

<h2>🧪 API Docs</h2>
<ul>
  <li><a href="http://localhost:8000/docs" target="_blank">Swagger UI</a></li>
  <li><a href="http://localhost:8000/redoc" target="_blank">ReDoc</a></li>
</ul>

<h2>📸 Streamlit Preview</h2>
<pre><code>streamlit run frontend.py</code></pre>

<h2>🛠️ Features</h2>
<ul>
  <li>✅ Clean FastAPI backend</li>
  <li>✅ Docker containerized setup</li>
  <li>✅ AWS EC2 deployable</li>
  <li>✅ Simple Streamlit UI</li>
  <li>✅ Organized code structure</li>
</ul>

<h2>📢 Disclaimer</h2>
<p>
  <strong>This project is not focused on ML model training.</strong><br>
  It demonstrates API development, Dockerization, and cloud deployment.
</p>

<h2>👨‍💻 Author</h2>
<ul>
  <li><strong>Abhay Singh</strong></li>
  <li>Email: <a href="mailto:abhaysingh71711@gmail.com">abhaysingh71711@gmail.com</a></li>
  <li>LinkedIn: <a href="https://www.linkedin.com/in/abhay-singh-050a5b293/" target="_blank">Abhay's LinkedIn</a></li>
  <li>GitHub: <a href="https://github.com/AbhaySingh71" target="_blank">AbhaySingh71</a></li>
</ul>
</body>
</html>
