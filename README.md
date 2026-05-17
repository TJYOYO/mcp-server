# MCP 项目


## init evn

```bash
uv init .
```

## 安装 MCP SDK

```bash
uv add "mcp[cli]"
```

## 添加到VS code for windows

方式1： 在.vscode目录下创建mcp.json文件，并添加以下内容：

```code
{
    "servers": {
        "mcp-server": {
           "type": "stdio",
           "command": "C:\\Users\\tianjin\\.local\\bin\\uv.exe",
           "args": ["run", "python", "main.py"],
           "cwd": "D:\\AI\\mcp-server"
        }
    },
    "inputs": []
}
```

1: "mcp-server"： 是服务器的名称，可以自定义。

2: "type": "stdio"： 指定服务器的通信方式为标准输入输出。

3: "command": "C:\\Users\\tianjin\\.local\\bin\\uv.exe"： 指定要运行的命令，这里是uv.exe的路径。

4: "args": ["run", "python", "main.py"]： 指定运行命令的参数，这里是运行Python脚本main.py。

5: "cwd": "D:\\AI\\mcp-server"： 指定服务器的工作目录，这里是mcp-server的路径。

方式2：通过mcp servers插件，然后命令面板（Ctrl+Shift+P）选择 "MCP: Add Server"，然后按照提示输入服务器的名称、类型、命令、参数和工作目录。

## 添加到VS code for MAC

todo
