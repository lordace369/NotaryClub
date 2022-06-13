
from flask import Flask, redirect,render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///note.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Notes(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"


@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        note1=Notes(title=title,desc=desc)
        db.session.add(note1)
        db.session.commit()

    allNotes=Notes.query.all()
    return render_template('index.html',allNotes=allNotes)


@app.route('/delete/<int:sno>')    
def delete (sno):
    note=Notes.query.filter_by(sno=sno).first()
    db.session.delete(note)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update (sno):
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        note=Notes.query.filter_by(sno=sno).first()
        note.title=title
        note.desc=desc
        db.session.add(note)
        db.session.commit()
        return redirect('/')

    note=Notes.query.filter_by(sno=sno).first()
    return render_template('update.html',note=note)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=='__main__':
    app.run(debug=True)