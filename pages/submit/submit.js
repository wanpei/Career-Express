// pages/submit/submit.js
const app = getApp();

Page({
  data: {
    jobId: null,
    job: null,
    form: {
      name: '',
      phone: '',
      email: '',
      experience: '',
      currentCompany: '',
      expectedSalary: '',
      introduction: ''
    },
    experiences: ['应届生', '1年以下', '1-3年', '3-5年', '5-10年', '10年以上'],
    salaries: ['面议', '10k以下', '10k-20k', '20k-30k', '30k-50k', '50k以上'],
    files: []
  },

  onLoad(options) {
    const jobId = parseInt(options.jobId);
    this.setData({ jobId });
    this.loadJobInfo(jobId);
  },

  loadJobInfo(jobId) {
    const jobs = app.globalData.jobs;
    const job = jobs.find(j => j.id === jobId);
    if (job) {
      this.setData({ job });
    }
  },

  onInput(e) {
    const { field } = e.currentTarget.dataset;
    const { value } = e.detail;
    this.setData({
      [`form.${field}`]: value
    });
  },

  onExperienceChange(e) {
    const index = e.detail.value;
    this.setData({
      'form.experience': this.data.experiences[index]
    });
  },

  onSalaryChange(e) {
    const index = e.detail.value;
    this.setData({
      'form.expectedSalary': this.data.salaries[index]
    });
  },

  chooseFile() {
    wx.chooseMessageFile({
      count: 1,
      type: 'file',
      extension: ['pdf', 'doc', 'docx'],
      success: (res) => {
        const file = res.tempFiles[0];
        this.setData({
          files: [{ name: file.name, size: file.size, path: file.path }]
        });
      }
    });
  },

  removeFile() {
    this.setData({ files: [] });
  },

  validateForm() {
    const { name, phone, email } = this.data.form;
    if (!name.trim()) {
      wx.showToast({ title: '请输入姓名', icon: 'none' });
      return false;
    }
    if (!phone.trim()) {
      wx.showToast({ title: '请输入手机号', icon: 'none' });
      return false;
    }
    if (!/^1[3-9]\d{9}$/.test(phone)) {
      wx.showToast({ title: '手机号格式不正确', icon: 'none' });
      return false;
    }
    if (!email.trim()) {
      wx.showToast({ title: '请输入邮箱', icon: 'none' });
      return false;
    }
    if (!/^\w+@[a-zA-Z0-9]+\.[a-zA-Z]+$/.test(email)) {
      wx.showToast({ title: '邮箱格式不正确', icon: 'none' });
      return false;
    }
    return true;
  },

  submit() {
    if (!this.validateForm()) return;

    wx.showLoading({ title: '提交中...' });

    setTimeout(() => {
      const application = {
        id: Date.now(),
        jobId: this.data.jobId,
        job: this.data.job,
        form: this.data.form,
        file: this.data.files[0] || null,
        status: 0, // 0: 待处理, 1: 已查看, 2: 感兴趣, 3: 不合适
        submitTime: new Date().toISOString().split('T')[0]
      };

      app.globalData.applications.push(application);

      wx.hideLoading();
      wx.showModal({
        title: '投递成功',
        content: '您的简历已成功投递，请耐心等待HR回复',
        showCancel: false,
        success: () => {
          wx.navigateBack();
        }
      });
    }, 1500);
  }
});
