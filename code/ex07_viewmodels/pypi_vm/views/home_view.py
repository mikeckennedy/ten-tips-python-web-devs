import flask

from pypi_vm.infrastructure.view_modifiers import response
from pypi_vm.viewmodels.home.home_index_viewmodel import HomeIndexViewModel

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    vm = HomeIndexViewModel()
    return vm.to_dict()
