# mcp-url2markdown
基于 [crawl4ai](https://github.com/unclecode/crawl4ai) 根据提供的url把网页内容转为干净，格式化的markdown内容

## 快速开始

使用uv安装

```bash
git clone https://github.com/sungithubid/mcp-url2markdown.git

uv sync
```


## 使用
Cursor，cline，roo code等工具配置

```json
{
  "mcpServers": {
    "url2md": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-url2markdown",
        "run",
        "server.py"
      ],
      "env": {},
      "disabled": false,
      "autoApprove": [],
      "alwaysAllow": []
    }
  }
}
```

