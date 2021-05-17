import pyblish.api


class CollectCurrentFile(pyblish.api.ContextPlugin):
    """Inject the current working file into context"""

    order = pyblish.api.CollectorOrder
    label = "Current File"
    hosts = ['clarisse']

    def process(self, context):
        import os
        import ix

        """Inject the current working file"""
        current_file = ix.application.get_current_project_filename()

        # Maya returns forward-slashes by default
        normalised = os.path.normpath(current_file)

        context.set_data('currentFile', value=normalised)
        self.log.info("current dir:{}".format(normalised))


