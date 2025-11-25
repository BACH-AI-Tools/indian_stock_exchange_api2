# Indian Stock Exchange Api2 MCP Server

English | [简体中文](./README.md) | [繁體中文](./README_ZH-TW.md)

## 🚀 Quick Start with EMCP Platform

**[EMCP](https://sit-emcp.kaleido.guru)** is a powerful MCP server management platform that allows you to quickly use various MCP servers without manual configuration!

### Quick Start:

1. 🌐 Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)**
2. 📝 Register and login
3. 🎯 Go to **MCP Marketplace** to browse all available MCP servers
4. 🔍 Search or find this server (`bach-indian_stock_exchange_api2`)
5. 🎉 Click the **"Install MCP"** button
6. ✅ Done! You can now use it in your applications

### EMCP Platform Advantages:

- ✨ **Zero Configuration**: No need to manually edit config files
- 🎨 **Visual Management**: Easy-to-use GUI for managing all MCP servers
- 🔐 **Secure & Reliable**: Centralized API key and authentication management
- 🚀 **One-Click Install**: Rich selection of servers in MCP Marketplace
- 📊 **Usage Statistics**: Real-time service call monitoring

Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)** now to start your MCP journey!


---

## Introduction

This is an automatically generated MCP server using [FastMCP](https://fastmcp.wiki) for accessing the Indian Stock Exchange Api2 API.

- **PyPI Package**: `bach-indian_stock_exchange_api2`
- **Version**: 1.0.0
- **Transport Protocol**: stdio


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

## Configuration

### API Authentication

This API requires authentication. Please set environment variable:

```bash
export API_KEY="your_api_key_here"
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | API Key | Yes |
| `PORT` | N/A | No |
| `HOST` | N/A | No |



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

**Note**: Replace `E:\path\to\indian_stock_exchange_api2\server.py` with the actual server file path.


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

This server is automatically generated by [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) tool.

Version: 1.0.0
