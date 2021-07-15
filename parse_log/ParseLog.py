import json


class LogParser:
    _arr_dict = []
    _default_ext = 'txt'
    _path = None

    def __init__(self, filename):
        self.filename = filename
        self.parse()

    def save(self, file_type=None, filename=None, output_path=''):
        fname = self._extract_fname_path() if filename is None else filename
        ext = '.' + self._default_ext if file_type is None else '.' + file_type

        path = None

        if output_path == '':
            path = fname[:fname.find('.log')] + ext
        else:
            path = output_path

        with open(path, 'w') as f:
            if file_type == 'json':
                json.dump(self._arr_dict, f, indent=2)
            else:
                for item in self._arr_dict:
                    values = list(item.values())
                    line = " ".join(values) + "\n"
                    f.write(line)

    def parse(self):
        _dict_container = {}
        with open(self.filename, 'r') as file:
            for line in file:
                splitted_line = line.split(', client')
                ctn_r = splitted_line[1].split(", ")
                ctn_l = splitted_line[0]
                _dict_container = self._parse_ctn_l(ctn_l)
                for i, item in enumerate(ctn_r):
                    key = item.split(': ')
                    if key[0] == '':
                        _dict_container['client'] = self._trim(key[1].strip())
                    else:
                        _dict_container[key[0].strip()] = self._trim(
                            key[1].strip())
                self._arr_dict.append(_dict_container)

    def _extract_fname_path(self):
        if self.filename.find('/') == -1:
            return self.filename
        else:
            split_path = self.filename.split('/')
            return split_path[-1]

    def _trim(self, string):
        if string.find('"') == -1:
            return string
        else:
            return string.replace('"', "")

    def _parse_ctn_l(self, ctn_l):
        foundColon = ctn_l.find(": ")

        message = ctn_l[foundColon + 2:].strip()
        properties = ctn_l[:foundColon].split(' ')
        date = ' '.join(properties[:2])
        level = properties[2].strip("[]")
        pid = properties[3].split("#")[0]
        tid = properties[3].split("#")[1]

        return {
            'date': date,
            'level': level,
            'PID': pid,
            'TID': tid,
            "message": message
        }

    def __repr__(self):
        return json.dumps(self._arr_dict, indent=2)
