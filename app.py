from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Zertifizierungen.db'
db = SQLAlchemy(app)

class Zertifizierungen(db.Model):
    """creating the Database Class"""
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    """recives post request to add new data"""
    if request.method == 'POST':
        zertifikate_content = request.form['content']
        new_zertifikate = Zertifizierungen(content=zertifikate_content)
        try:
            db.session.add(new_zertifikate)
            db.session.commit()
            return redirect('/')
        except:
            return 'Es gab ein Problem beim Hinzufügen Ihrer Zertifikat'
    else:
        zkn = Zertifizierungen.query.order_by(Zertifizierungen.date_created).all()
        return render_template('index.html', zkn=zkn)


@app.route('/delete/<int:id>')
def delete(id):
    """ recived request for entry delete """
    zertifikate_to_delete = Zertifizierungen.query.get_or_404(id)
    try:
        db.session.delete(zertifikate_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Beim Löschen dieser Zertifizierung gab es ein Problem'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    """ recived request for updating an entry """
    zertifikate = Zertifizierungen.query.get_or_404(id)
    if request.method == 'POST':
        zertifikate.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Es gab ein Problem bei der Aktualisierung deine Zertifizierung'
    else:
        return render_template('update.html', zertifikate=zertifikate)
        
if __name__ == "__main__":
    app.run(debug=True)