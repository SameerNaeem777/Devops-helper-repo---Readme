from click.testing import CliRunner
from src.devops_helper.cli import cli




def test_help():
runner = CliRunner()
result = runner.invoke(cli, ['--help'])
assert result.exit_code == 0
assert 'DevOps Helper CLI' in result.output
