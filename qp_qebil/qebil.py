# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The Qiita Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from os import environ


CONFIG_FP = environ["QP_QEBIL_CONFIG_FP"]


class StatusUpdate():
    def __init__(self, qclient, job_id):
        self.qclient = qclient
        self.job_id = job_id
        self.msg = ''

    def update_job_step(self, status, id):
        # internal function implements a callback function for user.
        # :param id: PBS/Torque/or some other informative and current job id.
        # :param status: status message
        self.qclient.update_job_step(self.job_id,
                                     self.msg + f" ({id}: {status})")

    def update_current_message(self, msg):
        # internal function that sets current_message to the new value before
        # updating the job step in the UI.
        self.msg = msg
        self.qclient.update_job_step(self.job_id, msg)


def qebil_interface(qclient, job_id, parameters, out_dir):
    """Sequence Processing Pipeline command

    Parameters
    ----------
    qclient : tgp.qiita_client.QiitaClient
        The Qiita server client
    job_id : str
        The job id
    parameters : dict
        The parameter values for this job
    out_dir : str
        The path to the job's output directory

    Returns
    -------
    bool, list, str
        The results of the job
    """

    # these variables will become useful again later.
    # run_identifier = parameters.pop('run_identifier')
    user_input_file = parameters.pop('sample_sheet')
    # lane_number = parameters.pop('lane_number')
    # job_pool_size = 30

    status_line = StatusUpdate(qclient, job_id)

    status_line.update_current_message("Step 1: Setting up QEBIL")

    if {'body', 'content_type', 'filename'} != set(user_input_file):
        return False, None, ("This doesn't appear to be a valid sample sheet "
                             "or mapping file; please review.")

    status_line.update_current_message("QEBIL Finished, processing results")

    ainfo = None

    # return success, ainfo, and the last status message.
    return True, ainfo, status_line.msg
