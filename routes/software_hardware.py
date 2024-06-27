from flask import Blueprint,render_template

bp_software_hardware=Blueprint('software_hardware',__name__,url_prefix='/software_hardware')

@bp_software_hardware.route('/')
def root():
    return render_template('fields/software_hardware.1.html')