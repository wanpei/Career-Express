from datetime import datetime
from config.database import db

class User(db.Model):
    """用户表"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    openid = db.Column(db.String(100), unique=True, nullable=False, comment='微信openid')
    unionid = db.Column(db.String(100), comment='微信unionid')
    nickname = db.Column(db.String(100), comment='昵称')
    avatar_url = db.Column(db.String(500), comment='头像URL')
    phone = db.Column(db.String(20), comment='手机号')
    email = db.Column(db.String(100), comment='邮箱')
    gender = db.Column(db.Integer, default=0, comment='性别：0未知 1男 2女')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')
    status = db.Column(db.Integer, default=1, comment='状态：0禁用 1正常')

    # 关系
    resumes = db.relationship('Resume', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    applications = db.relationship('Application', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    collections = db.relationship('Collection', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    notifications = db.relationship('Notification', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    view_records = db.relationship('ViewRecord', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'openid': self.openid,
            'nickname': self.nickname,
            'avatar_url': self.avatar_url,
            'phone': self.phone,
            'email': self.email,
            'gender': self.gender,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None,
            'status': self.status
        }

class Company(db.Model):
    """公司表"""
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, comment='公司名称')
    logo_url = db.Column(db.String(500), comment='公司Logo URL')
    description = db.Column(db.Text, comment='公司简介')
    industry = db.Column(db.String(50), comment='所属行业')
    scale = db.Column(db.String(50), comment='公司规模')
    location = db.Column(db.String(100), comment='公司地址')
    website = db.Column(db.String(200), comment='公司官网')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    # 关系
    jobs = db.relationship('Job', backref='company', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'logo_url': self.logo_url,
            'description': self.description,
            'industry': self.industry,
            'scale': self.scale,
            'location': self.location,
            'website': self.website,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        }

class Job(db.Model):
    """职位表"""
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), comment='公司ID')
    position = db.Column(db.String(100), nullable=False, comment='职位名称')
    salary = db.Column(db.String(50), comment='薪资范围')
    location = db.Column(db.String(50), comment='工作地点')
    experience = db.Column(db.String(50), comment='工作经验要求')
    education = db.Column(db.String(50), comment='学历要求')
    description = db.Column(db.Text, comment='职位描述')
    requirements = db.Column(db.Text, comment='职位要求')
    tags = db.Column(db.JSON, comment='福利标签')
    hr_wechat = db.Column(db.String(50), comment='HR微信号')
    hr_name = db.Column(db.String(50), comment='HR姓名')
    status = db.Column(db.Integer, default=1, comment='状态：0下架 1上架')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    # 关系
    applications = db.relationship('Application', backref='job', lazy='dynamic', cascade='all, delete-orphan')
    collections = db.relationship('Collection', backref='job', lazy='dynamic', cascade='all, delete-orphan')
    view_records = db.relationship('ViewRecord', backref='job', lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'company': self.company.name if self.company else None,
            'position': self.position,
            'salary': self.salary,
            'location': self.location,
            'experience': self.experience,
            'education': self.education,
            'description': self.description,
            'requirements': self.requirements,
            'tags': self.tags,
            'hr_wechat': self.hr_wechat,
            'hr_name': self.hr_name,
            'status': self.status,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        }

class Resume(db.Model):
    """简历表"""
    __tablename__ = 'resumes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, comment='用户ID')
    name = db.Column(db.String(50), comment='姓名')
    phone = db.Column(db.String(20), comment='手机号')
    email = db.Column(db.String(100), comment='邮箱')
    experience = db.Column(db.String(50), comment='工作年限')
    current_company = db.Column(db.String(100), comment='当前公司')
    expected_salary = db.Column(db.String(50), comment='期望薪资')
    introduction = db.Column(db.Text, comment='自我介绍')
    file_url = db.Column(db.String(500), comment='简历文件URL')
    file_name = db.Column(db.String(200), comment='简历文件名')
    file_size = db.Column(db.Integer, comment='简历文件大小（字节）')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'experience': self.experience,
            'current_company': self.current_company,
            'expected_salary': self.expected_salary,
            'introduction': self.introduction,
            'file_url': self.file_url,
            'file_name': self.file_name,
            'file_size': self.file_size,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        }

class Application(db.Model):
    """投递记录表"""
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, comment='用户ID')
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False, comment='职位ID')
    resume_id = db.Column(db.Integer, db.ForeignKey('resumes.id'), comment='简历ID')
    status = db.Column(db.Integer, default=0, comment='状态：0待处理 1已查看 2感兴趣 3不合适')
    remark = db.Column(db.Text, comment='备注信息')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'job_id': self.job_id,
            'resume_id': self.resume_id,
            'status': self.status,
            'remark': self.remark,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None,
            'job': self.job.to_dict() if self.job else None
        }

class Collection(db.Model):
    """收藏表"""
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, comment='用户ID')
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False, comment='职位ID')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')

    __table_args__ = (
        db.UniqueConstraint('user_id', 'job_id', name='uk_user_job'),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'job_id': self.job_id,
            'job': self.job.to_dict() if self.job else None,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        }

class Notification(db.Model):
    """消息通知表"""
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, comment='用户ID')
    title = db.Column(db.String(200), nullable=False, comment='通知标题')
    content = db.Column(db.Text, comment='通知内容')
    type = db.Column(db.String(20), default='system', comment='类型：system系统 application投递 interview面试')
    is_read = db.Column(db.Integer, default=0, comment='是否已读：0未读 1已读')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'content': self.content,
            'type': self.type,
            'is_read': self.is_read,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        }

class ViewRecord(db.Model):
    """浏览记录表"""
    __tablename__ = 'view_records'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), comment='用户ID（可为空，未登录用户）')
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False, comment='职位ID')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'job_id': self.job_id,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None
        }
