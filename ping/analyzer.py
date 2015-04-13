
def lines_packager(lines):
    import re
    from datetime import datetime
    PATTERN_PING = re.compile(r'PING (.+?) \(.*\):')
    PATTERN_LOSS = re.compile(r'.*, (.+?) packets received, (.+?)% packet loss')
    PATTERN_TRIP = re.compile(r'round-trip min/avg/max/stddev = (.+?)/(.+?)/(.+?)/(.+?) ms')

    def packager(pkgs, line):
        if "CST" in line:
            pkg = {}
            timestr = line.replace("CST ", "").strip()
            pkg['time'] = datetime.strptime(timestr, '%c')
            pkgs.append(pkg)

        if not pkgs:
            return pkgs

        pkg = pkgs[-1]
        if "PING" in line:
            m = PATTERN_PING.match(line)
            if m:
                pkg['host'] = m.group(1)
        elif "packet loss" in line:
            m = PATTERN_LOSS.match(line)
            if m:
                pkg['count'] = int(m.group(1))
                pkg['loss'] = float(m.group(2))
        elif "round-trip" in line:
            m = PATTERN_TRIP.match(line)
            if m:
                pkg['min'] = float(m.group(1))
                pkg['avg'] = float(m.group(2))
                pkg['max'] = float(m.group(3))
                pkg['stddev'] = float(m.group(4))

        return pkgs

    initial = []

    return reduce(packager, lines, initial)

def package_validater(pkgs):
    def validation(pkg):
        keys = [ 'time', 'host', 'count', 'loss' ]
        elkeys = [ 'min', 'avg', 'max', 'stddev' ]
        for key in keys:
            if not key in pkg:
                return False
        for key in elkeys:
            if not key in pkg:
                pkg[key] = 0.0

        return True;

    return filter(validation, pkgs)

def package_summerize(pkgs):
    if not pkgs:
        return {}

    import math

    def merge(a, b):
        pkg = {}
        sqa = a['stddev']**2
        sqb = b['stddev']**2
        na = a['count']
        nb = b['count']
        va = a['avg']
        vb = b['avg']

        pkg['host'] = b['host']
        pkg['count'] = na + nb
        pkg['loss'] = (a['loss'] * na + b['loss'] * nb) / pkg['count']
        pkg['min'] = min(a['min'], b['min'])
        pkg['max'] = max(a['max'], b['max'])
        pkg['avg'] = (va * na + vb * nb) / pkg['count']

        # calculate the std dev, it's a little complex.
        sq = (na*sqa + nb*sqb) / pkg['count'] - na * nb / pkg['count']**2 * (va - vb)**2
        pkg['stddev'] = math.sqrt(sq)
        return pkg

    return reduce(merge, pkgs)

def file_summerize(fname):
    from utils import pipeline_func

    s = None
    with open(fname) as f:
        lines = f.readlines()
        s = pipeline_func(lines, [
            lines_packager,
            package_validater,
            package_summerize
            ])

    return s

def pkg_score(pkg):
    loss = pkg['loss'] / 30.0
    delay = pkg['avg'] / 500.0
    std = pkg['stddev'] / 70.0
    score = (loss * 10 + delay + std) / 5
    return score


