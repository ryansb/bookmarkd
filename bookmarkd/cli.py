"""
Author: Ryan Brown <sb@ryansb.com>
License: AGPL3
"""

import click


@click.group()
def cli():
    pass

@cli.command()
def version():
    click.echo("You are using ofcourse version {}".format(__version__))
    click.echo("Get more information at "
               "https://github.com/ryansb/ofCourse")


@cli.command(short_help="Push this to openshift. Requires "
             "http://openshift.com account. Will check for "
             "course.openshift.git_url as well as CLI flag --remote")
@click.option("-o", "--output", help="File to send output to")
@click.option("--stdout", help="Sent output to stdout instead", is_flag=True)
def md(output, stdout):
    pass
