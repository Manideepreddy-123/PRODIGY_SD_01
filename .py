<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Temperature Converter 🌡️</title>
  <style>
    body {
      font-family: "Poppins", sans-serif;
      background: linear-gradient(135deg, #ffecd2, #fcb69f);
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 0;
    }
    .converter-container {
      background: #fff;
      border-radius: 20px;
      box-shadow: 0 5px 20px rgba(0,0,0,0.2);
      padding: 40px;
      text-align: center;
      width: 350px;
    }
    h1 {
      color: #333;
      font-size: 24px;
    }
    input, select, button {
      padding: 10px;
      font-size: 16px;
      border-radius: 8px;
      border: 1px solid #aaa;
      margin-top: 10px;
      width: 100%;
      box-sizing: border-box;
    }
    button {
      background: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
      transition: background 0.3s;
    }
    button:hover {
      background: #45a049;
    }
    .result {
      margin-top: 20px;
      font-weight: bold;
      color: #222;
    }
  </style>
</head>
<body>
  <div class="converter-container">
    <h1>🌡️ Temperature Converter</h1>
    <input type="number" id="tempInput" placeholder="Enter temperature" />
    <select id="unitSelect">
      <option value="c">Celsius (°C)</option>
      <option value="f">Fahrenheit (°F)</option>
      <option value="k">Kelvin (K)</option>
    </select>
    <button onclick="convertTemperature()">Convert</button>
    <div class="result" id="result"></div>
  </div>

  <script>
    function convertTemperature() {
      const value = parseFloat(document.getElementById("tempInput").value);
      const unit = document.getElementById("unitSelect").value;
      const resultDiv = document.getElementById("result");

      if (isNaN(value)) {
        resultDiv.textContent = "❌ Please enter a valid number!";
        return;
      }

      let resultText = "";

      if (unit === "c") {
        const f = (value * 9/5) + 32;
        const k = value + 273.15;
        resultText = `${value}°C = ${f.toFixed(2)}°F | ${k.toFixed(2)}K`;
      } else if (unit === "f") {
        const c = (value - 32) * 5/9;
        const k = c + 273.15;
        resultText = `${value}°F = ${c.toFixed(2)}°C | ${k.toFixed(2)}K`;
      } else if (unit === "k") {
        const c = value - 273.15;
        const f = (c * 9/5) + 32;
        resultText = `${value}K = ${c.toFixed(2)}°C | ${f.toFixed(2)}°F`;
      }

      resultDiv.textContent = resultText;
    }
  </script>
</body>
</html>
