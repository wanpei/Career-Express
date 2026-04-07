from flask import Blueprint, request, jsonify
from models.models import User, Job, Company, Application, Collection, Notification, ViewRecord, Resume
from config.database import db
from datetime import datetime

api = Blueprint('api', __name__)

# 用户相关接口
@api.route('/user/login', methods=['POST'])
def user_login():
    """用户登录"""
    data = request.get_json()
    openid = data.get('openid')

    if not openid:
        return jsonify({'code': 400, 'message': 'openid不能为空'}), 400

    user = User.query.filter_by(openid=openid).first()
    if not user:
        # 创建新用户
        user = User(
            openid=openid,
            nickname=data.get('nickname', ''),
            avatar_url=data.get('avatar_url', ''),
            gender=data.get('gender', 0)
        )
        db.session.add(user)
        db.session.commit()

    return jsonify({
        'code': 200,
        'message': '登录成功',
        'data': user.to_dict()
    })

@api.route('/user/info', methods=['GET'])
def get_user_info():
    """获取用户信息"""
    openid = request.args.get('openid')
    if not openid:
        return jsonify({'code': 400, 'message': 'openid不能为空'}), 400

    user = User.query.filter_by(openid=openid).first()
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404

    return jsonify({
        'code': 200,
        'message': '获取成功',
        'data': user.to_dict()
    })

# 职位相关接口
@api.route('/jobs', methods=['GET'])
def get_jobs():
    """获取职位列表"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    keyword = request.args.get('keyword', '')
    location = request.args.get('location', '')
    experience = request.args.get('experience', '')

    query = Job.query.filter_by(status=1)

    if keyword:
        query = query.filter(
            db.or_(
                Job.position.contains(keyword),
                Company.name.contains(keyword)
            )
        ).join(Company)

    if location:
        query = query.filter(Job.location == location)

    if experience:
        query = query.filter(Job.experience.contains(experience))

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    jobs = [job.to_dict() for job in pagination.items]

    return jsonify({
        'code': 200,
        'message': '获取成功',
        'data': {
            'list': jobs,
            'total': pagination.total,
            'page': page,
            'per_page': per_page
        }
    })

@api.route('/jobs/<int:job_id>', methods=['GET'])
def get_job_detail(job_id):
    """获取职位详情"""
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'code': 404, 'message': '职位不存在'}), 404

    # 记录浏览
    openid = request.args.get('openid')
    if openid:
        user = User.query.filter_by(openid=openid).first()
        if user:
            view_record = ViewRecord(user_id=user.id, job_id=job_id)
            db.session.add(view_record)
            db.session.commit()

    return jsonify({
        'code': 200,
        'message': '获取成功',
        'data': job.to_dict()
    })

# 投递相关接口
@api.route('/applications', methods=['POST'])
def create_application():
    """创建投递记录"""
    data = request.get_json()
    openid = data.get('openid')
    job_id = data.get('job_id')

    if not openid or not job_id:
        return jsonify({'code': 400, 'message': '参数不完整'}), 400

    user = User.query.filter_by(openid=openid).first()
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404

    job = Job.query.get(job_id)
    if not job:
        return jsonify({'code': 404, 'message': '职位不存在'}), 404

    # 检查是否已投递
    existing = Application.query.filter_by(user_id=user.id, job_id=job_id).first()
    if existing:
        return jsonify({'code': 400, 'message': '已投递过该职位'}), 400

    # 创建简历
    resume = Resume(
        user_id=user.id,
        name=data.get('name'),
        phone=data.get('phone'),
        email=data.get('email'),
        experience=data.get('experience'),
        current_company=data.get('current_company'),
        expected_salary=data.get('expected_salary'),
        introduction=data.get('introduction'),
        file_url=data.get('file_url'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size')
    )
    db.session.add(resume)
    db.session.flush()

    # 创建投递记录
    application = Application(
        user_id=user.id,
        job_id=job_id,
        resume_id=resume.id,
        status=0
    )
    db.session.add(application)
    db.session.commit()

    # 创建通知
    notification = Notification(
        user_id=user.id,
        title='投递成功',
        content=f'您已成功投递{job.position}职位',
        type='application'
    )
    db.session.add(notification)
    db.session.commit()

    return jsonify({
        'code': 200,
        'message': '投递成功',
        'data': application.to_dict()
    })

@api.route('/applications', methods=['GET'])
def get_applications():
    """获取投递记录列表"""
    openid = request.args.get('openid')
    status = request.args.get('status', type=int)

    if not openid:
        return jsonify({'code': 400, 'message': 'openid不能为空'}), 400

    user = User.query.filter_by(openid=openid).first()
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404

    query = Application.query.filter_by(user_id=user.id)
    if status is not None:
        query = query.filter_by(status=status)

    applications = query.order_by(Application.create_time.desc()).all()
    return jsonify({
        'code': 200,
        'message': '获取成功',
        'data': [app.to_dict() for app in applications]
    })

# 收藏相关接口
@api.route('/collections', methods=['POST'])
def create_collection():
    """添加收藏"""
    data = request.get_json()
    openid = data.get('openid')
    job_id = data.get('job_id')

    if not openid or not job_id:
        return jsonify({'code': 400, 'message': '参数不完整'}), 400

    user = User.query.filter_by(openid=openid).first()
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404

    job = Job.query.get(job_id)
    if not job:
        return jsonify({'code': 404, 'message': '职位不存在'}), 404

    # 检查是否已收藏
    existing = Collection.query.filter_by(user_id=user.id, job_id=job_id).first()
    if existing:
        return jsonify({'code': 400, 'message': '已收藏该职位'}), 400

    collection = Collection(user_id=user.id, job_id=job_id)
    db.session.add(collection)
    db.session.commit()

    return jsonify({
        'code': 200,
        'message': '收藏成功',
        'data': collection.to_dict()
    })

@api.route('/collections/<int:collection_id>', methods=['DELETE'])
def delete_collection(collection_id):
    """取消收藏"""
    collection = Collection.query.get(collection_id)
    if not collection:
        return jsonify({'code': 404, 'message': '收藏不存在'}), 404

    db.session.delete(collection)
    db.session.commit()

    return jsonify({
        'code': 200,
        'message': '取消收藏成功'
    })

@api.route('/collections', methods=['GET'])
def get_collections():
    """获取收藏列表"""
    openid = request.args.get('openid')

    if not openid:
        return jsonify({'code': 400, 'message': 'openid不能为空'}), 400

    user = User.query.filter_by(openid=openid).first()
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404

    collections = Collection.query.filter_by(user_id=user.id).order_by(Collection.create_time.desc()).all()
    return jsonify({
        'code': 200,
        'message': '获取成功',
        'data': [col.to_dict() for col in collections]
    })

# 消息通知接口
@api.route('/notifications', methods=['GET'])
def get_notifications():
    """获取通知列表"""
    openid = request.args.get('openid')
    type = request.args.get('type')

    if not openid:
        return jsonify({'code': 400, 'message': 'openid不能为空'}), 400

    user = User.query.filter_by(openid=openid).first()
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404

    query = Notification.query.filter_by(user_id=user.id)
    if type:
        query = query.filter_by(type=type)

    notifications = query.order_by(Notification.create_time.desc()).all()
    return jsonify({
        'code': 200,
        'message': '获取成功',
        'data': [noti.to_dict() for noti in notifications]
    })

@api.route('/notifications/<int:notification_id>/read', methods=['PUT'])
def mark_notification_read(notification_id):
    """标记通知为已读"""
    notification = Notification.query.get(notification_id)
    if not notification:
        return jsonify({'code': 404, 'message': '通知不存在'}), 404

    notification.is_read = 1
    db.session.commit()

    return jsonify({
        'code': 200,
        'message': '标记成功',
        'data': notification.to_dict()
    })

@api.route('/notifications/unread-count', methods=['GET'])
def get_unread_count():
    """获取未读消息数量"""
    openid = request.args.get('openid')

    if not openid:
        return jsonify({'code': 400, 'message': 'openid不能为空'}), 400

    user = User.query.filter_by(openid=openid).first()
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404

    count = Notification.query.filter_by(user_id=user.id, is_read=0).count()
    return jsonify({
        'code': 200,
        'message': '获取成功',
        'data': {'count': count}
    })
