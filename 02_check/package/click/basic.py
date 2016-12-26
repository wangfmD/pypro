import click

@click.command()
@click.option('--n', default=1, help='example:n=1')
def dots(n):
    click.echo('.'*n)

# dots --n=3
if __name__ == '__main__':
    dots()
