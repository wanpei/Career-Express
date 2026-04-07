// pages/applications/applications.js
const app = getApp();

Page({
  data: {
    applications: [],
    hasLogin: false,
    activeTab: 0,
    tabs: ['全部', '待处理', '已查看', '感兴趣', '不合适']
  },

  onLoad() {
    this.checkLoginStatus();
    this.loadApplications();
  },

  onShow() {
    this.loadApplications();
  },

  checkLoginStatus() {
    this.setData({
      hasLogin: app.globalData.hasLogin
    });
  },

  loadApplications() {
    if (!this.data.hasLogin) return;
    const applications = app.globalData.applications;
    this.setData({ applications });
  },

  onTabChange(e) {
    const index = e.detail.index;
    this.setData({ activeTab: index });
    this.filterApplications(index);
  },

  filterApplications(status) {
    const applications = app.globalData.applications;
    let filtered = applications;

    if (status > 0) {
      filtered = applications.filter(app => app.status === status - 1);
    }

    this.setData({ applications: filtered });
  },

  goToJobDetail(e) {
    const jobId = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/job-detail/job-detail?id=${jobId}`
    });
  },

  getStatusText(status) {
    const statusMap = ['待处理', '已查看', '感兴趣', '不合适'];
    return statusMap[status] || '待处理';
  },

  getStatusClass(status) {
    const classMap = ['pending', 'viewed', 'interested', 'rejected'];
    return classMap[status] || 'pending';
  },

  onPullDownRefresh() {
    setTimeout(() => {
      this.loadApplications();
      wx.stopPullDownRefresh();
    }, 500);
  },

  onShareAppMessage() {
    return {
      title: '我的投递 - 面试内推',
      path: '/pages/applications/applications'
    };
  }
});
