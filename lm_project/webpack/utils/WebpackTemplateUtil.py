_template_content = False


def set_latest_template(template_content):
    global _template_content
    _template_content = template_content


def get_latest_template():
    global _template_content
    return _template_content


def clear_template():
    global _template_content
    _template_content = None