"""
Indian Stock Exchange Api2 MCP Server

使用 FastMCP 的 from_openapi 方法自动生成

Version: 1.0.0
Transport: stdio
"""
import os
import json
import httpx
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "1.0.0"
__tag__ = "indian_stock_exchange_api2/1.0.0"

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# OpenAPI 规范
OPENAPI_SPEC = """{\n  \"openapi\": \"3.0.0\",\n  \"info\": {\n    \"title\": \"Indian Stock Exchange Api2\",\n    \"version\": \"1.0.0\",\n    \"description\": \"RapidAPI: linuz/indian-stock-exchange-api2\"\n  },\n  \"servers\": [\n    {\n      \"url\": \"https://indian-stock-exchange-api2.p.rapidapi.com\"\n    }\n  ],\n  \"paths\": {\n    \"/corporate_actions\": {\n      \"get\": {\n        \"summary\": \"Corporate Actions\",\n        \"description\": \"Get Corporate Actions Data\",\n        \"operationId\": \"corporate_actions\",\n        \"parameters\": [\n          {\n            \"name\": \"stock_name\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: infosys\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/historical_data\": {\n      \"get\": {\n        \"summary\": \"Historical Data\",\n        \"description\": \"- **Endpoint**: `/historical_data` - **Method**: `GET` - **Query Parameters**:     - `stock_name` (required): string     - `period` (optional): string, default is \\\\\",\n        \"operationId\": \"historical_data\",\n        \"parameters\": [\n          {\n            \"name\": \"stock_name\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: tcs\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"period\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"filter\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/mutual_fund_search\": {\n      \"get\": {\n        \"summary\": \"Mutual Fund Search\",\n        \"description\": \"### Mutual Fund Search  **Endpoint**: `GET /mutual_fund_search`  **Description**: This endpoint allows you to search for mutual funds.  **Parameters**: - `query` (string, required): The search term to query the mutual funds.  **Response**: ```json [   {     \\\\\",\n        \"operationId\": \"mutual_fund_search\",\n        \"parameters\": [\n          {\n            \"name\": \"query\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: nippon\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/ipo\": {\n      \"get\": {\n        \"summary\": \"IPO\",\n        \"description\": \"Get latest upcoming, listed, active, closed IPO data.\",\n        \"operationId\": \"ipo\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/NSE_most_active\": {\n      \"get\": {\n        \"summary\": \"NSE Most Active\",\n        \"description\": \"### NSE Most Active  **Endpoint:** `/NSE_most_active`   **Method:** GET    **Description:**   Get the latest most active stocks in the National Stock Exchange (NSE) based on trading volume.  **Example Request:** ```http GET /NSE_most_active ```  **Example Response:** ```json [     {         \\\\\",\n        \"operationId\": \"nse_most_active\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/stock_forecasts\": {\n      \"get\": {\n        \"summary\": \"Stock Forecasts\",\n        \"description\": \"$237\",\n        \"operationId\": \"stock_forecasts\",\n        \"parameters\": [\n          {\n            \"name\": \"stock_id\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: TCS\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"measure_code\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"period_type\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"data_type\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"age\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/historical_stats\": {\n      \"get\": {\n        \"summary\": \"Historical Stats\",\n        \"description\": \"- **Endpoint**: `/historical_stats` - **Method**: `GET` - **Query Parameters**:     - `stock_name` (required): string     - `stats` (required): string - **Description**: Retrieve historical statistics for a specific stock. - **Example Request**:     ```http     GET /historical_stats?stock_name=TATAMOTORS\\\\u0026stats=quarter_results     ```\",\n        \"operationId\": \"historical_stats\",\n        \"parameters\": [\n          {\n            \"name\": \"stock_name\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: TCS\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"stats\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/fetch_52_week_high_low_data\": {\n      \"get\": {\n        \"summary\": \"Fetch 52 Week High Low Data\",\n        \"description\": \"$238\",\n        \"operationId\": \"fetch_52_week_high_low_data\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/mutual_funds\": {\n      \"get\": {\n        \"summary\": \"Mutual Funds\",\n        \"description\": \"### Mutual Funds  **Endpoint:** `/mutual_funds`   **Method:** GET    **Description:**   Retrieve the latest data for mutual funds, including net asset value (NAV), returns, and other details.  **Example Request:** ```http GET /mutual_funds ```  **Example Response:** ```json {     \\\\\",\n        \"operationId\": \"mutual_funds\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/BSE_most_active\": {\n      \"get\": {\n        \"summary\": \"BSE Most Active\",\n        \"description\": \"### BSE Most Active  **Endpoint:** `/BSE_most_active`   **Method:** GET    **Description:**   Get the latest most active stocks in the Bombay Stock Exchange (BSE) based on trading volume.  **Example Request:** ```http GET /BSE_most_active ```  **Example Response:** ```json [     {         \\\\\",\n        \"operationId\": \"bse_most_active\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/commodities\": {\n      \"get\": {\n        \"summary\": \"Commodity Futures Data API\",\n        \"description\": \"$239\",\n        \"operationId\": \"commodity_futures_data_api\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/stock\": {\n      \"get\": {\n        \"summary\": \"Get Stock Data by Name\",\n        \"description\": \"$23a\",\n        \"operationId\": \"get_stock_data_by_name\",\n        \"parameters\": [\n          {\n            \"name\": \"name\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: tata steel\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/price_shockers\": {\n      \"get\": {\n        \"summary\": \"Price Shockers\",\n        \"description\": \"### Price Shockers  **Endpoint:** `/price_shockers`   **Method:** GET    **Description:**   Get data for stocks that have experienced significant price changes in a short period of time.  **Example Request:** ```http GET /price_shockers ```  **Example Response:** ```json [     {         \\\\\",\n        \"operationId\": \"price_shockers\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/industry_search\": {\n      \"get\": {\n        \"summary\": \"Industry Search\",\n        \"description\": \"$23b\",\n        \"operationId\": \"industry_search\",\n        \"parameters\": [\n          {\n            \"name\": \"query\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: tata\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/stock_target_price\": {\n      \"get\": {\n        \"summary\": \"Analyst Recommendations\",\n        \"description\": \"$23c\",\n        \"operationId\": \"analyst_recommendations\",\n        \"parameters\": [\n          {\n            \"name\": \"stock_id\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: TCS\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/trending\": {\n      \"get\": {\n        \"summary\": \"Get Trending Stocks\",\n        \"description\": \"$23d\",\n        \"operationId\": \"get_trending_stocks\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    }\n  },\n  \"components\": {\n    \"securitySchemes\": {\n      \"ApiAuth\": {\n        \"type\": \"apiKey\",\n        \"in\": \"header\",\n        \"name\": \"X-RapidAPI-Key\"\n      }\n    }\n  },\n  \"security\": [\n    {\n      \"ApiAuth\": []\n    }\n  ]\n}"""

# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "indian-stock-exchange-api2.p.rapidapi.com"
else:
    print("⚠️  警告: 未设置 API_KEY 环境变量")
    print("   RapidAPI 需要 API Key 才能正常工作")
    print("   请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://indian-stock-exchange-api2.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = json.loads(OPENAPI_SPEC)
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_dict,
    client=client,
    name="indian_stock_exchange_api2",
    version=__version__
)


# 注册请求拦截器，为所有请求添加 RapidAPI headers
_original_request = client.request

async def _add_rapidapi_headers(method, url, **kwargs):
    """拦截所有请求，添加必需的 RapidAPI headers"""
    # 确保 headers 存在
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    
    # 添加 RapidAPI 必需的 headers
    if API_KEY:
        kwargs['headers']['X-RapidAPI-Key'] = API_KEY
        kwargs['headers']['X-RapidAPI-Host'] = "indian-stock-exchange-api2.p.rapidapi.com"
    else:
        print("⚠️  警告: API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    print(f"🚀 启动 Indian Stock Exchange Api2 MCP 服务器")
    print(f"📦 版本: {__tag__}")
    print(f"🔧 传输协议: {TRANSPORT}")
    
    print()
    
    # 运行服务器
    
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()