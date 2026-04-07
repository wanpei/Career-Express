// pages/job-detail/job-detail.js
const app = getApp();

Page({
  data: {
    job: null,
    hasApplied: false,
    hasLogin: false,
    isCollected: false
  },

  onLoad(options) {
    const id = parseInt(options.id);
    this.loadJobDetail(id);
    this.checkLoginStatus();
    this.checkApplicationStatus(id);
    this.checkCollectionStatus(id);
  },

  loadJobDetail(id) {
    const jobs = app.globalData.jobs;
    const job = jobs.find(j => j.id === id);
    if (job) {
      this.setData({ job });
    } else {
      wx.showToast({
        title: '职位不存在',
        icon: 'error',
        complete: () => {
          setTimeout(() => {
            wx.navigateBack();
          }, 1500);
        }
      });
    }
  },

  checkLoginStatus() {
    this.setData({
      hasLogin: app.globalData.hasLogin
    });
  },

  checkApplicationStatus(jobId) {
    const applications = app.globalData.applications;
    const hasApplied = applications.some(app => app.jobId === jobId);
    this.setData({ hasApplied });
  },

  checkCollectionStatus(jobId) {
    const collections = app.globalData.collections;
    const isCollected = collections.some(c => c.jobId === jobId);
    this.setData({ isCollected });
  },

  goToSubmit() {
    if (!this.data.hasLogin) {
      wx.showModal({
        title: '提示',
        content: '请先登录后再投递简历',
        confirmText: '去登录',
        success: (res) => {
          if (res.confirm) {
            wx.switchTab({
              url: '/pages/my/my'
            });
          }
        }
      });
      return;
    }

    if (this.data.hasApplied) {
      wx.showToast({
        title: '您已投递过该职位',
        icon: 'none'
      });
      return;
    }

    wx.navigateTo({
      url: `/pages/submit/submit?jobId=${this.data.job.id}`
    });
  },

  onShareAppMessage() {
    const job = this.data.job;
    return {
      title: `${job.position} - ${job.company}`,
      path: `/pages/job-detail/job-detail?id=${job.id}`
    };
  },

  contactHR() {
    wx.showModal({
      title: '联系HR',
      content: 'HR微信号: hr2024\n\n添加时请备注：面试内推+职位名称',
      showCancel: false,
      confirmText: '复制微信号',
      success: () => {
        wx.setClipboardData({
          data: 'hr2024',
          success: () => {
            wx.showToast({
              title: '已复制',
              icon: 'success'
            });
          }
        });
      }
    });
  },

  collectJob() {
    if (!this.data.hasLogin) {
      wx.showModal({
        title: '提示',
        content: '请先登录后再收藏职位',
        confirmText: '去登录',
        success: (res) => {
          if (res.confirm) {
            wx.switchTab({
              url: '/pages/my/my'
            });
          }
        }
      });
      return;
    }

    if (this.data.isCollected) {
      // 取消收藏
      const collections = app.globalData.collections.filter(c => c.jobId !== this.data.job.id);
      app.globalData.collections = collections;
      wx.setStorageSync('collections', collections);
      this.setData({ isCollected: false });
      wx.showToast({
        title: '已取消收藏',
        icon: 'success'
      });
    } else {
      // 添加收藏
      const collection = {
        id: Date.now(),
        jobId: this.data.job.id,
        job: this.data.job,
        collectTime: new Date().toISOString().split('T')[0]
      };
      app.globalData.collections.push(collection);
      wx.setStorageSync('collections', app.globalData.collections);
      this.setData({ isCollected: true });
      wx.showToast({
        title: '已收藏',
        icon: 'success'
      });
    }
  }
});
