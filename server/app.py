from flask import Flask, jsonify
from flask_cors import CORS
from config.database import init_db
from routes.api import api
import os

def create_app():
    """创建Flask应用"""
    app = Flask(__name__)

    # 配置CORS
    CORS(app, resources={
        r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # 初始化数据库
    db = init_db(app)

    # 注册蓝图
    app.register_blueprint(api, url_prefix='/api')

    # 根路径
    @app.route('/')
    def index():
        return jsonify({
            'code': 200,
            'message': '面试内推小程序API服务',
            'version': '1.0.0'
        })

    # 健康检查
    @app.route('/health')
    def health():
        return jsonify({
            'code': 200,
            'message': '服务正常'
        })

    # 错误处理
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'code': 404,
            'message': '请求的资源不存在'
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'code': 500,
            'message': '服务器内部错误'
        }), 500

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
