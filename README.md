# AI-Trader: Reproduction and Modification (FTEC5660)

This repository contains the reproducibility report and code modification for the "AI-Trader" agentic system, completed as part of the FTEC5660 (Agentic AI for Business and FinTech) course assignment.

## 1. Project Overview
This project evaluates the performance of an autonomous trading LLM agent on a subset of the U.S. market (NASDAQ-100). The evaluation focuses on a highly volatile 30-day period (Oct 1, 2025 - Nov 7, 2025) to test the agent's risk management capabilities.

**Base Models Evaluated:**
* DeepSeek-v3.1-terminus (Baseline)
* GLM-4.6 (Baseline & Modified)

## 2. Modification Details
The native GLM-4.6 model struggled with raw financial data. I implemented a scoped modification targeting the agent's tool policy to fix this:
1. **Tool-Layer Enhancement:** Integrated a `financial_calculator` using a safe Python `eval()` environment, offloading floating-point arithmetic from the LLM.
2. **Prompt Engineering:** Granted the agent autonomy to evaluate intraday spreads using aggregated OHLCV data by adding the instruction: *"Use math tools to calculate relevant indicators from the price data to guide your decisions."*

---

## 3. Prerequisites
* **Python:** 3.10+
* **API Keys Required:**
  * **OpenAI API:** For AI model inference (or DeepSeek/GLM compatible proxies).
  * **Alpha Vantage:** For NASDAQ-100 and cryptocurrency data.
  * **Jina AI:** For market information search.

---

## 4. Installation Steps

**Step 1: Clone the Project**
```bash
git clone [https://github.com/HKUDS/AI-Trader.git](https://github.com/HKUDS/AI-Trader.git)
cd AI-Trader
```

**Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Configure Environment Variables**
Copy the example config and edit it with your personal credentials. DO NOT commit this .env file to your repository.
```bash
cp .env.example .env
```
Edit your .env file to include the following configurations:
```bash
# 🤖 AI Model API Configuration
OPENAI_API_BASE=[https://your-openai-proxy.com/v1](https://your-openai-proxy.com/v1)
OPENAI_API_KEY=your_openai_key

# 📊 Data Source Configuration
ALPHAADVANTAGE_API_KEY=your_alpha_vantage_key  # For NASDAQ-100 & Crypto
JINA_API_KEY=your_jina_api_key
TUSHARE_TOKEN=your_tushare_token               # For A-Share

# ⚙️ System Configuration
RUNTIME_ENV_PATH=./runtime_env.json            # Absolute path recommended

# 🌐 Service Port Configuration
MATH_HTTP_PORT=8000
SEARCH_HTTP_PORT=8001
TRADE_HTTP_PORT=8002
GETPRICE_HTTP_PORT=8003
CRYPTO_HTTP_PORT=8005

# 🧠 AI Agent Configuration
AGENT_MAX_STEP=30                              # Maximum reasoning steps
```
## 5. Run Steps
**Step 1: Fetch Market Data**
Retrieve the latest daily prices for the NASDAQ-100 and merge them into a unified format:
```bash
cd data
python get_daily_price.py
python merge_jsonl.py
cd ..
```
**Step 2: Start MCP Background Services**
The system requires these background services to execute tools (Math, Search, Trade):
```bash
cd ./agent_tools
python start_mcp_services.py
cd ..
```
**Step 3: Run the Agent Pipeline**
Open a new terminal window (keep the MCP services running) and execute the main trading logic:
```bash
# Option A: Run with default configuration
python main.py

# Option B: Run with a specific US market configuration
python main.py configs/default_config.json
```
**Step 4: Evaluate Metrics**
Once the trading session is completed, use the evaluation scripts to analyze risk-adjusted performance:
```bash
cd tools
python3 calculate_metrics.py ../data/agent_data/GLM-4.6/position/position.jsonl --data-dir ../data --is-hourly
python3 plot_metrics.py --output-dir ../plots --separate-plots
cd ..
```
