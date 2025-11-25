# Indian Stock Exchange Api2 MCP Server

[English](./README_EN.md) | [简体中文](./README.md) | 繁體中文

## 🚀 使用 EMCP 平台快速體驗

**[EMCP](https://sit-emcp.kaleido.guru)** 是一個強大的 MCP 伺服器管理平台，讓您無需手動配置即可快速使用各種 MCP 伺服器！

### 快速開始：

1. 🌐 造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 註冊並登入帳號
3. 🎯 進入 **MCP 廣場**，瀏覽所有可用的 MCP 伺服器
4. 🔍 搜尋或找到本伺服器（`bach-indian_stock_exchange_api2`）
5. 🎉 點擊 **「安裝 MCP」** 按鈕
6. ✅ 完成！即可在您的應用中使用

### EMCP 平台優勢：

- ✨ **零配置**：無需手動編輯配置檔案
- 🎨 **視覺化管理**：圖形介面輕鬆管理所有 MCP 伺服器
- 🔐 **安全可靠**：統一管理 API 金鑰和認證資訊
- 🚀 **一鍵安裝**：MCP 廣場提供豐富的伺服器選擇
- 📊 **使用統計**：即時查看服務調用情況

立即造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 開始您的 MCP 之旅！


---

## 簡介

這是一個使用 [FastMCP](https://fastmcp.wiki) 自動生成的 MCP 伺服器，用於存取 Indian Stock Exchange Api2 API。

- **PyPI 套件名**: `bach-indian_stock_exchange_api2`
- **版本**: 1.0.0
- **傳輸協定**: stdio


## 安装

### 从 PyPI 安装:

```bash
pip install bach-indian_stock_exchange_api2
```

### 从源码安装:

```bash
pip install -e .
```

## 运行

### 方式 1: 使用 uvx（推荐，无需安装）

```bash
# 运行（uvx 会自动安装并运行）
uvx --from bach-indian_stock_exchange_api2 bach_indian_stock_exchange_api2

# 或指定版本
uvx --from bach-indian_stock_exchange_api2@latest bach_indian_stock_exchange_api2
```

### 方式 2: 直接运行（开发模式）

```bash
python server.py
```

### 方式 3: 安装后作为命令运行

```bash
# 安装
pip install bach-indian_stock_exchange_api2

# 运行（命令名使用下划线）
bach_indian_stock_exchange_api2
```

## 配置

### API 認證

此 API 需要認證。請設定環境變數:

```bash
export API_KEY="your_api_key_here"
```

### 環境變數

| 變數名 | 說明 | 必需 |
|--------|------|------|
| `API_KEY` | API 金鑰 | 是 |
| `PORT` | 不適用 | 否 |
| `HOST` | 不適用 | 否 |



### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "indian_stock_exchange_api2": {
      "command": "python",
      "args": ["E:\path\to\indian_stock_exchange_api2\server.py"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**: 請將 `E:\path\to\indian_stock_exchange_api2\server.py` 替換為實際的伺服器檔案路徑。


## 可用工具

此服务器提供以下工具:


### `corporate_actions`

Get Corporate Actions Data

**端点**: `GET /corporate_actions`


**参数**:

- `stock_name` (string) *必需*: Example value: infosys



---


### `historical_data`

- **Endpoint**: `/historical_data` - **Method**: `GET` - **Query Parameters**:     - `stock_name` (required): string     - `period` (optional): string, default is \

**端点**: `GET /historical_data`


**参数**:

- `stock_name` (string) *必需*: Example value: tcs

- `period` (string): Example value: 

- `filter` (string): Example value: 



---


### `mutual_fund_search`

### Mutual Fund Search  **Endpoint**: `GET /mutual_fund_search`  **Description**: This endpoint allows you to search for mutual funds.  **Parameters**: - `query` (string, required): The search term to query the mutual funds.  **Response**: ```json [   {     \

**端点**: `GET /mutual_fund_search`


**参数**:

- `query` (string) *必需*: Example value: nippon



---


### `ipo`

Get latest upcoming, listed, active, closed IPO data.

**端点**: `GET /ipo`



---


### `nse_most_active`

### NSE Most Active  **Endpoint:** `/NSE_most_active`   **Method:** GET    **Description:**   Get the latest most active stocks in the National Stock Exchange (NSE) based on trading volume.  **Example Request:** ```http GET /NSE_most_active ```  **Example Response:** ```json [     {         \

**端点**: `GET /NSE_most_active`



---


### `stock_forecasts`

$237

**端点**: `GET /stock_forecasts`


**参数**:

- `stock_id` (string) *必需*: Example value: TCS

- `measure_code` (string) *必需*: Example value: 

- `period_type` (string) *必需*: Example value: 

- `data_type` (string) *必需*: Example value: 

- `age` (string) *必需*: Example value: 



---


### `historical_stats`

- **Endpoint**: `/historical_stats` - **Method**: `GET` - **Query Parameters**:     - `stock_name` (required): string     - `stats` (required): string - **Description**: Retrieve historical statistics for a specific stock. - **Example Request**:     ```http     GET /historical_stats?stock_name=TATAMOTORS\u0026stats=quarter_results     ```

**端点**: `GET /historical_stats`


**参数**:

- `stock_name` (string) *必需*: Example value: TCS

- `stats` (string): Example value: 



---


### `fetch_52_week_high_low_data`

$238

**端点**: `GET /fetch_52_week_high_low_data`



---


### `mutual_funds`

### Mutual Funds  **Endpoint:** `/mutual_funds`   **Method:** GET    **Description:**   Retrieve the latest data for mutual funds, including net asset value (NAV), returns, and other details.  **Example Request:** ```http GET /mutual_funds ```  **Example Response:** ```json {     \

**端点**: `GET /mutual_funds`



---


### `bse_most_active`

### BSE Most Active  **Endpoint:** `/BSE_most_active`   **Method:** GET    **Description:**   Get the latest most active stocks in the Bombay Stock Exchange (BSE) based on trading volume.  **Example Request:** ```http GET /BSE_most_active ```  **Example Response:** ```json [     {         \

**端点**: `GET /BSE_most_active`



---


### `commodity_futures_data_api`

$239

**端点**: `GET /commodities`



---


### `get_stock_data_by_name`

$23a

**端点**: `GET /stock`


**参数**:

- `name` (string) *必需*: Example value: tata steel



---


### `price_shockers`

### Price Shockers  **Endpoint:** `/price_shockers`   **Method:** GET    **Description:**   Get data for stocks that have experienced significant price changes in a short period of time.  **Example Request:** ```http GET /price_shockers ```  **Example Response:** ```json [     {         \

**端点**: `GET /price_shockers`



---


### `industry_search`

$23b

**端点**: `GET /industry_search`


**参数**:

- `query` (string) *必需*: Example value: tata



---


### `analyst_recommendations`

$23c

**端点**: `GET /stock_target_price`


**参数**:

- `stock_id` (string) *必需*: Example value: TCS



---


### `get_trending_stocks`

$23d

**端点**: `GET /trending`



---



## 技术栈

- **FastMCP**: 快速、Pythonic 的 MCP 服务器框架
- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

此伺服器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自動生成。

版本: 1.0.0
