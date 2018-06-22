from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates'),
)
template = env.get_template('index.jinja2')
f = open('docs/index.html', 'w')
f.write(template.render())
