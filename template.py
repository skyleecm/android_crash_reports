# use jinja2
import webapp2
from webapp2_extras import jinja2
# both autoescape and with are built-in
jinja2.default_config['environment_args']['extensions'] = []
# render is passed absolute filename
jinja2.default_config['template_path'] = "/"

# filter
def get_id(value):
    return value.key.id()

def _env():
    env = jinja2.get_jinja2().environment
    if "get_id" not in env.filters:
        env.filters["get_id"] = get_id
    return env

def render(filename, context):
    return _env().get_template(filename).render(context)
