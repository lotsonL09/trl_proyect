from flask import Blueprint,render_template

bp_software_hardware=Blueprint('software_hardware',__name__,url_prefix='/agricultura_silvicultura')

@bp_software_hardware.route('/')
def root():
    return render_template('fields/software_hardware.html')