import click
import os
import imdb
import re
import sys

ia = imdb.Cinemagoer()
movie_regex = r'(?P<title>.*)\s\((?P<year>\d+)\)\s-\s(?P<quality>.*)\.?(?:(?P<ext>\w+))'

@click.command()
@click.option('--input', '-t', default=sys.stdin, type=click.File('r'))
@click.option('--filter', '-f', default='', type=str)
@click.option('--rm', '-rm', is_flag=True, default=False)
def cli(input, filter, rm):
	"""Showcleaner CLI."""
	# filter_split = filter.split(',')
	# filter_json = {}
	# if len(filter_split) > 0:
	# 	for f in filter_split:
	# 		filter_split_2 = f.split('=')
	# 		filter_json[filter_split_2[0]] = filter_split_2[1]

	targets = []
	with input:
		targets = input.read().split('\n')
	targets = [t for t in targets if t]
	print(targets)
	for name in targets:
		print(name)
		match = re.search(movie_regex, name)
		if not match:
			print(f'Invalid file naming format for {name}')
			continue
		title = match.group('title') + " " + match.group('year')
		print(f'Searching for {title}')
		entries = ia.search_movie(title)
		if len(entries) == 0:
			print(f'Could not find IMDB entries for title "{title}"')
			continue
		entry = entries[0]
		
		# Get movie entry
		entry = ia.get_movie(entry.movieID)
		print(f'Found movie {repr(entry)}')
		# print(entry.infoset2keys)
		print(entry.get('rating'))
	pass