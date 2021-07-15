# 使用说明

## 一、授权说明

### 1、确认系统要求

请确认你要安装的系统是否满足要求：

- 系统：Windows 10/Windows Server 2016
- Python： 3.9
- 网络：联网

### 2、反馈主机信息

在命令行中输入下面命令
```
pip install pyarmor
```
然后输入
```
pyarmor hdinfo
```
复制打印信息发送给客服，然后耐心等待...

### 3、存放 licnse 文件

1. 收到客服的 license.lic 文件，放在本目录下
2. （可选）把本目录下的 pytransform.pyd 文件剪切到 ...\Python39\Lib\site-packages\ 目录


## 二、快速启动

### 1、安装 sweet

```
pip install sweet
```

### 2、安装官方`关键字模块`

```
pip install sweet.web
pip install sweet.http
pip install sweet.mobile
pip install sweet.db
pip install sweet.file
```
> 备注：示例的测试用例有用到，请全部安装，后续可自行卸载

### 3. 启动 Web「测试报告」服务

在项目目录（sweet_example），用命令行执行如下命令：

```
python app.py
```

打开网页：http://127.0.0.1:80 查看测试报告


### 4. 执行自动化测试示例

在项目目录下（sweet_example），用命令行执行如下命令：

```
python start.py
```