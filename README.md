# Indian Stock Exchange Api2 MCP Server

[English](./README_EN.md) | 简体中文 | [繁體中文](./README_ZH-TW.md)

## 🚀 使用 EMCP 平台快速体验

**[EMCP](https://sit-emcp.kaleido.guru)** 是一个强大的 MCP 服务器管理平台，让您无需手动配置即可快速使用各种 MCP 服务器！

### 快速开始：

1. 🌐 访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 注册并登录账号
3. 🎯 进入 **MCP 广场**，浏览所有可用的 MCP 服务器
4. 🔍 搜索或找到本服务器（`bach-indian_stock_exchange_api2`）
5. 🎉 点击 **"安装 MCP"** 按钮
6. ✅ 完成！即可在您的应用中使用

### EMCP 平台优势：

- ✨ **零配置**：无需手动编辑配置文件
- 🎨 **可视化管理**：图形界面轻松管理所有 MCP 服务器
- 🔐 **安全可靠**：统一管理 API 密钥和认证信息
- 🚀 **一键安装**：MCP 广场提供丰富的服务器选择
- 📊 **使用统计**：实时查看服务调用情况

立即访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 开始您的 MCP 之旅！


---

## 简介

这是一个 MCP 服务器，用于访问 Indian Stock Exchange Api2 API。

- **PyPI 包名**: `bach-indian_stock_exchange_api2`
- **版本**: 1.0.0
- **传输协议**: stdio


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

### API 认证

此 API 需要认证。请设置环境变量:

```bash
export API_KEY="your_api_key_here"
```

### 环境变量

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `API_KEY` | API 密钥 | 是 |
| `PORT` | 不适用 | 否 |
| `HOST` | 不适用 | 否 |



### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "indian_stock_exchange_api2": {
      "command": "uvx",
      "args": ["--from", "bach-indian_stock_exchange_api2", "bach_indian_stock_exchange_api2"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**: 请将 `E:\path\to\indian_stock_exchange_api2\server.py` 替换为实际的服务器文件路径。


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

- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

此服务器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自动生成。

版本: 1.0.0
