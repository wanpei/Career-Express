# 面试内推小程序后端服务

基于 Flask + MySQL 的小程序后端服务，提供职位管理、用户管理、投递记录、收藏和消息通知等功能。

## 目录结构

```
server/
├── app.py                 # 主应用文件
├── init_db.py            # 数据库初始化脚本
├── requirements.txt      # Python依赖
├── .env.example          # 环境变量示例
├── config/
│   └── database.py       # 数据库配置
├── models/
│   └── models.py         # 数据库模型
└── routes/
    └── api.py            # API路由
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env` 并修改配置：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填写你的数据库配置：

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=interview_recommend
```

### 3. 创建数据库

在 MySQL 中创建数据库：

```sql
CREATE DATABASE interview_recommend DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. 初始化数据库

运行初始化脚本，创建数据表并插入示例数据：

```bash
python init_db.py
```

### 5. 启动服务

```bash
python app.py
```

服务将在 `http://localhost:5000` 启动。

## API 文档

### 用户相关

#### 用户登录
- **接口**: `POST /api/user/login`
- **参数**:
  ```json
  {
    "openid": "用户openid",
    "nickname": "昵称",
    "avatar_url": "头像URL",
    "gender": 1
  }
  ```
- **返回**:
  ```json
  {
    "code": 200,
    "message": "登录成功",
    "data": {
      "id": 1,
      "openid": "xxx",
      "nickname": "xxx",
      ...
    }
  }
  ```

#### 获取用户信息
- **接口**: `GET /api/user/info?openid=xxx`

### 职位相关

#### 获取职位列表
- **接口**: `GET /api/jobs?page=1&per_page=10&keyword=xxx&location=xxx&experience=xxx`

#### 获取职位详情
- **接口**: `GET /api/jobs/{job_id}?openid=xxx`

### 投递相关

#### 创建投递记录
- **接口**: `POST /api/applications`
- **参数**:
  ```json
  {
    "openid": "用户openid",
    "job_id": 1,
    "name": "姓名",
    "phone": "手机号",
    "email": "邮箱",
    "experience": "工作年限",
    "current_company": "当前公司",
    "expected_salary": "期望薪资",
    "introduction": "自我介绍",
    "file_url": "简历文件URL",
    "file_name": "简历文件名",
    "file_size": 1024
  }
  ```

#### 获取投递记录
- **接口**: `GET /api/applications?openid=xxx&status=0`

### 收藏相关

#### 添加收藏
- **接口**: `POST /api/collections`
- **参数**:
  ```json
  {
    "openid": "用户openid",
    "job_id": 1
  }
  ```

#### 取消收藏
- **接口**: `DELETE /api/collections/{collection_id}`

#### 获取收藏列表
- **接口**: `GET /api/collections?openid=xxx`

### 消息通知相关

#### 获取通知列表
- **接口**: `GET /api/notifications?openid=xxx&type=system`

#### 标记通知已读
- **接口**: `PUT /api/notifications/{notification_id}/read`

#### 获取未读消息数量
- **接口**: `GET /api/notifications/unread-count?openid=xxx`

## 数据库表结构

- `users` - 用户表
- `companies` - 公司表
- `jobs` - 职位表
- `resumes` - 简历表
- `applications` - 投递记录表
- `collections` - 收藏表
- `notifications` - 消息通知表
- `view_records` - 浏览记录表

## 注意事项

1. 确保MySQL服务正在运行
2. 确保数据库用户有足够的权限
3. 生产环境请修改 `SECRET_KEY` 和数据库密码
4. 建议使用虚拟环境运行

## 开发建议

1. 使用 Docker 部署 MySQL 数据库
2. 使用 Nginx 作为反向代理
3. 配置日志记录
4. 添加单元测试
5. 实现文件上传功能

## License

MIT
