import os

__author__ = 'joeny'


def create_backup_file(*types):
    """
    Create a backup file base off the path given. (Decorator)

    :param types:
    :return:
    """
    def _check_module(f):

        def _check_params(*args, **kwargs):
            import shutil
            import os

            file_names = []
            backup_names = []

            var_name = f.func_code.co_varnames

            i = 0
            for i in range(0, len(var_name)):
                if var_name[i] == types[0]:
                    file_names .append(args[i])

            for name in file_names :
                root_folder, filename = os.path.split(name)

                backup_names.append(os.path.join(root_folder, "_$%s" % filename))

                shutil.copy2(name, backup_names[-1])

            ret = f(*args, **kwargs)

            # Remove name
            for name in backup_names:
                os.remove(name)

            return ret

        return _check_params

    return _check_module
