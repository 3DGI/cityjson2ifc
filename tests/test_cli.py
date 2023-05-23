import pytest
from click.testing import CliRunner
from cityjson2ifc import cli


def fail_with_msg(result, runner):
    msg = (f"\n- output: {result.output}\n"
           f"- exec_info: {result.exc_info}\n"
           f"- stdout: {result.stdout}\n")
    if not runner.mix_stderr:
        msg += f"- stderr: {result.stderr}"
    pytest.fail(msg)


def test_help():
    runner = CliRunner()
    result = runner.invoke(cli.main_cmd,
                           args=["--help"])
    assert result.exit_code == 0
