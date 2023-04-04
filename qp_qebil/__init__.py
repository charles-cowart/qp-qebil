# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The Qiita Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from qiita_client import QiitaPlugin, QiitaCommand

from .qebil import qebil_interface


class QiitaPluginAdmin(QiitaPlugin):
    _plugin_type = "private"


__version__ = '2023.04'

plugin = QiitaPluginAdmin('qp-qebil', __version__,
                          'Knight Lab QEBIL Interface')

req_params = {
    'run_identifier': ('string', ['']),
    'sample_sheet': ('prep_template', ['']),
    'lane_number': ('integer', [None]),
    }
opt_params = dict()
outputs = {'output': 'job-output-folder'}
dflt_param_set = dict()

qebil_cmd = QiitaCommand(
    'QEBIL Interface', 'Use QEBIL to extract metadata from EBI and load into '
    'Qiita', qebil_interface, req_params, opt_params, outputs, dflt_param_set)

plugin.register_command(qebil_cmd)
