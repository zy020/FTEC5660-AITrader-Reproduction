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
