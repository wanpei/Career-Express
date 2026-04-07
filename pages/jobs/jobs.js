// pages/jobs/jobs.js
const app = getApp();

Page({
  data: {
    jobs: [],
    filteredJobs: [],
    searchKeyword: '',
    filterLocation: '',
    filterExperience: '',
    locations: ['全部', '北京', '上海', '深圳', '杭州', '广州'],
    experiences: ['全部', '应届生', '1-3年', '3-5年', '5年以上'],
    activeFilter: '',
    loading: false
  },

  onLoad() {
    this.loadJobs();
  },

  onShow() {
    this.loadJobs();
  },

  loadJobs() {
    const jobs = app.globalData.jobs;
    this.setData({
      jobs: jobs,
      filteredJobs: jobs
    });
  },

  onSearchInput(e) {
    const keyword = e.detail.value;
    this.setData({ searchKeyword: keyword });
    this.filterJobs();
  },

  onLocationTap(e) {
    const location = e.currentTarget.dataset.value;
    this.setData({
      filterLocation: location === '全部' ? '' : location,
      activeFilter: ''
    });
    this.filterJobs();
  },

  onExperienceTap(e) {
    const experience = e.currentTarget.dataset.value;
    this.setData({
      filterExperience: experience === '全部' ? '' : experience,
      activeFilter: ''
    });
    this.filterJobs();
  },

  toggleFilter(e) {
    const type = e.currentTarget.dataset.type;
    this.setData({
      activeFilter: this.data.activeFilter === type ? '' : type
    });
  },

  filterJobs() {
    const { jobs, searchKeyword, filterLocation, filterExperience } = this.data;
    let filtered = jobs;

    if (searchKeyword) {
      const keyword = searchKeyword.toLowerCase();
      filtered = filtered.filter(job => 
        job.position.toLowerCase().includes(keyword) ||
        job.company.toLowerCase().includes(keyword)
      );
    }

    if (filterLocation) {
      filtered = filtered.filter(job => job.location === filterLocation);
    }

    if (filterExperience) {
      filtered = filtered.filter(job => job.experience.includes(filterExperience.replace('年', '')));
    }

    this.setData({ filteredJobs: filtered });
  },

  goToJobDetail(e) {
    const id = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/job-detail/job-detail?id=${id}`
    });
  },

  onPullDownRefresh() {
    setTimeout(() => {
      this.loadJobs();
      wx.stopPullDownRefresh();
    }, 500);
  },

  onReachBottom() {
    wx.showToast({
      title: '没有更多职位了',
      icon: 'none'
    });
  }
});
