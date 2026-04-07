// pages/index/index.js
const app = getApp();

Page({
  data: {
    banners: [
      { id: 1, image: 'https://picsum.photos/750/300?random=1', title: '大厂内推通道开启' },
      { id: 2, image: 'https://picsum.photos/750/300?random=2', title: '高薪职位等你来' },
      { id: 3, image: 'https://picsum.photos/750/300?random=3', title: '快速入职通道' }
    ],
    hotJobs: [],
    companies: [
      { id: 1, name: '字节跳动', logo: 'https://picsum.photos/100/100?random=10', count: 128 },
      { id: 2, name: '阿里巴巴', logo: 'https://picsum.photos/100/100?random=11', count: 256 },
      { id: 3, name: '腾讯', logo: 'https://picsum.photos/100/100?random=12', count: 189 },
      { id: 4, name: '美团', logo: 'https://picsum.photos/100/100?random=13', count: 98 }
    ]
  },

  onLoad() {
    this.loadHotJobs();
  },

  onShow() {
    this.loadHotJobs();
  },

  loadHotJobs() {
    const jobs = app.globalData.jobs.slice(0, 3);
    this.setData({ hotJobs: jobs });
  },

  onBannerTap(e) {
    const id = e.currentTarget.dataset.id;
    wx.showToast({
      title: `点击了轮播图${id}`,
      icon: 'none'
    });
  },

  goToJobs() {
    wx.switchTab({
      url: '/pages/jobs/jobs'
    });
  },

  goToJobDetail(e) {
    const id = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/job-detail/job-detail?id=${id}`
    });
  },

  onCompanyTap(e) {
    const name = e.currentTarget.dataset.name;
    wx.showToast({
      title: `${name}的职位`,
      icon: 'none'
    });
  },

  onPullDownRefresh() {
    setTimeout(() => {
      this.loadHotJobs();
      wx.stopPullDownRefresh();
    }, 500);
  }
});
