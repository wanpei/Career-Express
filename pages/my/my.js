// pages/my/my.js
const app = getApp();

Page({
  data: {
    hasLogin: false,
    userInfo: null,
    stats: {
      applied: 0,
      viewed: 0,
      collected: 0,
      notifications: 0
    }
  },

  onLoad() {
    this.checkLoginStatus();
    this.loadStats();
  },

  onShow() {
    this.checkLoginStatus();
    this.loadStats();
  },

  checkLoginStatus() {
    const hasLogin = app.globalData.hasLogin;
    const userInfo = app.globalData.userInfo;
    this.setData({
      hasLogin,
      userInfo
    });
  },

  loadStats() {
    const applications = app.globalData.applications;
    const collections = app.globalData.collections;
    const notifications = app.globalData.notifications;
    const unreadCount = notifications.filter(n => !n.isRead).length;

    this.setData({
      'stats.applied': applications.length,
      'stats.viewed': 12,
      'stats.collected': collections.length,
      'stats.notifications': unreadCount
    });
  },

  login() {
    wx.getUserProfile({
      desc: '用于完善用户资料',
      success: (res) => {
        const userInfo = res.userInfo;
        app.globalData.userInfo = userInfo;
        app.globalData.hasLogin = true;
        wx.setStorageSync('userInfo', userInfo);
        this.setData({
          hasLogin: true,
          userInfo
        });
        wx.showToast({
          title: '登录成功',
          icon: 'success'
        });
      },
      fail: () => {
        wx.showToast({
          title: '登录失败',
          icon: 'error'
        });
      }
    });
  },

  logout() {
    wx.showModal({
      title: '提示',
      content: '确定要退出登录吗？',
      success: (res) => {
        if (res.confirm) {
          app.globalData.userInfo = null;
          app.globalData.hasLogin = false;
          wx.removeStorageSync('userInfo');
          this.setData({
            hasLogin: false,
            userInfo: null
          });
          wx.showToast({
            title: '已退出登录',
            icon: 'success'
          });
        }
      }
    });
  },

  goToApplications() {
    if (!this.data.hasLogin) {
      wx.showToast({
        title: '请先登录',
        icon: 'none'
      });
      return;
    }
    wx.navigateTo({
      url: '/pages/applications/applications'
    });
  },

  goToCollections() {
    if (!this.data.hasLogin) {
      wx.showToast({
        title: '请先登录',
        icon: 'none'
      });
      return;
    }
    wx.navigateTo({
      url: '/pages/collections/collections'
    });
  },

  goToNotifications() {
    if (!this.data.hasLogin) {
      wx.showToast({
        title: '请先登录',
        icon: 'none'
      });
      return;
    }
    wx.navigateTo({
      url: '/pages/notifications/notifications'
    });
  },

  goToResume() {
    if (!this.data.hasLogin) {
      wx.showToast({
        title: '请先登录',
        icon: 'none'
      });
      return;
    }
    wx.showToast({
      title: '我的简历',
      icon: 'none'
    });
  },

  goToSettings() {
    wx.showToast({
      title: '设置',
      icon: 'none'
    });
  },

  goToAbout() {
    wx.showModal({
      title: '关于我们',
      content: '面试内推小程序\n版本：v1.0.0\n\n致力于帮助求职者快速找到心仪的工作',
      showCancel: false
    });
  },

  onShareAppMessage() {
    return {
      title: '面试内推 - 快速找到好工作',
      path: '/pages/index/index'
    };
  }
});
