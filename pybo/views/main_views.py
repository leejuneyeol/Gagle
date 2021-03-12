from flask import Blueprint, url_for, current_app
from werkzeug.utils import redirect
from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')


# @bp.route('/iu')
# def hello_pybo():
#     설명 = '''
#     아이유 - IU\n
#     본명: 이지은\n
#     나이: 29세 \n생년월일: 1993년 5월 16일\n
#     데뷔: 2008년 9월 18일
#     '''
#     return 설명

@bp.route('/iu')
def iu_pybo():
    return render_template('iu/iu_list.html')

@bp.route('/mypage')
def profile():
    return render_template('profile/mypage.html')

@bp.route('/')
def index():
    current_app.logger.info("INFO 레벨로 출력")
    return redirect(url_for('question._list'))