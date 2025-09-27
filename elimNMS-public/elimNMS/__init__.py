from elimNMS.controller import controller
from elimNMS.custom import CustomApp # noqa: F401
from elimNMS.database import db
from elimNMS.environment import env
from elimNMS.forms import form_factory
from elimNMS.server import server
from elimNMS.variables import vs


def initialize():
    server.register_plugins()
    first_init = db._initialize(env)
    if env.detect_cli():
        return
    form_factory._initialize()
    controller._initialize(first_init)
    vs.set_template_context()


initialize()
