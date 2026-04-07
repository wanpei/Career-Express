// app.js
App({
  globalData: {
    userInfo: null,
    hasLogin: false,
    collections: [],
    notifications: [
      {
        id: 1,
        title: '系统通知',
        content: '欢迎使用面试内推小程序',
        time: '2023-11-15 10:00',
        isRead: false,
        type: 'system'
      }
    ],
    jobs: [
      {
        id: 1,
        company: '字节跳动',
        position: '前端开发工程师',
        salary: '20k-40k',
        location: '北京',
        experience: '3-5年',
        education: '本科',
        description: '负责公司核心产品的前端开发工作，参与产品需求讨论和技术方案设计。',
        requirements: ['精通HTML/CSS/JavaScript', '熟悉React或Vue框架', '有大型项目开发经验', '良好的沟通能力和团队协作精神'],
        tags: ['五险一金', '年终奖', '弹性工作', '免费三餐'],
        createTime: '2023-11-15',
        status: 1
      },
      {
        id: 2,
        company: '阿里巴巴',
        position: 'Java后端开发工程师',
        salary: '25k-45k',
        location: '杭州',
        experience: '3-5年',
        education: '本科',
        description: '参与核心系统设计与开发，负责高并发、高可用系统的架构设计和优化。',
        requirements: ['精通Java语言', '熟悉Spring Boot/Cloud框架', '熟悉分布式系统设计', '有高并发系统开发经验'],
        tags: ['股票期权', '年终奖', '带薪年假', '住房补贴'],
        createTime: '2023-11-14',
        status: 1
      },
      {
        id: 3,
        company: '腾讯',
        position: '产品经理',
        salary: '18k-35k',
        location: '深圳',
        experience: '2-4年',
        education: '本科',
        description: '负责产品需求分析、功能设计和产品规划，推动产品迭代和优化。',
        requirements: ['有互联网产品经验', '熟悉产品设计流程', '良好的数据分析能力', '优秀的沟通表达能力'],
        tags: ['六险一金', '年终奖', '弹性工作', '年度体检'],
        createTime: '2023-11-13',
        status: 1
      },
      {
        id: 4,
        company: '美团',
        position: '数据分析师',
        salary: '15k-30k',
        location: '北京',
        experience: '1-3年',
        education: '本科',
        description: '负责业务数据分析，提供数据支持和决策建议，参与数据产品建设。',
        requirements: ['熟悉SQL和Python', '良好的数据敏感度', '有数据分析经验', '优秀的沟通表达能力'],
        tags: ['五险一金', '年终奖', '弹性工作', '餐补'],
        createTime: '2023-11-12',
        status: 1
      },
      {
        id: 5,
        company: '京东',
        position: 'UI设计师',
        salary: '12k-25k',
        location: '北京',
        experience: '1-3年',
        education: '本科',
        description: '负责产品界面设计，参与设计规范制定，提升产品用户体验。',
        requirements: ['熟练使用设计工具', '有良好的审美能力', '熟悉移动端设计规范', '有电商产品经验优先'],
        tags: ['五险一金', '年终奖', '弹性工作', '节日福利'],
        createTime: '2023-11-11',
        status: 1
      }
    ],
    applications: []
  },

  onLaunch() {
    // 检查登录状态
    const userInfo = wx.getStorageSync('userInfo');
    if (userInfo) {
      this.globalData.userInfo = userInfo;
      this.globalData.hasLogin = true;
    }

    // 加载收藏数据
    const collections = wx.getStorageSync('collections');
    if (collections) {
      this.globalData.collections = collections;
    }

    // 加载消息数据
    const notifications = wx.getStorageSync('notifications');
    if (notifications) {
      this.globalData.notifications = notifications;
    }
  }
})