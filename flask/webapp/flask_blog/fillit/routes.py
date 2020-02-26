from flask import Blueprint
from flask import render_template, jsonify, flash, request, redirect, url_for
from flask_blog.fillit import do_tetrino
from flask_blog.fillit.fillit_form import FillitForm

fillit = Blueprint('fillit', __name__)

def render_tetrino(form, nb):
    if nb < 1:
        nb = 1
    t = do_tetrino.Tetrino()
    t.build_random(nb)
    t.do_play()
    perf = "perf for {} tetriminos: {:.3f}sec (grid {} x {} - coverage {:.2f}%)".format(nb, 
                                                                        t.delta,
                                                                        t.sqa,t.sqa,t.stat)
    flash(perf, 'success')
    #return jsonify({'error' : 'Missing data!'})
    nb_col = max(int(nb / 2), 10)
    return render_template('fillit/fillit.html',
                            title='New Grid',
                            result = t.result,
                            data = t.show_in_line(nb_col),
                            label = "", blank = False,
                            form=form)

@fillit.route("/fillit", methods=['GET','POST'])
def fillit_route():
    form = FillitForm()
    if form.validate_on_submit():
        nb = int(form.nb_element.data)
        print("on post and valid" * 10)
        return render_tetrino(form, nb)
    elif request.method == 'GET':
        form.nb_element.data = 4
        print("GETgetgetget" * 11)
        return render_template('fillit/fillit.html',
                                title='New Grid',
                                result = None,
                                data = None,
                                label = "", blank = True,
                                form=form)
    print("no error" * 10)
    return redirect(url_for('fillit.fillit_route'))

@fillit.route('/process_grid', methods=['POST'])
def process_grid():
    print("PROCESS*10: {}".format(request.args.get('name',"foo")))

    return jsonify({'error' : 'Missing data!'})