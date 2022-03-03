"""
client.py: implementation of the VnodeClient class for issuing commands
over a control channel to the vnoded process running in a network namespace.
The control channel can be accessed via calls using the vcmd shell.
"""
from pathlib import Path

from core import utils
from core.executables import BASH, VCMD


class VnodeClient:
    """
    Provides client functionality for interacting with a virtual node.
    """

    def __init__(self, name: str, ctrlchnlname: Path) -> None:
        """
        Create a VnodeClient instance.

        :param name: name for client
        :param ctrlchnlname: control channel name
        """
        self.name: str = name
        self.ctrlchnlname: Path = ctrlchnlname

    def _verify_connection(self) -> None:
        """
        Checks that the vcmd client is properly connected.

        :return: nothing
        :raises IOError: when not connected
        """
        if not self.connected():
            raise IOError("vcmd not connected")

    def connected(self) -> bool:
        """
        Check if node is connected or not.

        :return: True if connected, False otherwise
        """
        return True

    def close(self) -> None:
        """
        Close the client connection.

        :return: nothing
        """
        pass

    def create_cmd(self, args: str, shell: bool = False) -> str:
        if shell:
            args = f'{BASH} -c "{args}"'
        return f"{VCMD} -c {self.ctrlchnlname} -- {args}"

    def check_cmd(self, args: str, wait: bool = True, shell: bool = False) -> str:
        """
        Run command and return exit status and combined stdout and stderr.

        :param args: command to run
        :param wait: True to wait for command status, False otherwise
        :param shell: True to use shell, False otherwise
        :return: combined stdout and stderr
        :raises core.CoreCommandError: when there is a non-zero exit status
        """
        self._verify_connection()
        args = self.create_cmd(args, shell)
        return utils.cmd(args, wait=wait, shell=shell)
