from flask import Blueprint,render_template,request,g,redirect,url_for
from models import QuestionModel,AnswerModel
from .forms import QuestionForm,AnswerForm
from exts import db
from decorators import login_required
#设置首页
bp = Blueprint('ask_question',__name__,url_prefix='/')

#访问的是根路径http://127.0.0.1:5000
@bp.route('/')
def index():
    # return render_template('index.html')
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template('index.html',questions=questions)

@bp.route('/qa/public',methods=['GET','POST'])
@login_required
def public_question():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title,content=content,author=g.user)
            db.session.add(question)
            db.session.commit()
            # todo:跳转到这篇问答的详情页面
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for('ask_question.public_question'))


@bp.route('/qa/detail/<qa_id>')
def qa_detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    return render_template("detail.html",question=question)

# @bp.route('/answer/public',methods=["POST"])
@bp.post('/answer/public')   #两种写法
@login_required
def public_answer():
    form = AnswerForm(request.form)    #验证表单是否正确
    if form.validate():      #验证成功做...
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content,question_id=question_id,author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("ask_question.qa_detail",qa_id=question_id))
    else:       #验证失败做....
        print(form.errors)
        return redirect(url_for("ask_question.qa_detail",qa_id=request.form.get("question_id")))


@bp.route("/search")
def search():
    # /search?q=flask   查询字符串的形式搜flask
    # /search/<q>  将关键字固定到参数中
    # post, request.form    请求
    q = request.args.get("q")
    questions = QuestionModel.query.filter(QuestionModel.title.contains(q)).all()
    return render_template("index.html", questions=questions)