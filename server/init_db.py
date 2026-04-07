from flask import Flask
from config.database import init_db
from models.models import User, Company, Job, Resume, Application, Collection, Notification, ViewRecord

def create_tables():
    """创建所有数据表"""
    app = Flask(__name__)
    db = init_db(app)

    with app.app_context():
        # 创建所有表
        db.create_all()
        print("数据库表创建成功！")

        # 插入示例数据
        insert_sample_data(db)
        print("示例数据插入成功！")

def insert_sample_data(db):
    """插入示例数据"""
    # 创建示例公司
    companies = [
        Company(
            name='阿里巴巴',
            logo_url='/images/company/alibaba.png',
            description='阿里巴巴集团控股有限公司是以马云为首的18人于1999年在浙江省杭州市创立的公司。',
            industry='互联网',
            scale='10000人以上',
            location='杭州',
            website='https://www.alibaba.com'
        ),
        Company(
            name='腾讯',
            logo_url='/images/company/tencent.png',
            description='腾讯，1998年11月诞生于中国深圳，是一家以互联网为基础的科技与文化公司。',
            industry='互联网',
            scale='10000人以上',
            location='深圳',
            website='https://www.tencent.com'
        ),
        Company(
            name='字节跳动',
            logo_url='/images/company/bytedance.png',
            description='字节跳动成立于2012年3月，公司使命是"Inspire Creativity, Enrich Life"。',
            industry='互联网',
            scale='10000人以上',
            location='北京',
            website='https://www.bytedance.com'
        )
    ]

    for company in companies:
        db.session.add(company)
    db.session.commit()

    # 创建示例职位
    jobs = [
        Job(
            company_id=1,
            position='前端开发工程师',
            salary='25k-45k',
            location='杭州',
            experience='3-5年',
            education='本科',
            description='负责公司核心产品的前端开发工作',
            requirements='1. 精通HTML、CSS、JavaScript
2. 熟悉Vue/React等主流框架
3. 有良好的代码规范和团队协作能力',
            tags=['五险一金', '年终奖', '带薪年假', '餐补'],
            hr_wechat='hr_alibaba',
            hr_name='张HR'
        ),
        Job(
            company_id=1,
            position='后端开发工程师',
            salary='30k-50k',
            location='杭州',
            experience='3-5年',
            education='本科',
            description='负责公司核心业务系统的后端开发',
            requirements='1. 精通Java/Python/Go等至少一门语言
2. 熟悉MySQL、Redis等数据库
3. 有高并发系统设计经验',
            tags=['五险一金', '年终奖', '股票期权', '免费班车'],
            hr_wechat='hr_alibaba',
            hr_name='李HR'
        ),
        Job(
            company_id=2,
            position='产品经理',
            salary='25k-40k',
            location='深圳',
            experience='3-5年',
            education='本科',
            description='负责产品规划、需求分析和产品设计',
            requirements='1. 有互联网产品经验
2. 良好的沟通协调能力
3. 熟练使用Axure等原型设计工具',
            tags=['五险一金', '年终奖', '带薪年假', '健身房'],
            hr_wechat='hr_tencent',
            hr_name='王HR'
        ),
        Job(
            company_id=3,
            position='算法工程师',
            salary='35k-60k',
            location='北京',
            experience='3-5年',
            education='硕士',
            description='负责推荐算法、机器学习模型的研发和优化',
            requirements='1. 熟悉机器学习、深度学习算法
2. 精通Python/C++
3. 有大规模推荐系统经验优先',
            tags=['五险一金', '年终奖', '股票期权', '弹性工作'],
            hr_wechat='hr_bytedance',
            hr_name='赵HR'
        ),
        Job(
            company_id=3,
            position='iOS开发工程师',
            salary='25k-45k',
            location='北京',
            experience='3-5年',
            education='本科',
            description='负责抖音等产品的iOS客户端开发',
            requirements='1. 精通Objective-C/Swift
2. 熟悉iOS系统原理和性能优化
3. 有大型App开发经验',
            tags=['五险一金', '年终奖', '股票期权', '免费三餐'],
            hr_wechat='hr_bytedance',
            hr_name='孙HR'
        )
    ]

    for job in jobs:
        db.session.add(job)
    db.session.commit()

    # 创建示例用户
    users = [
        User(
            openid='test_openid_1',
            nickname='测试用户1',
            avatar_url='/images/avatar/default.png',
            phone='13800138001',
            email='test1@example.com',
            gender=1
        ),
        User(
            openid='test_openid_2',
            nickname='测试用户2',
            avatar_url='/images/avatar/default.png',
            phone='13800138002',
            email='test2@example.com',
            gender=2
        )
    ]

    for user in users:
        db.session.add(user)
    db.session.commit()

    # 创建示例通知
    notifications = [
        Notification(
            user_id=1,
            title='系统通知',
            content='欢迎使用面试内推小程序',
            type='system'
        ),
        Notification(
            user_id=1,
            title='投递状态更新',
            content='您投递的"前端开发工程师"职位已被HR查看',
            type='application'
        )
    ]

    for notification in notifications:
        db.session.add(notification)
    db.session.commit()

if __name__ == '__main__':
    create_tables()
