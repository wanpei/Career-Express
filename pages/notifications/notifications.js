// pages/notifications/notifications.js
const app = getApp();

Page({
  data: {
    notifications: [],
    hasLogin: false,
    activeTab: 0,
    tabs: ['全部', '系统通知', '投递通知', '面试通知']
  },

  onLoad() {
    this.checkLoginStatus();
    this.loadNotifications();
  },

  onShow() {
    this.loadNotifications();
  },

  checkLoginStatus() {
    this.setData({
      hasLogin: app.globalData.hasLogin
    });
  },

  loadNotifications() {
    if (!this.data.hasLogin) return;
    const notifications = app.globalData.notifications;
    this.setData({ notifications });
  },

  onTabChange(e) {
    const index = e.detail.index;
    this.setData({ activeTab: index });
    this.filterNotifications(index);
  },

  filterNotifications(type) {
    const notifications = app.globalData.notifications;
    let filtered = notifications;

    if (type > 0) {
      const typeMap = ['', 'system', 'application', 'interview'];
      filtered = notifications.filter(n => n.type === typeMap[type]);
    }

    this.setData({ notifications: filtered });
  },

  markAsRead(e) {
    const id = e.currentTarget.dataset.id;
    const notifications = this.data.notifications.map(n => {
      if (n.id === id) {
        n.isRead = true;
      }
      return n;
    });
    app.globalData.notifications = notifications;
    this.setData({ notifications });
  },

  onPullDownRefresh() {
    setTimeout(() => {
      this.loadNotifications();
      wx.stopPullDownRefresh();
    }, 500);
  },

  onShareAppMessage() {
    return {
      title: '消息通知 - 面试内推',
      path: '/pages/notifications/notifications'
    };
  }
});
