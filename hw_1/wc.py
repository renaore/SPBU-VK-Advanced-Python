import click
import sys

@click.command()
@click.argument('files', nargs=-1, type=click.Path())
def wc(files):
    if (len(files) == 0):
        file = click.open_file("out.txt", "w")
        for line in sys.stdin:
            file.write(line)
        file.close()

        test_file = click.open_file("out.txt", 'rb')
        num_strings, num_words, num_bytes = 0, 0, 0
        for line in test_file:
            num_strings += 1
            num_words += len(line.split())
            num_bytes += len(line) - 1
        click.echo(str(num_strings) + ' ' + str(num_words) + ' ' + str(num_bytes))

    else:
        total_num_strings, total_num_words, total_num_bytes = 0, 0, 0
        for filename in files:
            test_file = click.open_file(filename, 'rb')
            num_strings, num_words, num_bytes = 0, 0, 0

            try:
                f_read = click.open_file(filename, "r")
                last_line = f_read.readlines()[-1]
                if (not last_line.endswith('\n')):
                    num_strings = -1
            except:
                pass

            for line in test_file:
                num_strings += 1
                num_words += len(line.split())
                num_bytes += len(line)
            total_num_strings += num_strings
            total_num_words += num_words
            total_num_bytes += num_bytes
            click.echo(str(num_strings) + ' ' + str(num_words) + ' ' + str(num_bytes) + ' ' + filename)

        if (len(files) != 1):
            click.echo(str(total_num_strings) + ' ' + str(total_num_words) + ' ' + str(total_num_bytes) + ' total')


if __name__ == '__main__':
    wc()
