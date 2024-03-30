import click
import sys

@click.command()
@click.argument('filename', default="-", type=click.Path())
def nl(filename):
    if (filename == "-"):
        numberer = 1
        for line in sys.stdin:
            line = line.rstrip('\n')
            click.echo('     ' + str(numberer) + '  ' + line)
            numberer+=1
    else:
        test_file = click.open_file(filename)
        numberer = 1
        for line in test_file:
            line = line.rstrip('\n')
            click.echo('     ' + str(numberer) + '  ' + line)
            numberer += 1


if __name__ == '__main__':
    nl()
