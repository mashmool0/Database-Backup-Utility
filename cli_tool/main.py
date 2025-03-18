import click


@click.group()
def cli():
    pass


@click.command()
def hello():
    click.echo("hi welcome to this tutorial!")


@click.command()
def by():
    click.echo("khodah negah daretooon farda miam pishetoon !")


cli.add_command(hello)
cli.add_command(by)

if __name__ == '__main__':
    cli()
