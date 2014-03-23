def reduce_file_path(path):
    folders = list(filter(lambda x: x != '.', filter(None, path.split('/'))))

    for i in range(1, len(folders)):
        if folders[i] == '..':
            folders.remove(folders[i - 1])

    return '/' + '/'.join(list(filter(lambda x: x != '..', folders)))
