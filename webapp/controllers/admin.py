from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView


class CustomModelView(ModelView):
    pass

class CustomFileAdmin(FileAdmin):
    pass
