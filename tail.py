import click
import sys

@click.command()
@click.argument('files', nargs=-1, type=click.Path())
def tail(files):
    if (len(files) == 0):
        list = []
        for line in sys.stdin:
            list.append(line.rstrip('\n'))
            if (len(list)>17):
                list.pop(0)
        for i in range (min(17, len(list))):
            click.echo(list[i])
    else:
        for filename in files:
            test_file = click.open_file(filename)
            list = []
            if (len(files)>1):
                click.echo('==> ' + filename + ' <==')
            for line in test_file:
                list.append(line.rstrip('\n'))
                if (len(list) > 10):
                    list.pop(0)
            for i in range(min(10, len(list))):
                click.echo(list[i])


if __name__ == '__main__':
    tail()
