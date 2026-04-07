# 面试内推小程序

一个基于微信小程序的面试内推平台，帮助求职者快速找到心仪的工作机会，同时为企业提供高效的招聘渠道。

## 项目简介

本项目是一个完整的面试内推小程序解决方案，包含前端小程序和后端服务两部分。前端使用微信小程序原生开发，后端使用Flask + MySQL构建，提供职位浏览、投递简历、收藏职位、消息通知等核心功能。

## 主要功能

### 求职者端
- **职位浏览**：查看各类职位信息，支持按关键词、地点、经验等条件筛选
- **职位详情**：查看职位详细信息，包括公司介绍、薪资范围、职位要求等
- **投递简历**：在线填写个人信息并投递简历，支持附件上传
- **职位收藏**：收藏感兴趣的职位，方便后续查看
- **投递记录**：查看投递历史和投递状态
- **消息通知**：接收系统通知和投递状态更新

### 企业端（待开发）
- **职位发布**：发布和管理职位信息
- **简历管理**：查看和筛选投递的简历
- **面试安排**：安排面试并发送通知
- **数据统计**：查看招聘数据统计

## 技术栈

### 前端
- 微信小程序原生框架
- 微信小程序云开发（可选）

### 后端
- Python 3.x
- Flask 框架
- MySQL 数据库
- SQLAlchemy ORM
- Flask-CORS 跨域支持

## 项目结构

```
小程序/
├── app.js                 # 小程序入口文件，包含全局配置和生命周期函数
├── app.json              # 小程序全局配置文件，配置页面路径、窗口表现、tabBar等
├── app.wxss              # 全局样式文件，定义全局CSS样式
├── sitemap.json          # 站点地图配置，控制小程序页面是否允许被微信索引
├── project.config.json   # 项目配置文件，包含编译设置、AppID等
├── project.private.config.json # 项目私有配置，包含个人开发设置
├── pages/                # 页面目录，包含所有小程序页面
│   ├── index/           # 首页
│   │   ├── index.js    # 首页逻辑文件
│   │   ├── index.json  # 首页配置文件
│   │   ├── index.wxml  # 首页结构文件
│   │   └── index.wxss  # 首页样式文件
│   ├── jobs/            # 职位列表页
│   │   ├── jobs.js     # 职位列表逻辑
│   │   ├── jobs.json   # 职位列表配置
│   │   ├── jobs.wxml   # 职位列表结构
│   │   └── jobs.wxss   # 职位列表样式
│   ├── job-detail/      # 职位详情页
│   │   ├── job-detail.js    # 职位详情逻辑
│   │   ├── job-detail.json  # 职位详情配置
│   │   ├── job-detail.wxml  # 职位详情结构
│   │   └── job-detail.wxss  # 职位详情样式
│   ├── submit/          # 投递简历页
│   │   ├── submit.js   # 投递简历逻辑
│   │   ├── submit.json # 投递简历配置
│   │   ├── submit.wxml # 投递简历结构
│   │   └── submit.wxss # 投递简历样式
│   ├── applications/    # 投递记录页
│   │   ├── applications.js    # 投递记录逻辑
│   │   ├── applications.json  # 投递记录配置
│   │   ├── applications.wxml  # 投递记录结构
│   │   └── applications.wxss  # 投递记录样式
│   ├── collections/     # 收藏列表页
│   │   ├── collections.js     # 收藏列表逻辑
│   │   ├── collections.json   # 收藏列表配置
│   │   ├── collections.wxml   # 收藏列表结构
│   │   └── collections.wxss   # 收藏列表样式
│   ├── notifications/   # 消息通知页
│   │   ├── notifications.js   # 消息通知逻辑
│   │   ├── notifications.json # 消息通知配置
│   │   ├── notifications.wxml # 消息通知结构
│   │   └── notifications.wxss # 消息通知样式
│   └── my/              # 个人中心页
│       ├── my.js       # 个人中心逻辑
│       ├── my.json     # 个人中心配置
│       ├── my.wxml     # 个人中心结构
│       └── my.wxss     # 个人中心样式
├── images/              # 图片资源目录
│   ├── README.md       # 图片资源说明文档
│   ├── home-active.png # 首页选中图标
│   ├── home.png        # 首页未选中图标
│   ├── job-active.png  # 职位页选中图标
│   ├── job.png         # 职位页未选中图标
│   ├── my-active.png   # 我的页选中图标
│   └── my.png          # 我的页未选中图标
├── utils/               # 工具类目录
│   └── api.js          # API接口封装，包含所有后端接口调用
└── server/              # 后端服务目录
    ├── app.py          # 后端主程序，Flask应用入口
    ├── init_db.py      # 数据库初始化脚本，创建表并插入示例数据
    ├── requirements.txt # Python依赖包列表
    ├── README.md       # 后端服务说明文档
    ├── .env.example    # 环境变量示例文件
    ├── config/         # 配置文件目录
    │   └── database.py # 数据库配置模块
    ├── models/         # 数据模型目录
    │   └── models.py   # SQLAlchemy数据模型定义
    └── routes/         # 路由目录
        └── api.py      # API路由定义，包含所有接口实现
```

## 快速开始

### 前端开发

1. 安装微信开发者工具
2. 导入本项目
3. 配置AppID
4. 点击编译运行

### 后端开发

1. 安装Python依赖
```bash
cd server
pip install -r requirements.txt
```

2. 配置数据库
```bash
cp .env.example .env
# 编辑.env文件，配置数据库连接信息
```

3. 初始化数据库
```bash
python init_db.py
```

4. 启动服务
```bash
python app.py
```

## 数据库设计

项目使用MySQL数据库，包含以下主要数据表：

- `users` - 用户表
- `companies` - 公司表
- `jobs` - 职位表
- `resumes` - 简历表
- `applications` - 投递记录表
- `collections` - 收藏表
- `notifications` - 消息通知表
- `view_records` - 浏览记录表

详细的数据库表结构请参考 `server/models/models.py`。

## API文档

后端提供RESTful API接口，主要接口包括：

- 用户登录和信息获取
- 职位列表和详情
- 投递记录的创建和查询
- 收藏的增删查
- 消息通知的查询和标记已读

详细的API文档请参考 `server/README.md`。

## 开发计划

- [x] 基础框架搭建
- [x] 职位浏览和详情
- [x] 投递简历功能
- [x] 收藏功能
- [x] 消息通知
- [ ] 企业端开发
- [ ] 实时聊天功能
- [ ] 简历解析
- [ ] 智能推荐
- [ ] 数据统计

## 贡献指南

欢迎提交Issue和Pull Request来帮助改进项目。

## 许可证

MIT License
