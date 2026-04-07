// pages/collections/collections.js
const app = getApp();

Page({
  data: {
    collections: [],
    hasLogin: false
  },

  onLoad() {
    this.checkLoginStatus();
    this.loadCollections();
  },

  onShow() {
    this.loadCollections();
  },

  checkLoginStatus() {
    this.setData({
      hasLogin: app.globalData.hasLogin
    });
  },

  loadCollections() {
    if (!this.data.hasLogin) return;
    const collections = app.globalData.collections;
    this.setData({ collections });
  },

  goToJobDetail(e) {
    const jobId = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/job-detail/job-detail?id=${jobId}`
    });
  },

  removeCollection(e) {
    const id = e.currentTarget.dataset.id;
    wx.showModal({
      title: '提示',
      content: '确定要取消收藏吗？',
      success: (res) => {
        if (res.confirm) {
          const collections = app.globalData.collections.filter(c => c.id !== id);
          app.globalData.collections = collections;
          wx.setStorageSync('collections', collections);
          this.setData({ collections });
          wx.showToast({
            title: '已取消收藏',
            icon: 'success'
          });
        }
      }
    });
  },

  onShareAppMessage() {
    return {
      title: '我的收藏 - 面试内推',
      path: '/pages/collections/collections'
    };
  }
});
