<h1 align="center">💼 SALARY PREDICTION USING BANK DATA (ANN Regression)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit"/>
  <img src="https://img.shields.io/badge/TensorFlow-ANN-orange?style=flat-square&logo=tensorflow"/>
</p>

---

<h2>📘 Project Overview</h2>

<p>
This project predicts a customer's <strong>Estimated Salary</strong> using their banking and demographic details through a trained <strong>Artificial Neural Network (ANN)</strong> model.  
It leverages <strong>Streamlit</strong> for interactive visualization, enabling users to input customer data and instantly get a salary estimate based on trained machine learning patterns.
</p>

<p>
The model was trained on structured financial data and uses encoded categorical features and standardized numerical features for improved accuracy and performance.
</p>
<p>
Use Case : To maximize revenue using estimated salary prediction by bank to target oriented selling of products and services.
</p>

---

<h2>🎯 Key Features</h2>

<ul>
  <li>⚡ <strong>Instant salary prediction</strong> using a deep learning regression model</li>
  <li>📊 <strong>Interactive Streamlit interface</strong> for live prediction</li>
  <li>🧠 <strong>Encoders and Scalers</strong> applied to preprocess categorical and numerical data</li>
  <li>💾 <strong>Model and transformer persistence</strong> using Pickle and Keras</li>
  <li>🎨 <strong>Clean, modern UI</strong> with visual metrics and user-friendly sliders</li>
</ul>

---

<h2>🧩 Tech Stack</h2>

<table>
<tr>
  <td><strong>Language</strong></td>
  <td>Python 🐍</td>
</tr>
<tr>
  <td><strong>Framework</strong></td>
  <td>TensorFlow / Keras</td>
</tr>
<tr>
  <td><strong>Frontend</strong></td>
  <td>Streamlit</td>
</tr>
<tr>
  <td><strong>Data Preprocessing</strong></td>
  <td>scikit-learn (StandardScaler, LabelEncoder, OneHotEncoder)</td>
</tr>
<tr>
  <td><strong>Model Type</strong></td>
  <td>Artificial Neural Network (Regression)</td>
</tr>
</table>

---

<h2>🧠 Skills Demonstrated</h2>

<ul>
  <li>Deep Learning Model Building (Regression)</li>
  <li>TensorFlow / Keras Model Training and Evaluation</li>
  <li>Data Normalization and Encoding Techniques</li>
  <li>Model Deployment with Streamlit</li>
  <li>Clean Code and UI Design for ML Apps</li>
</ul>

---

---

<h2 align="center">🖥️ Application Interface</h2>

<p align="center">
  <img src="https://github.com/BIKRANT-RAWAT/SALARY-PREDICTION-BANK-DATA-ANN-REGRESSION/blob/main/images/interface.png" alt="App Interface" width="45%" style="border-radius:10px; margin:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="https://github.com/BIKRANT-RAWAT/SALARY-PREDICTION-BANK-DATA-ANN-REGRESSION/blob/main/images/prediction.png" alt="Prediction Page" width="45%" style="border-radius:10px; margin:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);"/>
</p>

---

<h2 align="center">📊 Model Insights & Graphs</h2>

<p align="center">
  <img src="https://github.com/BIKRANT-RAWAT/SALARY-PREDICTION-BANK-DATA-ANN-REGRESSION/blob/main/images/epoch_mae.png" alt="Mean Absolute Error Graph" width="45%" style="border-radius:10px; margin:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="https://github.com/BIKRANT-RAWAT/SALARY-PREDICTION-BANK-DATA-ANN-REGRESSION/blob/main/images/evaluation%20loss%20vs%20iteration.png" alt="Evaluation loss vs iteration graph" width="45%" style="border-radius:10px; margin:10px; box-shadow:0 4px 8px rgba(0,0,0,0.1);"/>
</p>

---


<h2>🚀 How to Run the Project</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/yourusername/Salary-Prediction-Using-Bank-Data.git</code></pre>
  </li>
  <li>Create a virtual environment and activate it:
    <pre><code>python -m venv venv
venv\\Scripts\\activate</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Run the Streamlit app:
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>

---

<h2>📂 Folder Structure</h2>

<pre>
📁 Salary-Prediction-Using-Bank-Data
│
├── app.py                        # Streamlit application
├── model.h5                      # Trained ANN regression model
├── scaler.pkl                    # StandardScaler object
├── label_encoder_gender.pkl      # LabelEncoder for gender
├── onehot_encoder_geo.pkl        # OneHotEncoder for geography
├── requirements.txt              # Dependencies list
└── README.md                     # Project documentation
</pre>

---

<h2>🤝 Collaboration</h2>

<p>
Contributions are highly welcome!  
If you have ideas for model optimization, feature enhancement, or UI improvements:
</p>

<ol>
  <li>Fork the repository 🍴</li>
  <li>Create a new branch (<code>feature/your-feature</code>)</li>
  <li>Commit your changes with clear messages</li>
  <li>Open a Pull Request 🚀</li>
</ol>

<p align="center">
  <a href="https://github.com/yourusername/Salary-Prediction-Using-Bank-Data/fork">
    <img src="https://img.shields.io/badge/Fork-Repository-blue?style=for-the-badge&logo=github"/>
  </a>
</p>

---

<h2>💡 Future Enhancements</h2>

<ul>
  <li>📈 Integrate interactive salary comparison charts</li>
  <li>🌐 Deploy the app on Streamlit Cloud or Hugging Face Spaces</li>
  <li>🔐 Add user authentication and secure input handling</li>
</ul>

---

<h2>🙏 Acknowledgements</h2>

<ul>
  <li>❤️ <strong>Krish Naik Sir</strong> for mentoring and guiding such beautiful project</li>
  <li>🧠 <strong>TensorFlow & Keras</strong> — for ANN model building</li>
  <li>📘 <strong>Scikit-learn</strong> — for preprocessing tools</li>
  <li>🚀 <strong>Streamlit</strong> — for a seamless interactive interface</li>
  <li>💡 The open-source community — for enabling transparent and reproducible ML research</li>
</ul>

---

<h3 align="center">⭐ If you found this project helpful, give it a star on GitHub! ⭐</h3>
<p align="center">Made with ❤️ using Streamlit & TensorFlow</p>
